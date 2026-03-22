# Priority 3: Engagement Levers Bundle (45% → 55% Completion)
## 4 HTML Prototypes — 2026-03-22

All prototypes use the Doctolib Chrome Shell baseline with complete CSS, sidebar, header, and sub-sidebar. Only the `<main class="content">` section is customized per prototype.

---

## Proto P3A: Full Stack Bundle
**File:** `proto-p3a-full-bundle.html`

**Concept:** Complete engagement suite combining all three levers in one unified experience.

**Key Features:**
- TLE specialist cards with green checkmark badges ("✓ TLE Accepted")
- Notification preferences panel (push notifications, digests, reminders)
- Campaign Dashboard showing 500 enrolled specialists, 65% enrollment rate
- 4-card metric grid with request counts and response times
- All features visible simultaneously, showing full integration

**Visual Distinction:** Heavy badge usage + right sidebar panel + prominent metrics cards. Most feature-rich option.

---

## Proto P3B: Lightweight Badging Only
**File:** `proto-p3b-badging-only.html`

**Concept:** Minimal viable feature—just badges + a simple filter toggle.

**Key Features:**
- Green checkmark badges on specialist cards (some have, some don't)
- "Show only TLE-accepting specialists" checkbox at top
- JavaScript filter hides non-badged cards when checkbox is checked
- Clean, streamlined specialist grid without extra panels
- No campaign dashboard, no notification settings

**Visual Distinction:** Filter functionality only. Simplest, fastest to implement. Most lightweight.

---

## Proto P3C: Campaign Management (Admin View)
**File:** `proto-p3c-campaign-first.html`

**Concept:** Admin/ops-focused specialist recruitment dashboard.

**Key Features:**
- Campaign creation form (specialty + region selectors)
- Email template preview with Doctolib branding
- 5-metric KPI cards: Sent (500), Opened (68%), Clicked (36%), Enrolled (19%), ROI (4.5x)
- Conversion funnel visualization with horizontal bar charts
- Full outreach flow from send to enrollment tracking

**Visual Distinction:** Campaign dashboard focus, email templates, conversion metrics. Admin/specialist supply perspective.

---

## Proto P4D: Phased Rollout Timeline
**File:** `proto-p3d-phased-rollout.html`

**Concept:** Structured deployment plan with metric gates between phases.

**Key Features:**
- Vertical timeline with 4 phases:
  - Phase 1 (Week 2): Badging — Gate: >50 specialists badged ✓ PASSED (120)
  - Phase 2 (Week 5): Response UX — Gate: <24h response ✓ PASSED (14h)
  - Phase 3 (Week 8): Push Notifications — Gate: >70% opt-in (IN PROGRESS 62%)
  - Phase 4 (Week 12): Campaign — Gate: >65% enrollment (BLOCKED, awaiting Phase 3)
- Visual indicators: green checkmarks (passed), gray dots (pending)
- Dependency arrows showing gate requirements
- Blue info box explaining measurement gates

**Visual Distinction:** Roadmap/timeline view with dependency management. Risk-mitigation approach with explicit gates.

---

## Design Consistency Across All 4 Prototypes

### Chrome Shell (Identical)
- Left sidebar (76px, navy icon rail) — unchanged
- Top header (navy, 52px) — unchanged
- Sub-sidebar (Connect section, white, 230px) — unchanged
- All CSS variables and design tokens — unchanged
- All SVG icons and navigation structure — unchanged

### Floating Nav Bar (All 4)
- Fixed position bottom-center, dark navy background (#1B2A4A)
- "← Home" link + P3 badge + 4 option buttons (A, B, C, D)
- Active option: light blue text (#5BC0F0) + semi-transparent blue background
- Inactive options: white text + hover effect (subtle background)
- Each option links to its respective prototype

### Typography & Spacing
- Font: Open Sans (already in baseline)
- Design tokens: --dtl-blue (#0596DE), --dtl-gray-*, --dtl-success-*, etc.
- Buttons: 6px border-radius, white text on blue (#0596DE) background
- Cards: 1px solid border, 8px border-radius, white background

### Content Metrics
- P3A: 2,315 lines (full features)
- P3B: 2,288 lines (minimal features)
- P3C: 2,310 lines (dashboard focus)
- P3D: 2,283 lines (roadmap focus)

All files include closing `</html>` tag and floating nav before `</body>`.

---

## How to Test Locally
1. Open any `.html` file in a browser
2. Click nav buttons A, B, C, D at bottom to navigate between prototypes
3. Each prototype maintains the full Doctolib chrome (sidebar, header, layout)
4. Floating nav shows which option is currently active (blue highlight)

---

## Key Differentiation Points

| Aspect | P3A | P3B | P3C | P3D |
|--------|-----|-----|-----|-----|
| **Focus** | Full Suite | Badge Filter | Campaign Mgmt | Phased Risk |
| **Visual** | Badges + Sidebar + Metrics | Filter Checkbox | Email + Funnels | Timeline Gates |
| **Target User** | PM/Leadership | Practitioner | Admin/Ops | Leadership/Risk |
| **Complexity** | High | Low | Medium | Medium |
| **Implementation Speed** | Slow | Fast | Medium | Medium-Slow |
| **Engagement Lever(s)** | All 3 (badges, push, campaign) | Badging only | Campaign only | Phased rollout |
| **JavaScript** | None (static) | Toggle filter | Static metrics | Static timeline |

---

## Files in This Directory

```
2026-03-22-3-ai-pm-agent-run-tle/
├── proto-p3a-full-bundle.html          (Full engagement suite)
├── proto-p3b-badging-only.html         (Lightweight badge + filter)
├── proto-p3c-campaign-first.html       (Admin campaign dashboard)
├── proto-p3d-phased-rollout.html       (Deployment roadmap)
├── PROTOTYPES_SUMMARY.md               (this file)
└── index.html                          (home page / nav hub)
```

All prototypes are self-contained, complete HTML files (no external dependencies beyond Google Fonts CDN).
