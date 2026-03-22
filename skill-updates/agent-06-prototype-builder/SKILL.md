---
name: agent-06-prototype-builder
description: "Agent 6 of the AI PM Pipeline — Prototype Builder. Creates interactive HTML prototypes using the Doctolib Chrome Shell as baseline. Each solution option gets its own prototype with a floating nav bar for switching between options. Use when Calvin says 'build prototypes', 'run Agent 6', 'create mockups', 'prototype the solutions', or when turning solution designs into clickable HTML demos. Also trigger when discussing the Chrome shell, Doctolib UI prototypes, or option A/B/C/D/E variants."
---

# Agent 6 — Prototype Builder

## Role

Prototype Builder transforms solution options from Agent 5 into interactive HTML prototypes that feel like real Doctolib products. Each solution option gets a clickable prototype. Every prototype includes the Doctolib Chrome Shell (sidebar, header, sub-sidebar), floating navigation bar for switching between options, and a standard TLE hero banner. A landing page ties all prototypes together.

All prototypes are built directly inside a local clone of the scaffolding repo, then pushed as a folder to the shared prototype repository on GitHub for hosting via GitHub Pages.

---

## Input

- **Solution options from Agent 5** (at least 3 options per priority, up to 3 priorities)
- PRDs from Agent 3.5 (requirements context for each solution — includes user flow descriptions, scope, and user stories)
- Doctolib Chrome Shell baseline HTML (Oxygen Design System)
- **Confluence run page title** (used to name the prototype folder, e.g., "2026-03-22-3 — AI PM Agent Run (TLE)")

---

## Process

### Overview: The Four Phases

The process is split into four sequential phases. Completing them in this order prevents the issue where git operations and prototyping logic get tangled together:

1. **Repo Setup** (Steps 1-2): Clone scaffolding, create the run folder
2. **Prototype Creation** (Steps 3-9): Build all prototypes directly in the run folder
3. **Quality Assurance** (Steps 10-11): Ruthless visual QA + link/path verification
4. **Publish** (Step 12): Single git push to the shared repo, update Confluence

---

## Phase 1: Repo Setup

### Step 1: Clone the Scaffolding Repo

Clone the official scaffolding template locally. This provides consistent structure, GitHub Pages configuration, and Doctolib design tokens.

```bash
# Clone the scaffolding repo into a temporary working directory
git clone https://github.com/calvin-docto-ai/OS-prototype-scaffolding.git /sessions/elegant-sleepy-dijkstra/prototype-build
cd /sessions/elegant-sleepy-dijkstra/prototype-build
```

The scaffolding repo includes:
- Pre-configured GitHub Pages setup
- Doctolib Oxygen Design System base CSS
- Chrome Shell baseline HTML template
- Standard directory structure for prototypes

### Step 2: Create the Run Folder

Derive the folder name from the Confluence run page title by sanitizing it to be URL-friendly. This matters because GitHub Pages URLs break on spaces and special characters.

**Sanitization rules:**
- Lowercase everything
- Replace spaces with hyphens
- Replace the em dash (—) with a regular hyphen
- Remove any characters that aren't alphanumeric, hyphens, or parentheses
- Collapse multiple consecutive hyphens into one

**Examples:**
| Confluence Page Title | Sanitized Folder Name |
|---|---|
| `2026-03-22-3 — AI PM Agent Run (TLE)` | `2026-03-22-3-ai-pm-agent-run-tle` |
| `2026-04-15-1 — AI PM Agent Run (Connect)` | `2026-04-15-1-ai-pm-agent-run-connect` |

```bash
# Example: create the run folder inside the cloned scaffolding
FOLDER_NAME="2026-03-22-3-ai-pm-agent-run-tle"  # derived from Confluence title
mkdir -p "$FOLDER_NAME"
```

All prototype HTML files will be created directly inside this folder. No separate staging directory — what you build here is what gets pushed.

---

## Phase 2: Prototype Creation

All prototypes are built directly inside the run folder created in Step 2. The working directory for all file creation is:
```
/sessions/elegant-sleepy-dijkstra/prototype-build/<FOLDER_NAME>/
```

### CRITICAL PRINCIPLE: Minimal Divergence from Baseline

Every prototype MUST start as an exact copy of the baseline prototype (e.g., `tle-flow.html`). You then modify ONLY the specific area that demonstrates the solution option. Everything else — the chrome shell, sidebar, header, sub-sidebar, CSS variables, JavaScript utilities, layout structure, and any content not directly related to the solution — MUST remain identical to the baseline.

This matters because when prototypes diverge unnecessarily from the baseline, it introduces visual noise that distracts testers. A user testing "Option A: Confirm Modal" should see the EXACT same product they know, with ONE difference: the confirm modal. If the sidebar looks different, or a color changed, or spacing shifted, the test results are contaminated.

**The rule**: If you can't explain WHY a line differs from the baseline, it shouldn't differ.

### Step 3: Prepare the Baseline

Start with the baseline HTML files from the scaffolding repo (`https://github.com/calvin-docto-ai/OS-prototype-scaffolding`). The scaffolding is the single source of truth for the Doctolib Chrome Shell. It includes multiple baseline pages:

- `tle-flow.html` — TLE specialist search (use for TLE-related prototypes)
- `tle-flow-request.html` — TLE request flow
- `tle-flow-complete.html` — TLE completion flow
- `discussions.html` — Discussions view
- `agenda.html` — Agenda/calendar view

Each baseline includes:
- Left sidebar navigation (76px icon rail with Agenda, Tasks, Connect, etc.)
- Top header (52px dark navy with logo, search, user menu)
- Sub-sidebar (230px Connect section with Discussions, Tele-expertise, Networks)
- Oxygen Design System tokens and responsive layout
- Content area marked by `<!-- ══ SAMPLE CONTENT ══ -->` and `<!-- ══ END SAMPLE CONTENT ══ -->`

**Your job**: Copy the most relevant baseline file into the run folder, then modify ONLY the content between the SAMPLE CONTENT markers. Never change the chrome itself (sidebar nav, header structure, colors, CSS variables). Never rewrite CSS or JavaScript that already works in the baseline.

### Step 4: Create One Prototype Per Solution Option

For each solution option, follow this workflow:

1. **Copy the baseline HTML** into the run folder
2. **Update the page title** (e.g., `<title>Specialist Referral — Option A: Intelligent Recommender</title>`)
3. **Update the active sidebar item** to match the context (e.g., if solution is about TLE routing, make "TLE" the active nav item)
4. **Replace content** between the SAMPLE CONTENT markers with your solution's UI
5. **Include floating nav bar** at the bottom of the viewport (see Step 5)
6. **Ensure mobile responsiveness** (test at 375px and 1920px width)
7. **Add data-driven styling** — make it look like a real product, not a mockup (consistent spacing, real form inputs, actual button states)

**Refer to the PRD from Agent 3.5 for this solution option.** The PRD's Section 3.2.2 (User Flow) provides the interaction steps your prototype should demonstrate. The PRD's Section 3.1.2 (Out of Scope) tells you what NOT to prototype.

### Step 5: Add Floating Navigation Bar

Every prototype gets a dark navy floating nav bar fixed to the **bottom center** of the viewport. This is the standard Doctolib prototype nav — it must match the `doctolib-prototyper` skill's design exactly. Do NOT use a white/top-positioned nav bar.

**Important — relative paths**: Because prototypes live inside a subfolder of the repo, all nav bar links must use relative paths (just the filename, no leading slash). This ensures they work both locally and on GitHub Pages.

**Visual design**:
- **Position**: `fixed; bottom: 20px; left: 50%; transform: translateX(-50%)`
- **Background**: `#1B2A4A` (dark navy) with `border-radius: 24px`
- **Active tab**: `background: rgba(5, 150, 222, 0.3); color: #5BC0F0`
- **Inactive tab**: `transparent; color: rgba(255,255,255,0.6)`
- **Priority dot colors**: P1 = `#EF4444` (red), P2 = `#F59E0B` (amber), P3 = `#0596DE` (blue)

**Structure**: `[● P1] [← Home] [A] [B] [C] [D] [E]`

**HTML Template** — insert before `</body>`:
```html
<div style="
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: #1B2A4A;
  border-radius: 24px;
  padding: 12px 24px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  display: flex;
  gap: 16px;
  align-items: center;
  z-index: 9999;
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  font-weight: 500;
">
  <!-- Priority indicator -->
  <div style="display: flex; align-items: center; gap: 6px; color: rgba(255,255,255,0.6);">
    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #EF4444;"></span>
    P1
  </div>

  <!-- Home link -->
  <a href="index.html" style="
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 6px;
    transition: background 0.2s;
  " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">
    ← Home
  </a>

  <!-- Option tabs -->
  <div style="display: flex; gap: 8px;">
    <a href="proto-p1a-recommender.html" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: #5BC0F0;
      background: rgba(5, 150, 222, 0.3);
    ">A</a>
    <a href="proto-p1b-directory.html" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: rgba(255,255,255,0.6);
      transition: background 0.2s;
    " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">B</a>
    <a href="proto-p1c-network.html" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: rgba(255,255,255,0.6);
      transition: background 0.2s;
    " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">C</a>
  </div>
</div>
```

**Customize for each prototype:**
- Change `href` values to match your actual file names
- Update the priority label (P1/P2/P3) and dot color
- Set the correct active option's background and text color
- Show only the options that exist (A through E as needed)

**Why floating nav at the bottom?**
- Doesn't conflict with the Doctolib header bar at the top
- Quick switching between options without page reload
- Allows stakeholders to compare workflows side-by-side
- Matches the Doctolib product aesthetic (navy, rounded)

### Step 6: Create Landing Page

Build a landing page (`index.html`) inside the run folder that:

1. **Introduces the opportunity** being addressed
2. **Explains each solution option** (2-3 sentences per option)
3. **Provides links to each prototype** with visual preview
4. **Allows easy navigation** between landing page and prototypes

All links in the landing page must use relative paths (just filenames) since the page lives in the same folder as the prototypes.

**Structure**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Agent 5 Prototypes — Solution Options</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 20px;
      background: #f9f9f9;
    }
    h1 {
      color: #0066cc;
      font-size: 32px;
      margin-bottom: 10px;
    }
    .intro {
      font-size: 16px;
      color: #666;
      margin-bottom: 40px;
      max-width: 600px;
    }
    .priority-section {
      margin-bottom: 60px;
    }
    .priority-title {
      font-size: 24px;
      color: #333;
      margin-bottom: 20px;
    }
    .options-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }
    .option-card {
      background: white;
      border-radius: 8px;
      padding: 20px;
      border: 1px solid #e0e0e0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      transition: all 0.3s;
    }
    .option-card:hover {
      box-shadow: 0 8px 16px rgba(0,0,0,0.1);
      transform: translateY(-2px);
    }
    .option-name {
      font-size: 18px;
      font-weight: 600;
      color: #0066cc;
      margin-bottom: 10px;
    }
    .option-desc {
      font-size: 14px;
      color: #666;
      line-height: 1.5;
      margin-bottom: 20px;
    }
    .option-link {
      display: inline-block;
      background: #0066cc;
      color: white;
      padding: 10px 20px;
      border-radius: 4px;
      text-decoration: none;
      font-weight: 500;
      transition: background 0.2s;
    }
    .option-link:hover {
      background: #004fa3;
    }
  </style>
</head>
<body>

  <h1>Agent 5 — Prototypes</h1>

  <p class="intro">
    Below are interactive prototypes for each solution option. Click "View Prototype" to explore each workflow.
    Once inside a prototype, use the floating nav bar at the top to switch between options and compare.
  </p>

  <!-- PRIORITY 1 -->
  <div class="priority-section">
    <h2 class="priority-title">Priority 1: [Opportunity Title]</h2>
    <p>[Brief description of the opportunity]</p>

    <div class="options-grid">
      <div class="option-card">
        <div class="option-name">Option A: [Name]</div>
        <div class="option-desc">[2-3 sentence description of the solution approach]</div>
        <a href="proto-p1a-[name].html" class="option-link">View Prototype →</a>
      </div>
      <!-- Repeat for Options B, C, D, E -->
    </div>
  </div>

  <!-- PRIORITY 2 (if applicable) -->
  <div class="priority-section">
    <h2 class="priority-title">Priority 2: [Opportunity Title]</h2>
    <!-- Repeat options grid for Priority 2 -->
  </div>

</body>
</html>
```

### Step 7: Each Option Must Have Unique Content

Each option (A, B, C, D, E) within a priority MUST have a completely different content area. The whole point of building multiple prototypes is to let users compare genuinely different design approaches.

**What "different" means**:
- Different UI patterns (modal vs. inline vs. wizard vs. drawer vs. dashboard)
- Different layouts, components, and interaction flows
- Different information hierarchy and visual organization
- A user should be able to identify which option they're viewing without looking at the nav bar

**Common failure to avoid**: Generating the Chrome Shell and nav bar correctly, but reusing the same content area across all options with only the title changed. This makes the prototypes useless for testing. Design each option's content area from scratch based on its unique solution approach.

### Step 8: File Naming Convention

Use consistent, descriptive file names:

```
proto-p[1-3][a-e]-[description].html
```

Examples:
- `proto-p1a-recommender.html` (Priority 1, Option A)
- `proto-p1b-directory.html` (Priority 1, Option B)
- `proto-p1c-network.html` (Priority 1, Option C)
- `proto-p2a-inline-chat.html` (Priority 2, Option A)
- `proto-p2b-separate-app.html` (Priority 2, Option B)

**Landing page**: `index.html`

### Step 9: Build Prototypes with Real Doctolib UI

For each prototype, include:

1. **Correct Doctolib Chrome**
   - Sidebar with active nav item
   - Header with logo, search, user menu
   - Oxygen Design System colors

2. **Standard TLE Hero Banner** (if applicable)
   ```html
   <div class="hero-banner" style="background: linear-gradient(135deg, #0066cc 0%, #004fa3 100%); color: white; padding: 40px 20px; margin-bottom: 30px;">
     <h1 style="font-size: 28px; margin: 0; font-weight: 600;">Specialist Referral — Option A</h1>
     <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Intelligent recommendations help you find the right specialist in seconds.</p>
   </div>
   ```

3. **Primary Workflow** — The core interaction the user does
   - For Recommender: Show form, trigger recommendation, display 3-5 suggestions
   - For Directory: Show search, filters, results, selection flow
   - For Network: Show EHR data lookup, availability, integration with system

4. **Interactive Elements**
   - Clickable buttons (use real Doctolib button styles)
   - Form inputs (text, dropdowns, checkboxes)
   - State changes (before/after clicking, loading states, success/error messages)
   - Hover effects (buttons, cards, links)

5. **Mobile Responsiveness**
   - Test at 375px (mobile), 768px (tablet), 1920px (desktop)
   - Sidebar should collapse on mobile
   - Content should reflow smoothly

---

## Phase 3: Quality Assurance

### Step 10: Ruthless Visual QA Against Baseline

After building all prototypes, run the **ruthless-qa** skill process to verify that each prototype has not diverged from the baseline in any unintended way. This is not optional.

**Process**:

1. **Take a screenshot of the baseline prototype** (e.g., `tle-flow.html`) at each key state (default view, after clicking through each step). These screenshots become your reference images.

2. **For each prototype**, run the full ruthless QA process:
   - Spawn 5 parallel auditor sub-agents (Chrome & Navigation, Layout & Spacing, Typography & Content, Colors & Visual Style, Interactive & Detail)
   - Each auditor compares the prototype against the baseline screenshots
   - Each auditor's job is to find discrepancies that are NOT related to the solution option's intended changes
   - Minimum 3 rounds per prototype

3. **Auditor focus**: Auditors should be told which area of the UI is the "solution zone" (the part that SHOULD differ). Everything OUTSIDE that zone must be pixel-identical to the baseline. Discrepancies inside the solution zone are expected. Discrepancies outside the solution zone are bugs.

4. **Auditor prompt addition** — add this to every auditor prompt:
   ```
   IMPORTANT: This prototype intentionally differs from the baseline in ONE specific area:
   [describe the solution zone, e.g., "the chat input area at the bottom of the conversation panel"].

   Differences INSIDE that zone are expected — ignore them.
   Differences OUTSIDE that zone are BUGS — report them all.

   Focus your scrutiny on everything OUTSIDE the solution zone. The sidebar, header,
   sub-sidebar, specialist grid, form fields, patient/insurance panels, navigation
   behavior, CSS variables, fonts, colors, spacing — ALL must be identical to the baseline.
   ```

5. **Fix all unintended divergences** before proceeding. After fixing, run another round to verify.

6. **Completion criteria**: Stop when auditors find < 2 new unintended divergences (outside the solution zone) in a round, with a minimum of 3 rounds.

### Step 11: Link and Path Verification

Because prototypes live in a subfolder of the shared repo (not at the root), all internal links must be verified before pushing. Broken links are the most common issue with this folder structure.

**Automated check** — run this script from inside the run folder:

```python
import os
import re

folder = os.getcwd()
html_files = [f for f in os.listdir(folder) if f.endswith('.html')]
errors = []

for filename in html_files:
    with open(os.path.join(folder, filename), 'r') as f:
        content = f.read()

    # Find all href values pointing to .html files
    hrefs = re.findall(r'href=["\']([^"\']*\.html)["\']', content)

    for href in hrefs:
        # Links should be relative (just filename) — no leading slash, no folder path
        if '/' in href:
            errors.append(f"  {filename}: non-relative link found: {href}")
        elif href not in html_files:
            errors.append(f"  {filename}: broken link to: {href} (file does not exist)")

if errors:
    print("LINK ERRORS FOUND:")
    for e in errors:
        print(e)
else:
    print(f"All links verified across {len(html_files)} HTML files.")
```

**What this catches:**
- Links using absolute paths (e.g., `/proto-p1a.html`) that would break on GitHub Pages
- Links to files that don't exist in the folder
- Links using folder-relative paths (e.g., `prototypes/proto-p1a.html`) left over from old patterns

**Manual check:**
- Open `index.html` in Chrome and click every "View Prototype" link
- Inside each prototype, click every nav bar button — verify it loads the correct option
- Verify the "Home" nav button returns to `index.html`

Fix all link errors before proceeding to Phase 4.

---

## Phase 4: Publish

### Step 12: Push to the Shared Prototype Repository

All prototype runs are pushed as folders to a single shared repo: `https://github.com/calvin-docto-ai/ai-pm-prototypes`. This keeps all runs organized in one place and avoids creating a new repo per run.

**Workflow:**

#### 12a. Clone the shared repo

```bash
# Clone the shared prototype repo
git clone https://github.com/calvin-docto-ai/ai-pm-prototypes.git /sessions/elegant-sleepy-dijkstra/ai-pm-prototypes
cd /sessions/elegant-sleepy-dijkstra/ai-pm-prototypes
```

#### 12b. Copy the run folder into the shared repo

```bash
# Copy the entire run folder (with all prototypes) into the shared repo
cp -r /sessions/elegant-sleepy-dijkstra/prototype-build/$FOLDER_NAME .
```

#### 12c. Commit and push

```bash
git add "$FOLDER_NAME"
git commit -m "Add prototypes: $FOLDER_NAME"
git push origin main
```

#### 12d. Verify GitHub Pages deployment

GitHub Pages should already be enabled on the `ai-pm-prototypes` repo. Verify the new prototypes are accessible:

```bash
# Wait briefly for deployment
sleep 30

# Check that the landing page is accessible
curl -s -o /dev/null -w "%{http_code}" "https://calvin-docto-ai.github.io/ai-pm-prototypes/$FOLDER_NAME/index.html"
```

**Live URLs** will be:
```
https://calvin-docto-ai.github.io/ai-pm-prototypes/<FOLDER_NAME>/index.html
https://calvin-docto-ai.github.io/ai-pm-prototypes/<FOLDER_NAME>/proto-p1a-[name].html
```

If GitHub Pages is not yet enabled on the repo, enable it:
```bash
gh api -X POST repos/calvin-docto-ai/ai-pm-prototypes/pages \
  --field source='{"branch":"main","path":"/"}' \
  --silent
```

#### 12e. Update Confluence with Live Prototype URLs

After confirming the GitHub Pages site is live:

1. **Update the Agent 6 — Prototypes child page** on Confluence with the live URL:
   ```markdown
   ## Interactive Prototypes

   All prototypes are live and accessible at:
   **[View All Prototypes →](https://calvin-docto-ai.github.io/ai-pm-prototypes/<FOLDER_NAME>/index.html)**

   Individual prototypes:
   - [Option A — Description](https://calvin-docto-ai.github.io/ai-pm-prototypes/<FOLDER_NAME>/proto-p1a-name.html)
   - [Option B — Description](https://calvin-docto-ai.github.io/ai-pm-prototypes/<FOLDER_NAME>/proto-p1b-name.html)
   - ...
   ```

2. **Update the run parent page summary** to include the prototype link in the Agent Output Index table and in the run summary section.

Use `updateConfluencePage` MCP tool for both updates:
```
cloudId: "doctolib.atlassian.net"
pageId: "<agent-6-page-id>"
body: "<updated markdown with live URLs>"
contentFormat: "markdown"
```

---

## Output Structure

After completion, the shared repo will contain:

```
ai-pm-prototypes/
  2026-03-22-3-ai-pm-agent-run-tle/
    index.html                          (Landing page)
    proto-p1a-recommender.html          (Priority 1, Option A)
    proto-p1b-directory.html            (Priority 1, Option B)
    proto-p1c-network.html              (Priority 1, Option C)
    proto-p1d-automation.html           (Priority 1, Option D) [if applicable]
    proto-p2a-inline-chat.html          (Priority 2, Option A) [if applicable]
    ...
  2026-04-15-1-ai-pm-agent-run-connect/
    index.html
    ...
```

---

## Key Principles

### 1. Prototypes Feel Real, Not Like Mockups

Users should feel like they're using a Doctolib product, not clicking through Figma.

**What this means**:
- Use real Doctolib terminology (TLE, Connect, Discussions)
- Apply Oxygen Design System colors/spacing consistently
- Include realistic data (not lorem ipsum; use doctor names, real patient scenarios)
- Add micro-interactions (button hover states, loading spinners, success messages)
- Mobile responsiveness from day one

### 2. Each Option Is Fully Explorable

Users can click through the entire workflow, not just see a static mockup.

**Example for Specialist Referral**:
- User clicks "Refer to Specialist"
- Form appears or recommendations show
- User makes selections
- Confirmation message appears
- Next step in workflow is clear

### 3. Floating Nav Enables Side-by-Side Comparison

The nav bar is always accessible, allowing quick switching between options without reloading the page (ideally using local state or frontend routing).

### 4. Navigation Context Matches Opportunity

If the opportunity is about TLE routing, "TLE" should be the active sidebar item. If it's about Messaging, "Discussions" or "Messaging" should be active.

### 5. All Content in English

All labels, help text, buttons, error messages are in English. Use Doctolib's standard terminology.

### 6. All Links Are Relative

Because prototypes live in a subfolder of the shared repo, every `href` to another prototype must be a bare filename (e.g., `proto-p1a-recommender.html`), never an absolute path or a path with folder prefixes. This ensures links work both when opened locally and when served via GitHub Pages.

---

## Quality Checklist

Before pushing to the shared repo, verify:

**Baseline Fidelity (ruthless QA)**:
- [ ] Every prototype started as an exact copy of the baseline HTML file
- [ ] Ruthless QA (minimum 3 rounds, 5 auditors) completed for each prototype
- [ ] Zero unintended divergences outside the solution zone remain
- [ ] Sidebar navigation items are verbatim identical to baseline (never changed)
- [ ] Header, sub-sidebar, CSS custom properties identical to baseline
- [ ] All JavaScript utilities not related to the solution are untouched
- [ ] Each prototype's ONLY visual difference from the baseline is the intended solution change

**Links and Paths**:
- [ ] Link verification script passes with zero errors
- [ ] All nav bar links use relative paths (bare filenames only)
- [ ] All landing page links use relative paths
- [ ] Manually clicked through every link in every prototype
- [ ] "Home" button in nav bar returns to index.html

**Content & Interaction**:
- [ ] Landing page exists and links to all prototypes
- [ ] Each prototype has a floating nav bar with all options
- [ ] Floating nav shows correct active state
- [ ] Active sidebar item matches the opportunity context
- [ ] At least one complete user workflow is clickable/interactive
- [ ] Each option (A/B/C/D/E) has visually distinct content in the solution zone
- [ ] All CTA buttons use Doctolib blue (#0596DE), never green

**Polish**:
- [ ] All text is in English and uses Doctolib terminology
- [ ] No lorem ipsum; use realistic data (real names, real scenarios)
- [ ] No console errors (test in Chrome DevTools)
- [ ] File names follow pattern: `proto-p[1-3][a-e]-[description].html`

**Publishing**:
- [ ] Run folder pushed to `calvin-docto-ai/ai-pm-prototypes` repo
- [ ] GitHub Pages URLs verified and accessible
- [ ] Confluence updated with live prototype links
