---
name: doctolib-prototyper
description: "Create interactive HTML prototypes using the Doctolib product shell as a baseline. This skill produces self-contained HTML files viewable in Chrome that match the real Doctolib practitioner UI — complete with navy sidebar, header bar, sub-sidebar navigation, and Oxygen Design System tokens. Use whenever asked to 'create a prototype', 'mock up a solution', 'build a UI demo', 'prototype an option', or when multiple solution options need to be visualized as clickable HTML. Also trigger when the user references the 'Chrome shell', 'Doctolib shell', or wants to create A/B/C/D/E option variants for user testing. Pairs with the ai-pm-pipeline skill (Agent 6 — Prototype Builder)."
---

# Doctolib Prototyper Skill

Create interactive HTML prototypes that look like the real Doctolib product using a reusable Chrome Shell baseline. Every prototype copies the full shell and only modifies the content area.

## Overview

This skill produces self-contained, production-ready HTML files that are indistinguishable from the real Doctolib product interface. Each prototype:

- Starts with a complete "Chrome Shell" — the full Doctolib layout (sidebar, header, sub-sidebar)
- Swaps out only the content area to show different design options
- Runs directly in Chrome with no build steps or dependencies
- Uses English text and Doctolib's Oxygen Design System tokens
- Includes a floating navigation bar for switching between options and returning to the landing page

This allows rapid prototyping of multiple solution variants (Options A, B, C, D, E) in a single priority level, each visually identical to the product except for the feature being tested.

## The Chrome Shell

### Source of Truth

The baseline Chrome Shell lives in the scaffolding repo: **`https://github.com/calvin-docto-ai/OS-prototype-scaffolding`**

Always clone this repo to get the most up-to-date baseline files. Do NOT rely on a local `doctolib-chrome-shell.html` — the scaffolding repo is the single source of truth.

The repo contains multiple baseline pages for different product areas:
- `tle-flow.html` — TLE specialist search (most common starting point)
- `tle-flow-request.html` — TLE request flow
- `tle-flow-complete.html` — TLE completion flow
- `discussions.html` — Discussions view
- `agenda.html` — Agenda/calendar view

Pick the baseline that most closely matches the product area you're prototyping, then modify only the content area.

### Structure

Each baseline file contains:

```
┌─────────────────────────────────────────────────┐
│ Dark Navy Header (52px)                          │
├──────┬───────────────────────────────────────────┤
│      │                                            │
│      │ Sub-sidebar (230px) | Content Area        │
│ Icon │ Connect Section      |                    │
│ Rail │ - Discussions        | ← Swap this only  │
│(76px)│ - Tele-expertise     |                    │
│      │ - Networks           |                    │
│      │                      |                    │
└──────┴───────────────────────────────────────────┘
```

### Key Components

- **Main sidebar**: 76px dark navy (#1B2A4A) with icons and badges. Contains Agenda, Patient Flow, Tasks, Connect, Patient Messaging, Patient Management, E-mails, Document Import, Billing, Activity.
- **Header bar**: 52px dark navy with Doctolib logo, search bar, chips, notification icons, and user avatar.
- **Sub-sidebar**: 230px white panel showing Connect section with links to Discussions, Tele-expertise, Networks.
- **Content area**: Everything after the sub-sidebar. This is the ONLY section you modify.

### Design Tokens

Use these exact tokens — do not approximate:

| Token | Value | Usage |
|-------|-------|-------|
| `--dtl-navy` | #1B2A4A | Sidebar & header background |
| `--dtl-blue` | #0596DE | Primary actions, active states, links |
| `--dtl-gray-50` | #F7F8FA | Page background |
| `--dtl-gray-600` | #4B5563 | Body text |
| `--dtl-gray-800` | #1F2937 | Headings |

Full token reference is in the `doctolib-design-system` skill.

### CSS Classes Available in the Shell

The shell includes pre-built component styles:

- `.hero-banner` — White card with subtle shadow, rounded corners, for search/intro sections
- `.specialist-card` — Square card with avatar, name, specialty, location
- `.specialist-grid` — Grid layout for cards (responsive)
- `.search-bar` — Dual-field search with button
- `.category-label` — Uppercase label for card sections
- `.see-more-btn` — Centered pill button
- `.feedback-widget` — Float-right feedback stars
- `.content-section-label` — Bold dark navy label above hero

Reuse these wherever possible. For custom components, add a scoped `<style>` block — do NOT modify the shell's base CSS.

## Creating a Prototype

### Step-by-step Workflow

1. **Clone the scaffolding repo** and pick the right baseline:

   ```bash
   git clone https://github.com/calvin-docto-ai/OS-prototype-scaffolding.git
   ```

   Choose the baseline file that best matches your product area (e.g., `tle-flow.html` for TLE prototypes). Read its full contents as your starting point.

2. **Create a new file** with a descriptive name:
   - Format: `proto-p[priority][option]-[short-name].html`
   - Examples: `proto-p1a-confirm-modal.html`, `proto-p2b-search-filter.html`, `proto-p3e-sidebar-update.html`
   - DO NOT overwrite the shell. Always create a copy.

3. **Update the title tag** to reflect the prototype name:
   ```html
   <title>Doctolib — TLE: Confirm Modal (P1A)</title>
   ```

4. **Update the sub-sidebar active item** to point to the new file:
   - Find the link that should be active (e.g., Tele-expertise for a TLE prototype)
   - Change its `href` to point to the new file: `href="proto-p1a-confirm-modal.html"`
   - Add or keep the `active` class on that link

5. **Replace the content area**:
   - Find the comment: `<!-- ══ SAMPLE CONTENT ══ -->` (in scaffolding baselines)
   - Delete everything between that line and `<!-- ══ END SAMPLE CONTENT ══ -->`
   - Insert your new prototype content in that slot
   - If no markers exist, identify the main content section (after the sub-sidebar) and replace only that content

6. **Keep the component label**:
   - The `<div class="content-section-label">Tele-expertise</div>` (or appropriate section) should remain
   - Update it only if your prototype belongs to a different section

7. **Add the floating navigation bar** (see section below)

8. **Test in Chrome**: Open the file directly. No build step needed.

### Example: Replacing Content

Before (from the shell):
```html
<!-- ══ SAMPLE CONTENT ══ -->
<div class="content-section-label">Tele-expertise</div>
<div class="hero-banner">
  <h2>Find a specialist</h2>
  <!-- ... -->
</div>
<!-- ══ END SAMPLE CONTENT ══ -->
```

After (your prototype):
```html
<!-- ══ SAMPLE CONTENT ══ -->
<div class="content-section-label">Tele-expertise</div>
<div class="hero-banner">
  <h2>Confirm Your Appointment</h2>
  <p>You are about to schedule a tele-expertise session with Dr. Marie Dupont.</p>
  <button style="background: var(--dtl-blue); color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer;">Confirm</button>
</div>
<!-- ══ END SAMPLE CONTENT ══ -->
```

## Floating Navigation Bar

Every prototype MUST include a floating navigation bar fixed to the bottom center of the viewport. This allows users to:

- Return to the landing page ("Home" link)
- Switch between option variants (A/B/C/D/E tabs)
- See which priority level and option is active

### Structure

```
[Home] | [P1] | [A] [B] [C] [D] [E]
```

### Visual Design

- **Background**: #1B2A4A (dark navy) with rounded corners and shadow
- **Padding**: 12px 24px
- **Border radius**: 24px
- **Box shadow**: 0 4px 12px rgba(0,0,0,0.15)
- **z-index**: 9999
- **Position**: `position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);`

### Active and Inactive States

| State | Background | Text Color |
|-------|------------|-----------|
| **Inactive tab** | Transparent | rgba(255,255,255,0.6) |
| **Active tab** | rgba(5, 150, 222, 0.3) | #5BC0F0 |
| **Home icon** | Transparent | White |
| **Priority dot** | Varies (see below) | — |

### Priority Dot Colors

- **P1**: #EF4444 (red)
- **P2**: #F59E0B (amber)
- **P3**: #0596DE (blue)

### HTML Template

Insert this before the closing `</body>` tag:

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
    🏠 Home
  </a>

  <div style="width: 1px; height: 20px; background: rgba(255,255,255,0.2);"></div>

  <!-- Priority -->
  <div style="display: flex; align-items: center; gap: 6px; color: rgba(255,255,255,0.6);">
    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #EF4444;"></span>
    P1
  </div>

  <!-- Option tabs -->
  <div style="display: flex; gap: 8px;">
    <a href="proto-p1a-option-name.html" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: #5BC0F0;
      background: rgba(5, 150, 222, 0.3);
    ">A</a>
    <a href="proto-p1b-option-name.html" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: rgba(255,255,255,0.6);
      transition: background 0.2s;
    " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">B</a>
    <a href="proto-p1c-option-name.html" style="
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
- Change `href` values to match your file names
- Update the priority (P1/P2/P3) and color
- Show only the options that exist (A, B, C, D, E as needed)
- Set the correct active option's background and text color

## Landing Page (Agent 5 Prototypes Hub)

Create a landing page (`agent5-prototypes.html`) that displays all prototypes grouped by priority. This is where the "Home" link points.

### Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Doctolib — Prototypes Hub</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap');

    :root {
      --dtl-navy: #1B2A4A;
      --dtl-blue: #0596DE;
      --dtl-gray-50: #F7F8FA;
      --dtl-gray-200: #E4E7EB;
      --dtl-gray-600: #4B5563;
      --dtl-gray-800: #1F2937;
    }

    body {
      margin: 0;
      padding: 24px;
      background: var(--dtl-gray-50);
      font-family: 'Open Sans', sans-serif;
      color: var(--dtl-gray-600);
    }

    .header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 32px;
    }

    .badge {
      background: var(--dtl-blue);
      color: white;
      padding: 4px 12px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
    }

    h1 {
      margin: 0;
      font-size: 28px;
      color: var(--dtl-gray-800);
    }

    .summary-table {
      background: white;
      border: 1px solid var(--dtl-gray-200);
      border-radius: 8px;
      margin-bottom: 40px;
      overflow: hidden;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }

    th {
      background: var(--dtl-gray-50);
      padding: 12px 16px;
      text-align: left;
      font-weight: 600;
      color: var(--dtl-gray-800);
      border-bottom: 1px solid var(--dtl-gray-200);
    }

    td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--dtl-gray-200);
    }

    tr:last-child td {
      border-bottom: none;
    }

    .priority {
      font-weight: 600;
    }

    .priority-1 { color: #EF4444; }
    .priority-2 { color: #F59E0B; }
    .priority-3 { color: #0596DE; }

    .option-badges {
      display: flex;
      gap: 6px;
    }

    .option-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      background: var(--dtl-blue);
      color: white;
      border-radius: 4px;
      font-weight: 600;
      font-size: 12px;
      text-decoration: none;
      transition: all 0.2s;
    }

    .option-badge:hover {
      background: #0080C5;
    }

    .sections {
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .priority-section {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .section-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--dtl-gray-800);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }

    .option-card {
      background: white;
      border: 1px solid var(--dtl-gray-200);
      border-radius: 8px;
      padding: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s;
    }

    .option-card:hover {
      border-color: var(--dtl-blue);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .option-card-content {
      flex: 1;
    }

    .option-card-title {
      font-weight: 600;
      color: var(--dtl-gray-800);
      margin-bottom: 4px;
    }

    .option-card-desc {
      font-size: 13px;
      color: var(--dtl-gray-600);
    }

    .option-card-link {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      background: var(--dtl-blue);
      color: white;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 600;
      transition: background 0.2s;
    }

    .option-card-link:hover {
      background: #0080C5;
    }

    .baseline-link {
      margin-top: 40px;
      padding: 24px;
      background: white;
      border: 1px dashed var(--dtl-gray-200);
      border-radius: 8px;
      text-align: center;
    }

    .baseline-link a {
      color: var(--dtl-blue);
      text-decoration: none;
      font-weight: 600;
    }

    .baseline-link a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="header">
    <span class="badge">Agent 5</span>
    <h1>Prototype Hub — Doctolib Prototypes</h1>
  </div>

  <!-- Summary Table -->
  <div class="summary-table">
    <table>
      <thead>
        <tr>
          <th>Priority</th>
          <th>Problem</th>
          <th>Impact</th>
          <th>Options</th>
          <th>Docs</th>
        </tr>
      </thead>
      <tbody>
        <!-- Add rows here. Example: -->
        <tr>
          <td class="priority priority-1">P1</td>
          <td>Confirmation flow unclear</td>
          <td>Users confused about next steps</td>
          <td>
            <div class="option-badges">
              <a class="option-badge" href="proto-p1a-confirm-modal.html" title="Option A">A</a>
              <a class="option-badge" href="proto-p1b-confirm-flow.html" title="Option B">B</a>
            </div>
          </td>
          <td><a href="#" style="color: var(--dtl-blue); text-decoration: none;">PRD</a></td>
        </tr>
        <!-- Add more rows... -->
      </tbody>
    </table>
  </div>

  <!-- Grouped Option Cards by Priority -->
  <div class="sections">
    <!-- P1 Section -->
    <div class="priority-section">
      <div class="section-title">
        <span class="dot" style="background: #EF4444;"></span>
        Priority 1 — High Impact
      </div>
      <div class="option-card">
        <div class="option-card-content">
          <div class="option-card-title">Option A — Confirm Modal</div>
          <div class="option-card-desc">Standard modal confirmation pattern</div>
        </div>
        <a class="option-card-link" href="proto-p1a-confirm-modal.html">View</a>
      </div>
      <div class="option-card">
        <div class="option-card-content">
          <div class="option-card-title">Option B — Inline Confirmation</div>
          <div class="option-card-desc">Confirmation UI embedded in page flow</div>
        </div>
        <a class="option-card-link" href="proto-p1b-confirm-flow.html">View</a>
      </div>
    </div>

    <!-- P2 Section (if needed) -->
    <!-- <div class="priority-section">
      <div class="section-title">
        <span class="dot" style="background: #F59E0B;"></span>
        Priority 2 — Medium Impact
      </div>
      Add more option cards...
    </div> -->
  </div>

  <!-- Baseline Shell Link -->
  <div class="baseline-link">
    <p style="margin: 0; color: var(--dtl-gray-600); font-size: 13px; margin-bottom: 8px;">Reference</p>
    <a href="https://github.com/calvin-docto-ai/OS-prototype-scaffolding">View Doctolib Chrome Shell (Scaffolding Repo)</a>
  </div>
</body>
</html>
```

Update this with your actual prototype names, priorities, problems, and links.

## Naming Convention

Follow this pattern for all files:

| Type | Format | Example |
|------|--------|---------|
| **Prototype** | `proto-p[priority][option]-[short-name].html` | `proto-p1a-confirm-modal.html` |
| **Landing page** | `index.html` | — |
| **Shell baseline** | Cloned from `OS-prototype-scaffolding` repo | `tle-flow.html`, `agenda.html`, etc. |

- `p1`, `p2`, `p3` = priority level
- `a`, `b`, `c`, `d`, `e` = option variant (uppercase in nav bar, lowercase in filename)
- Short name = hyphen-separated, lowercase, descriptive
- Never modify the scaffolding baseline files directly — always copy them first

## Batch Injection Pattern

When creating many prototypes (5+ options across multiple priorities), use a Python script to inject the floating nav bar into all files at once. This is faster and more reliable than editing each file manually.

### Batch Script Template

```python
#!/usr/bin/env python3
import os
import re

# Define all prototypes and their metadata
PROTOTYPES = [
    {
        "file": "proto-p1a-confirm-modal.html",
        "priority": "P1",
        "priority_color": "#EF4444",
        "option": "A",
        "active": True,
        "siblings": ["proto-p1b-confirm-flow.html", "proto-p1c-confirm-drawer.html"]
    },
    {
        "file": "proto-p1b-confirm-flow.html",
        "priority": "P1",
        "priority_color": "#EF4444",
        "option": "B",
        "active": False,
        "siblings": ["proto-p1a-confirm-modal.html", "proto-p1c-confirm-drawer.html"]
    },
    # ... more prototypes
]

def generate_nav_bar(priority, priority_color, option, siblings):
    """Generate the floating nav bar HTML."""
    sibling_buttons = ""
    for i, (sibling, label) in enumerate(zip(siblings, "ABCDE")):
        is_active = (label == option)
        bg = "rgba(5, 150, 222, 0.3)" if is_active else "transparent"
        color = "#5BC0F0" if is_active else "rgba(255,255,255,0.6)"
        sibling_buttons += f"""    <a href="{sibling}" style="
      padding: 6px 12px;
      border-radius: 6px;
      text-decoration: none;
      color: {color};
      background: {bg};
      transition: all 0.2s;
    " onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='{bg}'">{label}</a>\n"""

    nav_html = f"""<div style="
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
    🏠 Home
  </a>

  <div style="width: 1px; height: 20px; background: rgba(255,255,255,0.2);"></div>

  <div style="display: flex; align-items: center; gap: 6px; color: rgba(255,255,255,0.6);">
    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: {priority_color};"></span>
    {priority}
  </div>

  <div style="display: flex; gap: 8px;">
{sibling_buttons}  </div>
</div>
"""
    return nav_html

def remove_existing_nav(content):
    """Remove any existing nav bar (idempotent)."""
    pattern = r'<div style="\s*position: fixed;\s*bottom: 20px;.*?</div>\s*</body>'
    return re.sub(pattern, '</body>', content, flags=re.DOTALL)

def inject_nav_bar(filepath, nav_html):
    """Inject nav bar into a prototype file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing nav (idempotent)
    content = remove_existing_nav(content)

    # Insert new nav before </body>
    content = content.replace('</body>', nav_html + '</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    for proto in PROTOTYPES:
        filepath = proto["file"]
        if os.path.exists(filepath):
            nav = generate_nav_bar(
                proto["priority"],
                proto["priority_color"],
                proto["option"],
                proto["siblings"]
            )
            inject_nav_bar(filepath, nav)
            print(f"✓ Injected nav into {filepath}")
        else:
            print(f"✗ File not found: {filepath}")

if __name__ == "__main__":
    main()
```

**Usage**:
1. Create the script in your prototype directory
2. Define all prototypes in the `PROTOTYPES` list with filenames and metadata
3. Run: `python3 batch_inject_nav.py`
4. The script is idempotent — run it multiple times safely if prototypes are added

Benefits:
- Single source of truth for cross-links
- Prevents manual typos in href values
- Highlights sibling relationships
- Easy to maintain as you add more options

## CRITICAL: Each Option Must Have Unique Content

When creating multiple options (A, B, C, D, E) for a priority level, each option MUST have visually distinct content in the main content area. The whole point of options is to let users compare different design approaches. If all options look the same except for the nav bar highlighting, the prototypes are useless for testing.

What "visually distinct" means in practice:
- Different UI patterns (e.g., Option A uses a modal, Option B uses inline expansion, Option C uses a wizard)
- Different layouts, components, or interaction models
- Different information hierarchy or content organization
- The user should be able to tell which option they're looking at without checking the nav bar

A common failure mode: generating the shell + nav bar correctly but copy-pasting the same content area into every option. This defeats the purpose entirely. When building prototypes, design each option's content area independently based on what that solution approach would actually look like.

## Hosting Prototypes on GitHub Pages

All prototypes are published to a single shared repo: **`https://github.com/calvin-docto-ai/ai-pm-prototypes`**

Each pipeline run gets its own subfolder inside this repo, named after the Confluence run page title (sanitized to be URL-friendly: lowercase, hyphens, no special characters).

### Publishing Workflow

After building all prototypes locally:

```bash
# 1. Clone the shared prototype repo
git clone https://github.com/calvin-docto-ai/ai-pm-prototypes.git

# 2. Create a run folder (sanitized from Confluence page title)
cd ai-pm-prototypes
mkdir -p 2026-03-22-3-ai-pm-agent-run-tle

# 3. Copy all prototype HTML files into the run folder
cp /path/to/prototypes/*.html 2026-03-22-3-ai-pm-agent-run-tle/

# 4. Stage, commit, push
git add 2026-03-22-3-ai-pm-agent-run-tle/
git commit -m "Add prototypes: 2026-03-22-3-ai-pm-agent-run-tle"
git push origin main
```

After pushing, prototypes will be live at:
```
https://calvin-docto-ai.github.io/ai-pm-prototypes/2026-03-22-3-ai-pm-agent-run-tle/index.html
https://calvin-docto-ai.github.io/ai-pm-prototypes/2026-03-22-3-ai-pm-agent-run-tle/proto-p1a-confirm-modal.html
```

GitHub Pages deploys typically take 1-2 minutes. Verify by visiting the landing page URL.

**Important — relative paths**: Because prototypes live in a subfolder, all links between prototypes (nav bar, landing page) must use relative paths (bare filenames like `proto-p1a-name.html`, not absolute paths). This ensures links work both locally and on GitHub Pages.

### Linking from Confluence

When publishing pipeline results to Confluence, use the GitHub Pages URL:

```html
<a href="https://calvin-docto-ai.github.io/ai-pm-prototypes/<folder-name>/index.html">View all N interactive prototypes →</a>
```

This ensures stakeholders can click through to prototypes directly from Confluence without needing local file access. The repo must be public for GitHub Pages to serve the files without authentication.

## Quality Checklist

Before delivering a prototype to the user, verify:

- [ ] File is `.html` and opens in Chrome with no build step
- [ ] Full Doctolib chrome is present: sidebar (76px), header (52px), sub-sidebar (230px)
- [ ] Baseline was cloned from `OS-prototype-scaffolding` repo (not an old local copy)
- [ ] Content sits correctly after the sub-sidebar and after `<!-- ══ SAMPLE CONTENT ══ -->`
- [ ] All text is in English (no French)
- [ ] Colors match the design token table (no eyeballed approximations or CSS color names)
- [ ] Cards have 1px solid borders with `--border-color`, not drop shadows alone
- [ ] Hero banners use `.hero-banner` class or inline styles matching the baseline
- [ ] Specialist cards use `.specialist-card` or replicate the structure from the shell
- [ ] Floating nav bar is present and positioned at bottom center
- [ ] Nav bar links point to correct file names (no typos)
- [ ] Floating nav bar has correct priority color (P1=#EF4444, P2=#F59E0B, P3=#0596DE)
- [ ] Active option in nav bar is highlighted with blue background and #5BC0F0 text
- [ ] Title tag follows format: "Doctolib — TLE: [Name] ([ID])"
- [ ] Sub-sidebar active item has `active` class and points to current file
- [ ] All interactive elements (buttons, links, tabs) work when clicked
- [ ] Inactive or dimmed states use opacity (0.5-0.6), not just lighter text color
- [ ] Avatar images use `https://i.pravatar.cc/112?img=XX` (https, not http)
- [ ] No inline `<style>` blocks modify the shell's base CSS classes (`.hero-banner`, `.specialist-card`, etc.)
- [ ] No sidebar or header modifications — only content area changed
- [ ] Content area is not wider than the original shell content
- [ ] Font is Open Sans or system default (not custom fonts requiring network requests)
- [ ] Each option (A/B/C/D/E) has visually distinct content — not just different nav highlighting
- [ ] Prototypes are pushed to GitHub Pages and URLs are verified live

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Prototype looks broken in Chrome | Ensure the full `<head>` and CSS from the shell is included. Check browser console for JS errors. |
| Design tokens not recognized | Verify `:root` CSS variables are copied from the shell. Use `var(--dtl-navy)` syntax. |
| Nav bar not visible | Check z-index is 9999. Ensure `position: fixed` is set. Verify `bottom: 20px` and `left: 50%; transform: translateX(-50%)` for centering. |
| Links to other options are broken | Check `href` values match actual file names. Use lowercase hyphens in filenames. |
| Sidebar or header is modified | Restore from the shell file. Do NOT edit the sidebar/header — only the content area. |
| Colors look different from product | Use the exact hex values from the token table. Do not use CSS color names like `navy` or `lightblue`. |
| Fonts not loading | Ensure Google Fonts import is in `<head>`: `@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap');` |

## Related Skills

- **doctolib-design-system** — Deep reference for design tokens, component patterns, golden rules, and anti-patterns
- **ai-pm-pipeline** (Agent 6 — Prototype Builder) — Orchestrates when to use this skill in the product definition workflow
