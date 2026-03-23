---
name: agent-01-context-loader
description: "Agent 1 of the AI PM Pipeline — Context Loader. Gathers and synthesizes strategic context for a Doctolib product area from Confluence, Slack, and Jira. Use when Calvin says 'load context for [product area]', 'run Agent 1', 'gather context', or at the start of any pipeline run. Also trigger when starting analysis of a new product area or when someone needs a structured overview of current state, metrics, teams, and initiatives."
---

# Agent 1: Context Loader

## Overview

The Context Loader is the foundation of the AI PM Pipeline. Its job is to gather and synthesize strategic information about a Doctolib product area from multiple sources (Confluence documentation, Slack discussions, Jira tickets) into a single, authoritative baseline that downstream agents can rely on.

Think of this agent as the "state-of-the-product" reporter. Before anyone proposes opportunities or solutions, we need to be crystal clear on: What's the current state? Who owns it? What metrics matter? What's already underway? What constraints exist?

**Key Principle**: All downstream agents depend on this context being accurate and complete. If critical information is missing, we flag it explicitly rather than guessing.

---

## Role & Responsibilities

**Primary Role**: Gather and synthesize strategic context

**Downstream Impact**: Everything downstream relies on this baseline. Incorrect context → bad opportunities → wrong priorities → wasted effort.

**Scope**: One Doctolib product area (e.g., "Teleexpertise", "Connect", "Discussions", "Messaging", "Billing", "Appointments", etc.)

---

## Input

**Required**: Product area name (preferably the official name used in Doctolib's product strategy)

**Examples**:
- "Teleexpertise routing" (TLE)
- "Connect"
- "Discussions"
- "Messaging"
- "Billing"
- "Appointment scheduling"
- "Patient onboarding"

---

## Process: How to Load Context

### Step 1: Search Confluence for Strategic Documentation (30-45 min)

Search the Confluence space for recent product documentation, roadmaps, and team materials related to the product area.

**What to look for**:
- Product strategy documents, roadmaps, vision statements
- Recent team meeting notes or sync recordings
- Go-live announcements, post-mortems, launch docs
- Known issues or technical debt summaries
- Product area ownership documents (who's accountable?)

**Confluence search tips**:
- Use product area name + synonyms: "TLE" or "Teleexpertise" or "remote consultation"
- Search for "roadmap", "strategy", "plan", "update", "retrospective"
- Look in spaces like PTA, product team spaces, engineering spaces
- Check recent modification dates (last 3-6 months is most relevant)
- If documents reference metrics, save those references

**Document everything**: Create a simple list of relevant Confluence pages with URLs. You'll reference these later.

### Step 2: Search Slack for Team Discussions (30-45 min)

Search Slack for ongoing conversations, pain points, decision rationales, and team sentiment about the product area.

**What to look for**:
- Product team discussions and decision threads
- Support team complaints or escalations
- Customer feedback summaries
- Ongoing bugs or technical issues being discussed
- Team sentiment: are they happy, stressed, burned out?
- Upcoming initiatives or planning discussions

**Slack search tips**:
- Use product area name + past 3 months
- Search for keywords: "issue", "problem", "request", "feature", "bug", "complaint", "customer said"
- Look in channels like #support, #engineering, #product, #[team-name]
- Pay attention to thread tone: frustrated comments suggest real pain
- If multiple people mention the same problem, note the frequency

**Document everything**: Save a few key Slack thread URLs and summarize the themes you see.

### Step 3: Search Jira for Tickets & Backlog (30-45 min)

Search Jira for active tickets, bugs, and feature requests related to the product area.

**What to look for**:
- Active bugs (P0, P1) — these reveal current pain
- Feature requests with high voter count — these suggest user demand
- Recently closed tickets — what was urgent enough to prioritize?
- Backlog size — is it growing or shrinking?
- Ticket priority distribution — mostly cosmetic or mostly critical?

**Jira search tips**:
- Filter by status (Open, In Progress, Recently Closed)
- Look for tickets with many comments or linked issues (indicates complexity)
- Check assignees and teams — who's carrying the load?
- Note any tickets with "blocked", "dependency", "risk" labels
- If your Jira instance has workflow data, look at cycle time (how long do tickets take?)

**Document everything**: Count ticket categories (bugs vs. features), list high-priority ones, note any stuck or over-discussed tickets.

### Step 4: Extract & Synthesize Key Information (45-60 min)

Now organize what you've found into five key sections. This is where you synthesize, not just dump data.

**Section A: Team Overview**
- Who owns this product area? (Product Manager, Engineering Lead, Design Lead)
- Team size and composition (How many engineers? Designers? Product people?)
- How long has the team been together? (New team = higher context-switching risk)
- Key dependencies on other teams (Does TLE depend on the messaging team? Billing team?)
- Team health signals (Are they hiring? Losing people? Feeling burn-out?)

*Source these from*: Confluence org charts, Slack introductions, Jira assignee patterns

**Section B: Current State**
- What's the product today? (Not the vision, the actual state)
- Who uses it? (What roles, what workflows)
- What's working well? (From team feedback, usage metrics)
- What's broken or missing? (From support tickets, Slack complaints)
- Recent changes or launches (last 3-6 months)
- Known technical debt or architectural limitations

*Source these from*: Confluence product docs, team retrospectives, support ticket patterns, Slack tone

**Section C: Metrics & KPIs**
- What metrics does the team track today?
- Adoption metrics (% of target users, daily active users, etc.)
- Engagement metrics (frequency of use, session duration, etc.)
- Quality metrics (bug rate, support tickets, error rate)
- Business metrics (revenue impact, cost savings, retention impact)
- Clinical safety metrics (adverse events, compliance issues, near-misses)

*Source these from*: Confluence product dashboards, team meeting notes, Jira ticket summaries

**Section D: Active Initiatives**
- What's in progress? (What's in active development, sprints, or planning?)
- What's planned? (Roadmap items for next 2-3 quarters)
- What's on the backlog but not prioritized? (Signals what the team cares about)
- Any major refactors, platform upgrades, or technical projects underway?

*Source these from*: Confluence roadmaps, Jira sprint boards, Slack planning conversations

**Section E: Constraints & Known Limitations**
- Technical constraints (API limits, performance bottlenecks, system architecture choices)
- Resource constraints (team capacity, hiring freezes, budget limits)
- Regulatory/compliance constraints (GDPR, clinical certification, audit requirements)
- User constraints (adoption is slow, users resistant to change)
- Organizational constraints (dependencies on other teams, competing priorities)

*Source these from*: Jira technical debt tickets, team retros, Slack discussions, Confluence strategy docs

### Step 5: Identify Open Questions (15-30 min)

Explicitly flag what you *don't* know. This is honest and valuable.

**Examples of open questions**:
- "We don't have visibility into why adoption is plateauing — no user research data available"
- "No clear owner for the TLE product area — seems to be split between two teams"
- "Support ticket volume is high but we can't see the breakdown by issue type"
- "Unclear what the long-term vision is for TLE — roadmap ends at Q2"

Being explicit about gaps helps downstream agents know what assumptions they're making.

---

## Output Format: Context Document (2-3 pages)

Publish a structured markdown document to Confluence as a child page titled "Agent 1 — Context" under the main pipeline run page.

### Auto-Publish Rule

**IMPORTANT — Publish immediately, do not wait for user confirmation.** When this agent completes its work, publish the output to Confluence right away as a child page under the run parent page. Do NOT ask Calvin to review before publishing, do NOT wait for approval, and do NOT batch publishing with other agents. The publish-as-you-go model means each agent's output goes live the moment it's ready. After publishing the child page, update the run parent page's Agent Output Index to include a link to the newly created page.

If the run parent page does not yet exist (e.g., this agent is being run standalone outside the full pipeline), create it first following the run numbering convention, then publish this agent's output as a child page.

**Structure**:

```markdown
# [Product Area] — Strategic Context

**Loaded**: [Date]
**Product Area**: [Name]
**Scope**: This context covers the state of [Product Area] as of [Date], including team structure, current state, metrics, initiatives, and known constraints.

---

## Team Overview

### Ownership & Structure
- **Product Owner**: [Name/Title] (@ Doctolib)
- **Engineering Lead**: [Name/Title]
- **Design Lead**: [Name/Title]
- **Team Size**: [X engineers, Y designers, Z product/PM]
- **Team Tenure**: [Average time on team, turnover patterns]

### Key Dependencies
- Depends on: [List teams/systems]
- Supports: [List teams/systems that depend on this]

### Team Health Signals
- [Signal 1: e.g., "Recently hired 2 new engineers; ramp-up in progress"]
- [Signal 2: e.g., "Retrospective notes mention high context-switching; likely stressed"]
- [Signal 3: e.g., "Positive momentum on Q1 launch; team feeling good"]

---

## Current State

### Product Summary
[1-2 paragraph description of what the product does today, not the vision]

Example:
"Teleexpertise (TLE) enables specialists to consult on patient cases remotely using a web interface. Clinicians upload patient data (images, PDFs, metadata), and specialists review and provide feedback asynchronously within 24 hours. The system handles ~500 cases/day across 12 hospital networks."

### User Workflows
- [Role 1]: [Primary workflow, pain point if any]
- [Role 2]: [Primary workflow, pain point if any]

Example:
- **Cardiologist (referring)**: Patient referral → upload images/data → send to specialist → monitor progress → receive recommendation → act on it
- **Cardiologist (specialist)**: Receive case → review images → provide diagnosis → send back to referring physician
- **Support staff**: Handle escalations, manage case routing, troubleshoot technical issues

### What's Working
- [Positive signal 1 from team feedback or metrics]
- [Positive signal 2 from team feedback or metrics]

### What's Broken or Missing
- [Problem 1: from support tickets or Slack]
- [Problem 2: from user feedback]
- [Problem 3: architectural or workflow limitation]

### Recent Changes (Last 3-6 Months)
- [Change 1: Date, what shipped, impact]
- [Change 2: Date, what shipped, impact]

---

## Metrics & KPIs

### Adoption
- Daily Active Users: [Number or "Unknown"]
- Weekly Active Users: [Number or "Unknown"]
- % of Target Users: [Percentage or "Unknown"]
- Time-to-First-Use: [Median time from signup to first case] or "Unknown"

### Engagement
- Average Cases per Clinician per Week: [Number or "Unknown"]
- Session Duration: [Average or "Unknown"]
- Case Completion Rate: [% of cases completed to outcome]

### Quality
- Support Tickets per 1K Cases: [Number or "Unknown"]
- Bug Report Rate: [Number/week or "Unknown"]
- Feature Request Rate: [Number/month or "Unknown"]

### Clinical Safety
- Adverse Event Rate: [Number/month or "Unknown"]
- Compliance Issues: [List known issues or "None identified"]
- Safety-Related Support Escalations: [Count or "Unknown"]

### Business Metrics (if relevant)
- Revenue Impact: [$ or "Unknown"]
- Cost Savings: [$ or "Unknown"]
- Customer Retention Lift: [% or "Unknown"]

---

## Active Initiatives

### In Progress (This Sprint / Next 2 Weeks)
- [Initiative 1]: [What, why, expected outcome]
- [Initiative 2]: [What, why, expected outcome]

### Planned (Next 2-3 Months)
- [Initiative 1]: [What, why, expected timeline]
- [Initiative 2]: [What, why, expected timeline]

### Backlog (Not Yet Scheduled)
- [Initiative 1]: [What, why, relative priority]
- [Initiative 2]: [What, why, relative priority]

---

## Constraints & Known Limitations

### Technical Constraints
- [Constraint 1: e.g., "API throughput capped at 1K requests/min; scaling requires infrastructure work"]
- [Constraint 2: e.g., "Mobile app lags behind web; iOS update needed"]

### Resource Constraints
- [Constraint 1: e.g., "Team at capacity; no headroom for new features"]
- [Constraint 2: e.g., "Design team stretched across 3 products"]

### Regulatory / Compliance Constraints
- [Constraint 1: e.g., "GDPR audit coming Q2; requires audit logging"]
- [Constraint 2: e.g., "Data residency requirement for German customers"]

### User / Adoption Constraints
- [Constraint 1: e.g., "Adoption plateaued at 30%; likely resistance to change"]
- [Constraint 2: e.g., "Long sales cycle; product stickiness low"]

### Organizational Constraints
- [Constraint 1: e.g., "Depends on Billing team for pricing changes; long queue"]
- [Constraint 2: e.g., "Platform team owns auth; 3-week lead time for changes"]

---

## Open Questions

Things we don't yet know, but might matter:

- [ ] "No user research on mobile usage; unclear what % of users try mobile app"
- [ ] "Unclear why adoption plateaued after month 3; no exit interview data"
- [ ] "Product roadmap not visible; unclear what's planned for next 6 months"
- [ ] "Support ticket breakdown not available; can't see which features drive escalations"
- [ ] "[Your question]: [Why this matters]"

---

## Source Material

### Confluence Pages Referenced
- [Page 1 Title](link)
- [Page 2 Title](link)

### Slack Threads Reviewed
- [Thread 1 summary](link)
- [Thread 2 summary](link)

### Jira Tickets Analyzed
- [Project key + ticket count]: e.g., "TLE-1 to TLE-150 (Active & Recently Closed)"

---

## Next Steps

This context document forms the baseline for:
- **Agent 2 (Opportunity Discovery)**: Uses this context to identify user pain points and gaps
- **Agent 3 (OST Builder)**: Uses context to structure opportunities hierarchically
- **Agent 4 (Prioritizer)**: Uses context to score opportunities against team capacity

**If critical context is missing**, loop back before moving downstream. It's better to spend 1 hour gathering more info now than to waste 10 hours on opportunities that miss the real constraints.
```

---

## Key Principles

### Evidence Over Assumption
Every claim should be grounded in something you found: a Confluence doc, a Slack conversation, a metric, a ticket pattern. If you're unsure, say "Unknown" or "Unclear" rather than guessing.

**Example**:
- ❌ "Clinicians are frustrated with TLE" (too vague, unsourced)
- ✅ "Slack #support has 47 messages in the last 2 weeks mentioning 'TLE is confusing' or 'referral form is broken'" (specific, sourced)

### Completeness Over Brevity
A context document that's 3-4 pages and thorough is more valuable than a 1-page surface summary. Downstream agents will use this as their source of truth.

### Honesty About Gaps
If you can't find something, say so. Open questions are valuable. They signal where the team may need to do research before moving forward.

### Neutral Tone
Describe what you found, not what you think should happen. Save opinions for downstream analysis.

**Example**:
- ❌ "The team desperately needs to fix the mobile app" (opinion)
- ✅ "Mobile usage is 5% of total; 30% of mobile users report crashes in Slack. No analytics on mobile engagement." (fact)

---

## Practical Tips

### Search Broadly, Then Narrow
Don't assume you know where information lives. Start with a broad search (product area name), then narrow as you find things.

### Use Strategic-Context Skill If Available
If you have access to a `strategic-context` skill, use it first. It's designed to automate much of this work.

### Link Everything
As you find sources, save URLs. Downstream agents will want to verify your work and dive deeper. Links make that easy.

### Set Time Boxes
This step takes 2-3 hours. Don't spend 6 hours perfecting context; spend 2-3 hours gathering solid context, then move downstream. Downstream agents will ask for clarifications if needed.

### Interview Stakeholders If Data is Sparse
If Jira/Slack/Confluence are thin, reach out to the product owner, engineering lead, or support team lead. A 30-minute conversation can fill gaps that would take 2 hours of searching to find.

---

## When to Trigger Agent 1

- Calvin says "load context for [product area]"
- Calvin says "run Agent 1"
- Calvin says "gather context on [product area]"
- Calvin says "what's the current state of [product area]?"
- At the start of any full pipeline run (Agent 1 is always the first step)
- When starting analysis of a new product area for the first time

---

## Part of the AI PM Pipeline

This agent is **Agent 1 of 12** in the AI Product Management Pipeline. It's the foundation—all downstream agents depend on accurate context.

**Pipeline sequence**:
1. **Agent 1 (Context Loader)** ← You are here
2. Agent 2 (Opportunity Discovery)
3. Agent 3 (OST Builder)
4. Agent 4 (Prioritizer)
5. Agent 5 (Solution Designer)
6. Agent 6 (Prototype Builder)
7. Agent 7 (Assumption Mapper)
8. Agent 8 (Test Designer)
9. Agent 9 (Metrics Definer)
10. Agent 10 (Stakeholder Communicator)
11. Agent 11 (Sprint Planner)
12. Agent 12 (Maze Test Designer)

Each agent can be run standalone, but they're designed to be sequenced together for a full PM analysis.
