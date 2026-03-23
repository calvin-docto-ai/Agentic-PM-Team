---
name: documentation-checker
description: "Verify and fix Confluence documentation structure for AI PM Pipeline runs. Use this skill after EVERY agent completes during a pipeline run, or when Calvin says 'check documentation', 'verify Confluence', 'fix the pages', 'check the pages', or 'run documentation checker'. Also trigger when any pipeline run finishes and you need to confirm all pages exist, are properly nested, and the index table has working links. If an ai-pm-pipeline run just completed and you're about to tell Calvin it's done — run this first. It catches orphaned pages, missing child pages, broken links, and empty content before stakeholders see it."
---

# Documentation Checker

This skill validates and repairs the Confluence page structure for AI PM Pipeline runs. It ensures every run has a properly nested parent page, all 12 agent child pages exist with content, and the run summary's Agent Output Index contains clickable links to each child page.

## When to Run

Run this skill in two modes:

1. **After each agent completes** (inline check): Verify the agent's child page was created under the run parent page. If not, create it. Update the parent page's index table with a link to the child page.

2. **Full audit** (end-of-run or on-demand): Check the entire run's Confluence structure — parent page placement, all 12 child pages, index links, and content presence.

## The Expected Structure

Every pipeline run must produce this exact Confluence hierarchy:

```
AI-Product Management Team (Page ID: 3870819267)          ← FIXED root
└── YYYY-MM-DD-N — AI PM Agent Run ([Product Area])       ← Run parent page
    ├── Agent 1 — Context
    ├── Agent 2 — Opportunities
    ├── Agent 3 — Opportunity Solution Tree
    ├── Agent 3.5 — PRDs
    ├── Agent 4 — Prioritization
    ├── Agent 5 — Solution Design
    ├── Agent 6 — Prototypes
    ├── Agent 7 — Assumptions
    ├── Agent 8 — Test Design
    ├── Agent 9 — Metrics
    ├── Agent 10 — Communications
    ├── Agent 11 — Sprint Plan
    └── Agent 12 — Maze Tests
```

The root parent page `3870819267` is fixed and never changes. All run parent pages are children of it. All agent pages are children of their run parent page.

---

## Mandatory parentId Validation (After Every Page Creation)

**CRITICAL — Run this after EVERY `createConfluencePage` call, with zero exceptions.** This catches the orphaned-page bug where sub-agents pass an incorrect `parentId`, resulting in pages created under the wrong parent (observed in Run 4 on 2026-03-22 with Agents 3, 3.5, and 4).

### Procedure

1. After `createConfluencePage` returns the new page's `id`, **immediately** call `getConfluencePage` on that `id` to read back the page metadata.
2. Check that the page's actual parent matches the **intended** parent:
   - For the run parent page: intended parentId = `"3870819267"`
   - For agent child pages: intended parentId = the run parent page ID
3. **If parentId matches**: Log `"✓ parentId verified: <pageId> is child of <parentId>"` and proceed.
4. **If parentId does NOT match**: Immediately fix it by calling `updateConfluencePage` with the correct `parentId` to move the page. Log `"⚠ FIXED: Page <pageId> was under <wrong_parent>, moved to <correct_parent>"`.
5. **If `getConfluencePage` fails** (page doesn't exist): The create call silently failed. Retry `createConfluencePage` once. If it fails again, log `"✗ FAILED: Could not create or verify page"` and halt.

### Why This Exists

In pipeline Run 4 (2026-03-22), Agents 3, 3.5, and 4 were orphaned because sub-agents received a stale or incorrect parentId. The documentation checker caught this at the end, but by then 3 pages needed manual repair. This validation step catches the problem within seconds of page creation, before subsequent agents compound the error.

### When Sub-Agents Create Pages

When the pipeline spawns sub-agents (e.g., Agent 3.5 spawning per-PRD sub-agents, or Agent 5 spawning per-priority sub-agents), **the parent agent must pass the run parent page ID explicitly as a parameter to each sub-agent**. Sub-agents must NOT attempt to look up or infer the parentId — they must use exactly the ID they were given. After each sub-agent creates its page, it must run the parentId validation procedure above before returning.

---

## Full Audit Procedure

### Step 1: Verify the run parent page exists under the correct parent

Use `getConfluencePageDescendants` on page `3870819267` to list its children. Confirm the run parent page (by title pattern `YYYY-MM-DD-N — AI PM Agent Run (...)`) appears in the list.

**If the run page is missing from children:** Use `updateConfluencePage` to set `parentId: "3870819267"` on the run page, moving it to the correct location.

**If no run page exists at all:** Something went very wrong — flag this and stop.

### Step 2: Check all 12 agent child pages exist under the run parent

Use `getConfluencePageDescendants` on the run parent page to list its children. Compare against the expected list of 12 agent pages:

```
Expected child pages (by title):
1.  "Agent 1 — Context"
2.  "Agent 2 — Opportunities"
3.  "Agent 3 — Opportunity Solution Tree"
4.  "Agent 3.5 — PRDs"
5.  "Agent 4 — Prioritization"
6.  "Agent 5 — Solution Design"
7.  "Agent 6 — Prototypes"
8.  "Agent 7 — Assumptions"
9.  "Agent 8 — Test Design"
10. "Agent 9 — Metrics"
11. "Agent 10 — Communications"
12. "Agent 11 — Sprint Plan"
13. "Agent 12 — Maze Tests"
```

For each missing page:
1. **Search Confluence** using `searchConfluenceUsingCql` with `title = "Agent N — Title"` in the PTA space to see if the page exists somewhere else (orphaned under wrong parent).
2. **If found elsewhere:** Use `updateConfluencePage` to move it by setting `parentId` to the run parent page ID.
3. **If not found anywhere:** Use `createConfluencePage` to create it with content from the local pipeline output file (e.g., `/sessions/.../pipeline-output/agent-01-context.md`). Use these parameters:
   - `cloudId: "doctolib.atlassian.net"`
   - `spaceKey: "PTA"`
   - `parentId: "<run_parent_page_id>"`
   - `contentFormat: "markdown"`
4. **After creating or moving any page:** Run the parentId validation procedure (see above) to confirm the page is now under the correct parent.

### Step 3: Verify each child page has content

For each child page, use `getConfluencePage` and check that the body is not empty (not just whitespace or a single empty paragraph). If a page has no content but the local markdown file exists, update the page with the file's content using `updateConfluencePage`.

### Step 4: Rebuild the Agent Output Index with links

After all child pages are confirmed, rebuild the Agent Output Index table on the run parent page. Each row must link to the actual Confluence page.

The link format in markdown is:
```
[Agent 1 — Context](https://doctolib.atlassian.net/wiki/spaces/PTA/pages/<PAGE_ID>/Agent+1+Context)
```

Build the full index table:
```markdown
| Phase | Agent # | Title |
|-------|---------|-------|
| Discovery | 1 | [Agent 1 — Context](<url>) |
| Discovery | 2 | [Agent 2 — Opportunities](<url>) |
| Discovery | 3 | [Agent 3 — Opportunity Solution Tree](<url>) |
| Discovery | 3.5 | [Agent 3.5 — PRDs](<url>) |
| Discovery | 4 | [Agent 4 — Prioritization](<url>) |
| Design | 5 | [Agent 5 — Solution Design](<url>) |
| Design | 6 | [Agent 6 — Prototypes](<url>) |
| Validation | 7 | [Agent 7 — Assumptions](<url>) |
| Validation | 8 | [Agent 8 — Test Design](<url>) |
| Validation | 9 | [Agent 9 — Metrics](<url>) |
| Communication | 10 | [Agent 10 — Communications](<url>) |
| Communication | 11 | [Agent 11 — Sprint Plan](<url>) |
| Testing | 12 | [Agent 12 — Maze Tests](<url>) |
```

Use `updateConfluencePage` to replace the Agent Output Index section in the run parent page body with the linked version.

### Step 5: Report results

Print a summary:
- Run parent page: confirmed under 3870819267 ✓/✗
- Child pages found: N/12
- Child pages created: N
- Child pages moved (orphan fix): N
- parentId validations passed: N/N
- parentId validations fixed: N
- Pages with empty content fixed: N
- Index links updated: ✓/✗

If all 12 child pages exist with content, all parentIds are verified, and the index has links, the audit passes. Otherwise, list what remains broken.

## Inline Check (After Single Agent)

When running after a single agent completes:

1. Check if the agent's child page exists under the run parent page using `getConfluencePageDescendants`.
2. If missing, create it using `createConfluencePage` with the agent's output content.
3. **IMMEDIATELY run parentId validation** — call `getConfluencePage` on the newly created page and verify its parent matches the run parent page ID. If it doesn't match, fix it with `updateConfluencePage`. (See "Mandatory parentId Validation" section above.)
4. Use `updateConfluencePage` on the run parent page to add the new link to the index table.
5. Report: "Agent N — Title: published ✓ (parentId verified)" or "Agent N — Title: published ✓ (parentId FIXED — was under wrong parent)" or "Agent N — Title: FAILED — [reason]"

## MCP Tools Reference

All Confluence operations use these Atlassian MCP tools:

| Operation | Tool | Key Parameters |
|-----------|------|---------------|
| List children | `getConfluencePageDescendants` | `cloudId: "doctolib.atlassian.net"`, `pageId`, `depth: 1` |
| Read page | `getConfluencePage` | `cloudId: "doctolib.atlassian.net"`, `pageId`, `contentFormat: "markdown"` |
| Create page | `createConfluencePage` | `cloudId: "doctolib.atlassian.net"`, `spaceKey: "PTA"`, `parentId`, `title`, `body`, `contentFormat: "markdown"` |
| Update page | `updateConfluencePage` | `cloudId: "doctolib.atlassian.net"`, `pageId`, `parentId` (to move), `body`, `contentFormat: "markdown"` |
| Search pages | `searchConfluenceUsingCql` | `cloudId: "doctolib.atlassian.net"`, `cql: "title = \"...\" AND space.key = \"PTA\""` |

The `cloudId` is always `"doctolib.atlassian.net"`. The space key is always `"PTA"`. The root parent page ID is always `"3870819267"`.

## Common Failure Modes

- **Pages created under wrong parent (ORPHANED)**: Sub-agents receiving stale or incorrect parentId create pages under the wrong parent — sometimes the space root, sometimes another run's page. This was the #1 issue in Run 4 (2026-03-22), affecting Agents 3, 3.5, and 4. **Root cause**: sub-agents not reliably receiving the run parent page ID. **Fix**: The mandatory parentId validation step (above) catches this immediately after creation. Additionally, parent agents must pass the run parent page ID explicitly to every sub-agent as a parameter.
- **Pages created but empty**: Connection timeouts during content paste leave shell pages. Fix by updating with content from local files.
- **Index table has no links**: The summary page was published with plain text titles instead of clickable links. Fix by rebuilding the index with page URLs.
- **Duplicate pages**: Multiple pages with the same title. Keep the one under the correct parent, delete or rename the orphan.
- **Draft pages**: Pages stuck in draft status. Publish them by updating with `status: "current"`.
