# Design System — Della Sigrest Portfolio

**Last Updated:** April 2026  
**Status:** Active (used with Stitch + Cursor)  
**Platform:** Static HTML/CSS/JS (no build step)

---

## COLOR PALETTE

### Core Neutrals (Dark Mode)
```
--bg:             #0b0b0b    (Pure black background)
--surface:        #131313    (Primary surface for cards, sections)
--surface-hover:  #191919    (Slightly lighter on hover/focus)
--surface-alt:    #0f0f0f    (Darker alternate surface, optional)
--surface-bright: #1a1a1a    (Brighter surface for emphasis)
```

### Text Colors
```
--text-primary:   #e8e8e8    (Main body text, headings)
--text-secondary: #888       (Descriptive text, metadata)
--text-tertiary:  #555       (Muted text, disabled states)
```

### Borders & Dividers
```
--border:       #1e1e1e     (Primary border color)
--border-hover: #2a2a2a     (Elevated border on hover)
--border-soft:  rgba(255, 255, 255, 0.04)  (Subtle dividers)
```

### Accent Color (Teal)
```
--accent:           #2dd4bf   (Primary brand color)
--accent-dim:       rgba(45,212,191,0.08)   (Background wash)
--accent-hover:     rgba(45,212,191,0.14)   (Hover state)
--accent-muted:     rgba(45, 212, 191, 0.2) (Muted variant)
```

### Shadows
```
--shadow-sm:  0 1px 2px 0 rgba(0, 0, 0, 0.05)      (Subtle depth)
--shadow-md:  0 4px 6px -1px rgba(0, 0, 0, 0.1)    (Card base)
--shadow-lg:  0 20px 25px -5px rgba(0, 0, 0, 0.1)  (Elevated)
```

---

## TYPOGRAPHY

### Font Family
```
Primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
Weight Range: 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold)
Line Height Base: 1.6
```

### Type Scale

#### Page Headings
| Usage | Size | Weight | Line Height | Letter Spacing |
|-------|------|--------|-------------|----------------|
| H1 (Hero) | clamp(34px, 4.5vw, 52px) | 700 | 1.12 | -0.03em |
| H1 (Case Study) | clamp(32px, 4vw, 48px) | 700 | 1.12 | -0.03em |
| H1 (About) | clamp(32px, 4vw, 44px) | 700 | 1.15 | -0.03em |

#### Section Headings
| Usage | Size | Weight | Line Height | Letter Spacing |
|-------|------|--------|-------------|----------------|
| H2 (Case Body) | 24px | 700 | 1.0 | -0.02em |
| H2 (About) | 20px | 700 | 1.0 | -0.01em |
| H3 (Pillar) | 16px | 600 | 1.0 | -0.01em |
| Section Label | 13px | 600 | 1.0 | 0.08em (uppercase) |

#### Body Text
| Usage | Size | Weight | Line Height | Color |
|-------|------|--------|-------------|-------|
| Body (Long Form) | 16px | 400 | 1.8 | --text-secondary |
| Hero Subtitle | 17px | 400 | 1.75 | --text-secondary |
| Case Description | 14px | 400 | 1.65 | --text-secondary |
| Metadata | 12px | 500 | 1.0 | --text-tertiary |
| Eyebrow | 14px | 500 | 1.0 | --text-secondary |

#### Labels & Meta
```
Case Tag: 11px, weight 600, uppercase, letter-spacing 0.05em
Year/Date: 12px, weight 400, color --text-tertiary
Metric Label: 12px, weight 400, color --text-tertiary
```

---

## SPACING SYSTEM

### Base Unit
**1 unit = 4px** (all values scale from this)

### Semantic Spacing

#### Navigation
```
--nav-h:      64px   (Fixed nav height)
--side-pad:   clamp(24px, 5vw, 64px)  (Responsive horizontal padding)
```

#### Vertical Rhythm (Sections)
```
Hero Section Bottom:     80px
Pillar Section Bottom:   80px
Case Cards Bottom:       120px
Footer Padding:          40px (top/bottom)
Case Study Bottom:       120px
```

#### Component Padding

| Component | Padding |
|-----------|---------|
| Pillar Card | 40px (vertical), 36px (horizontal) |
| Case Card Content | 28px (vertical), 32px (horizontal) |
| Case Body | 60px (vertical), var(--side-pad) (horizontal) |
| About Body | 40px (vertical), var(--side-pad) (horizontal) |
| Metric Card | 24px |
| Callout Box | 20px (vertical), 24px (horizontal) |

#### Component Gaps
```
Nav Links:        32px
Hero Elements:    24px (eyebrow to title), 24px (title to subtitle), 48px (subtitle to CTA)
Pillar Grid:      1px (creates border effect)
Case Cards Grid:  16px (vertical stack)
Meta Items:       24px (grid gap)
Footer Links:     24px
```

### Margins Between Content Blocks
```
H2 to paragraph:        20px
Paragraph to paragraph: 20px
H2 to H2:               64px (top margin)
List items:             10px (between items)
Blockquote:             32px (margin top/bottom)
Metric row:             32px (margin top/bottom)
```

---

## BORDER & RADIUS

### Border Radius
```
--radius:    14px   (Primary, most components)
--radius-sm: 8px    (Smaller elements, tags, pills)
```

### Border Width
```
Default:    1px
Prominent:  1.5px (hero CTA, emphasis states)
```

### Border Strategy
```
Primary borders:   var(--border) at 1px
Hover borders:     var(--border-hover) at 1px
Soft dividers:     var(--border-soft) at 1px (metadata grids)
Accent borders:    var(--accent) with reduced opacity for subtle states
```

---

## SHADOW HIERARCHY

### Application Rules

#### Level 1: Subtle (Baseline)
```
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05)
Usage: Minimal depth, used sparingly at rest state
```

#### Level 2: Card (Standard)
```
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1)
Usage: Default for case cards, metric cards
```

#### Level 3: Elevated (Hover)
```
box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 0 0 1px var(--accent-dim)
Usage: .case-card:hover, interactive elements on elevation
```

#### Level 4: Maximum (Special)
```
box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.25)
Usage: Reserved for modals or major elevation (currently unused)
```

---

## TRANSITIONS & ANIMATIONS

### Timing Tokens
```
--transition:      0.25s cubic-bezier(0.4, 0, 0.2, 1)  (Standard easing)
--transition-fast: 0.15s ease                           (Quick feedback)
```

### Interaction Patterns

#### Hover States
```
Color change:       var(--transition)
Transform shift:    var(--transition) (typically translateY(-3px) to -4px)
Shadow elevation:   var(--transition)
Border color:       var(--transition)
```

#### Scroll Animations
```
Entrance (h2, metrics, images):
  - From: opacity 0, translateY(16px)
  - To: opacity 1, translateY(0)
  - Duration: 0.6s ease
  - Timeline: view() entry 0% cover 25%
```

#### Micro-interactions
```
CTA arrow hover:    transform var(--transition), translateY(3px)
Link underline:     text-decoration-color var(--transition)
Card number hover:  color var(--transition) from --text-tertiary to --accent
```

### Reduced Motion
```
When prefers-reduced-motion: reduce
- animation-duration: 0.01ms !important
- transition-duration: 0.01ms !important
- .fade-in opacity: 1, transform: none
```

---

## LAYOUT SYSTEM

### Max Width
```
--max-w: 1120px (Content constraint)
```

### Grid System

#### Pillars (2-column on desktop)
```
grid-template-columns: repeat(2, 1fr)
gap: 1px (creates subtle grid border effect)
```

#### Case Cards (1 column)
```
grid-template-columns: 200px 1fr (image | content)
gap: none (seamless)
```

#### Meta Grid (Case Studies)
```
grid-template-columns: repeat(auto-fit, minmax(140px, 1fr))
gap: 24px
```

#### Metrics Row
```
grid-template-columns: repeat(auto-fit, minmax(160px, 1fr))
gap: 16px
```

### Responsive Breakpoints

#### 768px and Below (Tablet)
- Nav links hide (mobile menu)
- Hero h1: 32px
- Pillars: grid-template-columns: 1fr (single column)
- Case cards: grid-template-columns: 1fr (stack vertically)
- Case meta: grid-template-columns: 1fr 1fr (2-column)
- Metrics: grid-template-columns: 1fr 1fr (2-column)
- Placeholder grid (cols-3): grid-template-columns: 1fr 1fr

#### 480px and Below (Mobile)
- Pillars: border-radius: 0, margin: full-width, border-left/right: removed
- Case cards: border-radius: var(--radius-sm)
- Placeholder grids (cols-2, cols-3): grid-template-columns: 1fr
- Placeholder min-height: 140px

---

## COMPONENT PATTERNS

### Navigation
```
Fixed positioning, top: 0, z-index: 100
Height: var(--nav-h) = 64px
Background: rgba(11,11,11,0.88) with backdrop-filter: blur(24px)
Active state: Underline with --accent color, 1.5px height
Mobile toggle: 28px width × 20px height, hamburger icon
```

### Hero Section
- Min-height: 100vh
- Padding top: calc(var(--nav-h) + 40px)
- Padding bottom: 80px
- Eyebrow: flex with decorative line (32px width, 1px height)
- CTA button: inline-flex, 13px padding vertical, 26px horizontal, border-radius: var(--radius-sm)

### Pillar Cards
- Padding: 40px vertical, 36px horizontal
- Background: var(--surface)
- Hover: background transitions to var(--surface-hover)
- Border: 1px solid var(--border) (grid gap creates appearance)

### Case Card
- Layout: 200px image column | content column
- Image area: min-height 160px, background: var(--accent-dim)
- Content padding: 28px vertical, 32px horizontal
- Case number: 32px, weight 700, transitions color on hover
- Tag: 11px uppercase, 3px vertical padding, 10px horizontal, border-radius: 100px
- Link: transitions color on hover to --accent

### Case Study Page
- Hero: padding top calc(var(--nav-h) + 60px)
- Body: max-width 720px, padding 60px vertical, var(--side-pad) horizontal
- Heading (h2): 24px, weight 700, margin-top 64px, margin-bottom 20px
- List items: 15px, color --text-secondary, padding-left 20px for bullet
- Bullet: 6px circle, background --accent, opacity 0.6

### Metric Card
- Background: var(--surface)
- Border: 1px solid var(--border)
- Border-radius: var(--radius-sm)
- Padding: 24px
- Number: 28px, weight 700, color --accent
- Label: 12px, color --text-tertiary, text-align: center

### Callout / Blockquote
- Border-left: 3px solid var(--accent)
- Background (callout): var(--accent-dim)
- Padding-left: 20px (blockquote), 20px 24px (callout)
- Border-radius (callout): var(--radius-sm)

---

## DESIGN PRINCIPLES

### Dark Mode Best Practices
- Use reduced contrast for secondary text (avoid pure white on black)
- Add breathing room: 20-30% more padding than light mode equivalent
- Layer surfaces with subtle elevation to create depth
- Use accent color strategically — restraint is key

### Accessibility
- WCAG AA compliance minimum
- Text contrast ratio: 4.5:1 for body text
- Interactive elements: 44px × 44px minimum touch target
- Motion: respects prefers-reduced-motion

### Typography Hierarchy
- H1 commands attention; typically used once per page
- H2 breaks sections; establishes rhythm
- Body text defaults to secondary color for visual rest
- Accent color draws eye to key actions

### Interaction Design
- Hover states provide feedback on all interactive elements
- Transitions are consistent (0.25s easing)
- Loading states should be obvious (opacity, transform, color)
- Disabled states reduce opacity or gray out

---

## IMPLEMENTATION NOTES FOR CLAUDE / STITCH

### CSS Variables
All design tokens are defined in `:root {}` selector. Update tokens there, and all components automatically adapt.

### Adding New Components
1. Create class (e.g., `.new-element`)
2. Reference tokens: `color: var(--text-primary)`, `transition: var(--transition)`
3. Define semantic colors (don't hardcode hex values)
4. Test on both light/dark (if applicable) and with motion preferences

### Exporting to DESIGN.md
Whenever significant changes are made:
1. Extract all updated token values from `styles.css :root {}`
2. Update this file with new values
3. Export to Stitch or share with Claude via MCP

### Performance Considerations
- No web fonts except Inter (already loaded)
- Transitions use GPU-accelerated properties (transform, opacity)
- Smooth scrolling enabled (`scroll-behavior: smooth`)
- Backdrop filters on nav (minor performance cost, acceptable trade)

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 2026 | Initial design system extraction from styles.css |
| | | Added Stitch + Cursor integration notes |
| | | Documented spacing, color, and component patterns |

---

**Prepared for:** Della Sigrest  
**Exported by:** Design System Assistant  
**For use with:** Stitch 2.0, Cursor IDE, Claude Code