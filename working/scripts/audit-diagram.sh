#!/usr/bin/env bash
# audit-diagram.sh — figma-to-html drift detector
# Usage:   ./audit-diagram.sh <file.html> [<file.html> ...]
# Exit 0 = all files pass (no FAIL). Exit 1 = at least one FAIL detected.
# WARN does not fail the audit but is surfaced for human review.
#
# What this catches (Day 2 systemic-fix Layer 3):
#   1. Required project palette tokens absent
#   2. Forbidden variable names (drift indicators)
#   3. Light-theme defaults (the NOT-12 / NOT-06 failure mode)
#   4. Missing iframe infrastructure (.diagram wrapper, body.embedded, height-poster v1)
#   5. Debug visual artifacts (green debug borders, oversized watermark text)
#   6. localhost:3845 asset references
#   7. iframe-width rule violations (1-col grid collapse above 480px)
#   8. WARN on hover/click handlers (sometimes wanted, often debug residue)

set -u

GLOBAL_FAIL=0

audit_one() {
  local file="$1"
  local fail=0
  local checks=()

  if [ ! -f "$file" ]; then
    echo "ERROR: file not found: $file"
    return 2
  fi

  echo ""
  echo "=== $(basename "$file") ==="

  # 1. Required palette tokens --------------------------------------------------
  # Note: -- before the pattern tells grep to stop option parsing (since tokens start with --)
  for token in \
    "--canvas: #0A0C16" \
    "--card: #10121C" \
    "--text-pri: #E0DFE4" \
    "--text-sec: rgba(224,223,228,0.6)" \
    "--accent: #7FB5B0"; do
    if ! grep -qF -- "$token" "$file"; then
      echo "  FAIL: missing required palette token: $token"
      fail=1
    fi
  done

  # 2. Forbidden variable names (drift signatures) ------------------------------
  for forbidden in \
    "--canvas-bg" \
    "--bg-primary" \
    "--text-primary" \
    "--text-secondary" \
    "--accent-teal" \
    "--border-green" \
    "--text-muted" \
    "--ellipse-before" \
    "--ellipse-after"; do
    if grep -qF -- "$forbidden" "$file"; then
      echo "  FAIL: forbidden variable name (drift signature): $forbidden"
      fail=1
    fi
  done

  # 3. Light-theme markers ------------------------------------------------------
  # Scoped to: --canvas variable, --canvas-bg variable, or body { background ... }
  # Allows white as bezel/icon stroke on inner elements (e.g. phone mock borders).
  if grep -qiE "^[[:space:]]*--canvas[a-z-]*:[[:space:]]*(#fafafa|#ffffff|#fff[[:space:]]*[;}]|#f8f8f8|#fff[a-f0-9]{0,3}[[:space:]]*[;}])" "$file"; then
    echo "  FAIL: --canvas* variable set to light value (light-theme drift)"
    fail=1
  fi
  # body background as light value
  if awk '/body[[:space:]]*\{/,/\}/' "$file" | grep -qiE "background[a-z-]*:[[:space:]]*(#fafafa|#ffffff|#fff[[:space:]]*[;}]|#f8f8f8)"; then
    echo "  FAIL: body background set to light value (light-theme drift)"
    fail=1
  fi

  # 4. Iframe infrastructure ----------------------------------------------------
  if ! grep -qF "classList.add('embedded')" "$file"; then
    echo "  FAIL: missing body.embedded toggle script"
    fail=1
  fi
  if ! grep -qF "diagram-height-poster v1" "$file"; then
    echo "  FAIL: missing height-poster v1 marker comment"
    fail=1
  fi
  # .diagram wrapper class — must exist as a class attribute, not just .diagram-container
  if ! grep -qE "class=\"diagram\"|class='diagram'|class=\"diagram [a-z]|class='diagram [a-z]" "$file"; then
    echo "  FAIL: no .diagram wrapper class (may be using .diagram-container — non-standard)"
    fail=1
  fi
  # Body.embedded CSS rule — must style transparent + zero padding
  if ! grep -qE "body\.embedded[[:space:]]*\{" "$file"; then
    echo "  FAIL: missing body.embedded CSS rule"
    fail=1
  fi

  # 5. Forbidden visuals --------------------------------------------------------
  # Debug green border (the NOT-14 case)
  if grep -qE "border:[[:space:]]*[0-9]+px[[:space:]]+solid[[:space:]]+(#22[Cc]55[Ee]|#00[Ff]{2}00|var\(--border-green\))" "$file"; then
    echo "  FAIL: debug green border detected"
    fail=1
  fi
  # Watermark-sized text (font-size 100px+)
  if grep -qE "font-size:[[:space:]]*(1[0-9]{2}|[2-9][0-9]{2})px" "$file"; then
    echo "  FAIL: watermark-sized text (font-size > 100px) — likely debug residue"
    fail=1
  fi

  # 6. Asset URL hygiene --------------------------------------------------------
  if grep -qF "localhost:3845" "$file"; then
    echo "  FAIL: localhost:3845 asset reference (won't resolve)"
    fail=1
  fi

  # 7. iframe-width rule --------------------------------------------------------
  # Look for @media (max-width: 5xx-9xx or 1xxx) blocks containing
  # grid-template-columns: 1fr — that's a 1-col collapse above 480px.
  awk '
    /@media[[:space:]]*\([[:space:]]*max-width:[[:space:]]*([5-9][0-9][0-9]|[1-9][0-9]{3})/ {
      flag=1; bound=NR+25; mw=$0
    }
    flag && NR<bound && /grid-template-columns:[[:space:]]*1fr[[:space:]]*[;}]/ {
      print "VIOLATION: 1-col collapse above 480px at line " NR " (block starts: " mw ")"
      flag=0
      exit_code=1
    }
    /\}/ { flag=0 }
    END { exit (exit_code+0) }
  ' "$file" || { echo "  FAIL: iframe-width rule violated (above)"; fail=1; }

  # 8. Hover handlers (WARN, not fail) ------------------------------------------
  # Use grep -c which prints a single integer; pipe through head -1 to be safe
  hover_count=$(grep -cE ":hover|cursor:[[:space:]]*pointer|addEventListener\(['\"]click" "$file" 2>/dev/null | head -1)
  hover_count=${hover_count:-0}
  if [ "$hover_count" -gt 0 ] 2>/dev/null; then
    echo "  WARN: $hover_count hover/click hook(s) detected — confirm intentional vs debug residue"
  fi

  # 9. Old-style heightUpdate message (Day 1 leftover) --------------------------
  if grep -qF "type: 'heightUpdate'" "$file" || grep -qF 'type: "heightUpdate"' "$file"; then
    echo "  FAIL: old-style 'heightUpdate' postMessage (parent listens for 'diagram-height')"
    fail=1
  fi

  if [ $fail -eq 0 ]; then
    echo "  PASS"
  else
    echo "  --- FAILED ---"
    GLOBAL_FAIL=1
  fi

  return $fail
}

# Main: iterate over args
if [ $# -eq 0 ]; then
  echo "Usage: $0 <file.html> [<file.html> ...]"
  echo "       $0 img/diagrams/diagram-*-v5.html"
  exit 2
fi

for f in "$@"; do
  audit_one "$f" || true   # don't let set -e exit on individual fail
done

echo ""
if [ $GLOBAL_FAIL -eq 0 ]; then
  echo "=== ALL PASS ==="
  exit 0
else
  echo "=== AT LEAST ONE FAIL ==="
  exit 1
fi
