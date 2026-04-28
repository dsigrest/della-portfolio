#!/usr/bin/env python3
"""Inject a postMessage height publisher into every diagram HTML embedded
on case-notifications.html. Idempotent — re-running won't double-add.

The marker comment `<!-- diagram-height-poster v1 -->` is how we detect
prior injection.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "case-notifications.html"
DIAG_DIR = ROOT / "img" / "diagrams"

MARKER = "<!-- diagram-height-poster v1 -->"
SCRIPT = """\
""" + MARKER + """
<script>
(function () {
  function compute() {
    var d = document.querySelector('.diagram');
    if (!d) return 0;
    return Math.max(
      d.scrollHeight, d.offsetHeight,
      document.documentElement ? document.documentElement.scrollHeight : 0,
      document.body ? document.body.scrollHeight : 0
    );
  }
  function send() {
    if (!window.parent || window.parent === window) return;
    var h = compute();
    if (h > 0) {
      window.parent.postMessage({ type: 'diagram-height', height: h }, '*');
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', send);
  } else {
    send();
  }
  window.addEventListener('load', send);
  // Re-send to catch font swaps, image loads, animations.
  setTimeout(send, 50);
  setTimeout(send, 250);
  setTimeout(send, 1000);
  if (window.ResizeObserver) {
    var ro = new ResizeObserver(send);
    var d = document.querySelector('.diagram');
    if (d) ro.observe(d);
    if (document.body) ro.observe(document.body);
  }
  window.addEventListener('resize', send);
})();
</script>
"""


def find_embedded_filenames():
    """Return the set of img/diagrams/*.html files currently embedded."""
    txt = CASE.read_text(encoding="utf-8")
    # match  src="img/diagrams/<file>.html"
    rx = re.compile(r'src="img/diagrams/([^"]+\.html)"')
    return set(rx.findall(txt))


def inject(path: Path, dry_run: bool = False) -> str:
    """Inject script before </body>. Returns 'added', 'skip', or 'noop'."""
    txt = path.read_text(encoding="utf-8")
    if MARKER in txt:
        return "skip"
    if "</body>" not in txt:
        return "noop"
    new = txt.replace("</body>", SCRIPT + "</body>", 1)
    if not dry_run:
        path.write_text(new, encoding="utf-8")
    return "added"


def main():
    dry = "--dry-run" in sys.argv
    embedded = find_embedded_filenames()
    print(f"Found {len(embedded)} embedded diagrams in case-notifications.html")
    counts = {"added": 0, "skip": 0, "noop": 0, "missing": 0}
    for name in sorted(embedded):
        p = DIAG_DIR / name
        if not p.exists():
            print(f"  [missing] {name}")
            counts["missing"] += 1
            continue
        result = inject(p, dry)
        counts[result] += 1
        print(f"  [{result}] {name}")
    print()
    print("Summary:", counts, "(dry-run)" if dry else "")


if __name__ == "__main__":
    main()
