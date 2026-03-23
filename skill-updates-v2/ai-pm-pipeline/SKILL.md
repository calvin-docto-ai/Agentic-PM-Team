---
name: ai-pm-pipeline
description: "Run the 13-agent AI Product Management pipeline for any product area. This master orchestrator takes a product domain and runs through 5 phases: Discovery (context loading, opportunity discovery, OST building, PRD writing, prioritization), Design (solution design, prototyping), Validation (assumption mapping, test design, metrics definition), Communication (stakeholder updates, sprint planning), and Testing (Maze unmoderated test blueprints). Use this skill whenever Calvin says 'run the pipeline', 'start a new analysis', 'do the full PM process', 'run all agents', or wants to analyze a new product area end-to-end. Also trigger when discussing the agent architecture, pipeline phases, or referencing specific agents by number (Agent 1-13)."
---

# AI Product Management Pipeline

## Overview

The AI PM Pipeline is a systematic 5-phase, 13-agent workflow designed to comprehensively analyze and develop solutions for Doctolib product areas. This pipeline transforms raw product data and user insights into validated, prototyped solutions with testing blueprints ready for deployment.

**Scope**: Any Doctolib product domain (Connect, TLE, Discussions, Messaging, Billing, etc.)

**Output**: Complete product analysis published to Confluence (PTA space), including strategic context, opportunities, designs, prototypes, validation plans, communications, and testing blueprints.

**Architecture**: Each agent independently processes input, produces structured output, publishes its output to Confluence immediately, and hands off to the next agent. The run parent page is created before any agent runs, and each agent's output is published as a child page the moment it completes — not batched at the end. This progressive publishing means stakeholders can follow along in real-time and no work is lost if the pipeline is interrupted.

---

## Phase 1: Discovery — Understanding the Landscape

The Discovery phase establishes a shared understanding of the product area, identifies user pain points and opportunities, structures those opportunities in a hierarchy, and prioritizes them using clinical safety and impact frameworks.

### Agent 1 — Context Loader

**Role**: Gather and synthesize strategic context.

**Input**: Product area name (e.g., "Teleexpertise routing")

**Process**:
1. Search Confluence for recent product documentation, roadmaps, and team updates in the product area
2. Search Slack for team discussions, decision rationales, and ongoing initiatives
3. Search Jira using **lightweight extraction** — pull only `summary`, `status`, `key`, `priority`, and `assignee` fields via JQL. Do NOT fetch full ticket JSON payloads. Count and categorize tickets (bugs vs. features, by priority), list high-priority items, and note stuck or over-discussed tickets. (See agent-01-context-loader skill for the full lightweight Jira protocol.)
4. Extract key information: team structure, current metrics, ongoing initiatives, known constraints, prior decisions
5. Organize context into sections: Team Overview, Current State, Metrics & KPIs, Active Initiatives, Open Questions, Constraints

**Context Reuse Rule**: If a previous Agent 1 run exists for the **same product area** from the **same calendar day** (i.e., less than ~16 hours old), you may reuse that context instead of re-gathering. When reusing: (a) explicitly state in the output header "Context reused from Run N (YYYY-MM-DD), gathered at [time]. Freshness: [X] hours." (b) verify the previous context page still exists and has content, (c) still publish a new "Agent 1 — Context" child page for this run (copy the content, add the reuse notice). For runs on a different day or different product area, always gather fresh context.

**Output**: Structured context document (markdown, 2-3 pages) published to Confluence child page "Agent 1 — Context"

**Key principle**: This agent ensures all downstream agents work from the same factual baseline. If information is missing, flag it explicitly.

---

### Agent 2 — Opportunity Discovery

**Role**: Uncover unmet user needs and product gaps.

**Input**: Context document from Agent 1

**Process**:
1. Review context for known pain points and user feedback mentions
2. Search Slack for support discussions, user complaints, and feature requests
3. Search Jira for support tickets and user-reported issues
4. Analyze patterns: what problems appear repeatedly? What user workflows are broken?
5. Interview or synthesize feedback from customer-facing teams (Support, Customer Success) if available
6. Generate 8-12 opportunities, each with: problem statement, affected users/roles, frequency of occurrence, impact if solved
7. Rank by frequency and severity of impact
8. Tag each opportunity with evidence source (ticket ID, Slack thread, feedback)

**Output**: Ranked opportunity list (markdown table, 1-2 pages) published to Confluence child page "Agent 2 — Opportunities"

**Structure**:
- Opportunity Title
- Problem Statement
- Affected User Roles
- Frequency (how often encountered)
- Impact Level (High/Medium/Low)
- Evidence Source(s)
- Notes

**Key principle**: Opportunities are grounded in evidence, not speculation. Each opportunity should reference at least one source.

---

### Agent 3 — Opportunity Solution Tree (OST) Builder

**Role**: Structure opportunities hierarchically to reveal relationships and dependencies.

**Input**: Opportunity list from Agent 2

**Process**:
1. Identify desired outcomes (e.g., "Clinicians can safely collaborate with specialists in real-time")
2. Map opportunities to outcomes — which opportunities drive which outcomes?
3. For each opportunity, identify possible solutions (high-level, not detailed yet)
4. Arrange in a tree structure: Outcomes → Opportunities → Solutions (parent-child relationships)
5. Identify cross-cutting opportunities (e.g., "Notification system" may serve multiple outcomes)
6. Create visual representation (indented list or ASCII tree)

**Output**: OST diagram/structure (markdown with hierarchy, 2-3 pages) published to Confluence child page "Agent 3 — Opportunity Solution Tree"

**Structure**:
```
Outcome: [What do we want to achieve?]
  Opportunity: [What gap prevents this?]
    Solution Option 1: [How might we solve this?]
    Solution Option 2: [Alternative approach]
  Opportunity: [Related opportunity]
    Solution Option 1:
    Solution Option 2:
```

**Key principle**: The OST reveals dependencies and shared solutions. If multiple opportunities point to the same solution, that becomes a higher-priority "lever."

---

### Agent 3.5 — PRD Writer

**Role**: Write Doctolib-standard PRDs for every solution option identified in the OST.

**Input**: OST from Agent 3 (with outcomes, opportunities, solution options), Context from Agent 1, Opportunities from Agent 2

**Process**:
1. Extract all solution options from the OST
2. For each solution option, write a PRD following the Doctolib standard template:
   - Metadata table (Status, PM, Tech Holder, Designer, etc.)
   - Section 1: Context (from Agent 1), Why solve this (from Agent 2), OKR alignment, KPI definition
   - Section 2: Discovery highlights (evidence from Agent 2)
   - Section 3: Solution description (user flow, user stories, scope, data/security considerations)
   - Section 4: Rollout strategy (default: France, A/B test, single batch)
   - Section 5: Impact measurement (tied to opportunity metrics)
3. Publish each PRD as a separate Confluence child page under the pipeline run page
4. Create an index page "Agent 3.5 — PRDs" linking to all individual PRDs

**Output**: Individual Confluence child pages per solution option PRD, plus an index page "Agent 3.5 — PRDs"

**Key principle**: PRDs follow the exact Doctolib template structure. Unknown fields are marked [TBD]. These PRDs feed into Agent 4 for more informed prioritization and Agent 5/6 for detailed design and prototyping.

---

### Agent 4 — Prioritizer

**Role**: Score and rank opportunities using weighted frameworks.

**Input**: Opportunity list from Agent 2, OST from Agent 3, and PRDs from Agent 3.5

**Process**:
1. For each opportunity, score across the ICE framework:
   - **Impact**: How many users affected? How severe is the problem? (1-10)
   - **Confidence**: How confident are we this will work? (1-10)
   - **Ease**: How easy is it to implement? (1-10)
   - ICE Score = (Impact × Confidence) / Ease

2. Apply clinical safety weighting:
   - If opportunity involves patient safety, diagnosis, prescribing, or critical workflow, multiply by 1.5
   - If opportunity directly enables compliance (GDPR, regulatory), multiply by 1.3
   - This ensures high-risk, high-value opportunities surface even if ease is low

3. Identify prototype-worthy opportunities (typically 5-10) — since AI prototyping is fast and cheap, the bar is 'worth a prototype?' not 'top 3 only'

4. Include a "watch list" of lower-ranked but promising opportunities

**Output**: Prioritized opportunities table with scoring and rationale (markdown, 1-2 pages) published to Confluence child page "Agent 4 — Prioritization"

**Structure**:
| Rank | Opportunity | Impact | Confidence | Ease | ICE Score | Safety Weight | Weighted Score | Rationale |
|------|-------------|--------|------------|------|-----------|---------------|----------------|-----------|
| 1 | ... | 9 | 8 | 7 | 10.3 | 1.5 | 15.4 | ... |

**Key principle**: Clinical safety always wins. If something is low-ICE but involves patient safety, it rises in priority. Transparency in scoring means stakeholders can understand trade-offs.

---

## Phase 2: Design — Creating Solutions

The Design phase takes the prototype-worthy opportunities (typically 5-10, not just 3) and generates solution options with pros/cons and risk assessment, then builds interactive prototypes.

### Agent 5 — Solution Designer

**Role**: Generate solution options for each priority.

**Input**: Prototype-worthy opportunities from Agent 4 (typically 5-10), with PRDs from Agent 3.5 for detailed requirements

**Process**:
1. For each priority opportunity:
   - Brainstorm 3-5 solution approaches (different UX patterns, different technical stacks, different workflow changes)
   - For each option, document:
     - User workflow: step-by-step how a user would interact
     - Key design decisions: what makes this option unique?
     - Pros: advantages, user benefits
     - Cons: limitations, risks, trade-offs
     - Effort estimate: small (1-2 sprints), medium (3-4 sprints), large (5+ sprints)
     - Risk assessment: technical risk, adoption risk, safety risk
     - Dependencies: what else needs to happen first?

2. Sketch wireframes or user flows for each option (text description or ASCII art is fine at this stage)

3. Highlight the "recommendation" option — which feels most balanced for impact, effort, and risk?

**Output**: Solution options document (markdown with detailed descriptions, 4-6 pages) published to Confluence child page "Agent 5 — Solution Design"

**Structure per priority**:
```
## Priority 1: [Opportunity Title]

### Solution Option A: [Name]
- User Workflow: [Description of how user interacts]
- Key Decisions: [What's different here?]
- Pros:
  - [Benefit 1]
  - [Benefit 2]
- Cons:
  - [Limitation 1]
  - [Limitation 2]
- Effort: Medium (3-4 sprints)
- Risk: Technical (moderate), Adoption (low), Safety (low)
- Recommendation: ⭐ Yes / No [reasoning]

### Solution Option B: [Name]
...
```

**Key principle**: Multiple solutions should feel genuinely different, not marginal variations. Pros and cons should be concrete, not vague.

---

### Agent 6 — Prototype Builder

**Role**: Create interactive HTML prototypes using Doctolib's design system, hosted via GitHub Pages.

**Input**: Solution options from Agent 5, PRDs from Agent 3.5, Confluence run page title

**Process** (four sequential phases — repo setup, then prototyping, then QA, then publish):

1. **Repo Setup**:
   - Clone `https://github.com/calvin-docto-ai/OS-prototype-scaffolding` locally for baseline templates and design tokens
   - Create a run folder named after the Confluence run page title, sanitized for URLs (lowercase, hyphens, no special chars — e.g., `2026-03-22-3-ai-pm-agent-run-tle`)
   - All prototypes are built directly inside this folder

2. **Prototype Creation**:
   - Use the Doctolib Chrome Shell (Oxygen Design System) as the baseline UI framework
   - For each solution option per priority, build a clickable HTML prototype directly in the run folder
   - Each prototype starts as an exact copy of the baseline — modify ONLY the solution-specific content area
   - Add floating nav bar for switching between options; include a landing page (`index.html`)
   - All internal links must use relative paths (bare filenames) since prototypes live in a subfolder

3. **Quality Assurance**:
   - Run ruthless visual QA (minimum 3 rounds, 5 auditors) to verify no unintended baseline divergence
   - Run link/path verification to ensure all nav bar links, landing page links, and inter-prototype links work correctly in the subfolder structure
   - Fix all issues before publishing

4. **Publish**:
   - Clone `https://github.com/calvin-docto-ai/ai-pm-prototypes` (shared repo for all runs)
   - Copy the run folder into the shared repo, commit, and push
   - Verify GitHub Pages deployment — prototypes are live at `https://calvin-docto-ai.github.io/ai-pm-prototypes/<folder-name>/`
   - Update Confluence with live prototype URLs

**Output**:
- HTML prototype files (one per solution option, plus landing page) in a named run folder
- Pushed to shared repo `calvin-docto-ai/ai-pm-prototypes` and live on GitHub Pages
- Published to Confluence child page "Agent 6 — Prototypes" with live URLs

**File structure** (inside the shared repo):
```
ai-pm-prototypes/
  2026-03-22-3-ai-pm-agent-run-tle/
    index.html (landing page)
    proto-p1a-recommender.html
    proto-p1b-directory.html
    proto-p1c-network.html
    ...
  2026-04-15-1-ai-pm-agent-run-connect/
    index.html
    ...
```

**Key principle**: Prototypes should feel realistic — use real Doctolib UI patterns, color schemes, and terminology. Repo setup happens first, prototyping second, QA third, publishing last — never interleave git operations with prototype creation.

---

## Phase 3: Validation — De-Risking the Solution

The Validation phase identifies the riskiest assumptions behind each solution, designs experiments to test them, and defines success metrics.

### Agent 7 — Assumption Mapper

**Role**: Surface hidden assumptions that could derail a solution.

**Input**: Solution options from Agent 5

**Process**:
1. For each solution option, identify 5-10 critical assumptions
2. Categorize each assumption by type:
   - **Desirability**: Will users actually want this? Will they use it?
   - **Viability**: Can we build this with our current resources? Is it sustainable?
   - **Feasibility**: Is the technology feasible? Are there system constraints?
   - **Usability**: Will users be able to figure out how to use it? Will they understand the value?

3. For each assumption, assess **riskiness**:
   - How confident are we this is true? (1-10, where 10 = very confident)
   - What's the impact if we're wrong? (High/Medium/Low)
   - Riskiness = (10 - Confidence) × Impact

4. Rank assumptions by riskiness — focus on the top 5 per solution

5. Document the assumption registry with:
   - Assumption statement
   - Category (D/V/F/U)
   - Confidence level
   - Impact if wrong
   - Riskiness rank
   - Notes on why we believe this (or doubt it)

**Output**: Assumption registry (markdown table, 2-3 pages) published to Confluence child page "Agent 7 — Assumptions"

**Structure**:
| Assumption | Category | Confidence | Impact | Riskiness | Notes |
|-----------|----------|-----------|--------|-----------|-------|
| Clinicians will adopt the new workflow within 2 weeks | D | 6/10 | High | 40 | They're skeptical of change; prior adoption was slow |
| The notification system can handle 10K messages/min | F | 9/10 | Medium | 5 | We've load-tested; this is our standard throughput |

**Key principle**: Assumptions should be specific and testable, not vague (e.g., "users will like it" is too vague; "users will use the new search 3+ times per day" is testable).

---

### Agent 8 — Test Designer

**Role**: Design experiments to validate critical assumptions.

**Input**: Assumption registry from Agent 7 and solution options from Agent 5

**Process**:
1. For each high-riskiness assumption, design an experiment:
   - **Test type**: Qualitative interview, unmoderated user test (Maze), A/B test, load test, etc.
   - **Sample size**: How many participants/records do we need?
   - **Duration**: How long will the test take? (hours, days, weeks?)
   - **Success criteria**: What would success look like? What constitutes validation?
   - **Failure criteria**: What result would tell us to pivot?
   - **Measurement method**: How do we measure? (task completion rate, time on task, survey response, server metrics, etc.)

2. Sequence experiments by dependency:
   - Run desirability tests early (interview, prototype test) before investing in build
   - Run viability/feasibility tests in parallel with design
   - Run usability tests after basic prototype

3. Create experiment cards, each documenting one test

**Output**: Experiment cards (markdown, 3-4 pages) published to Confluence child page "Agent 8 — Test Design"

**Structure per experiment**:
```
## Experiment: Assumption [Title]

**Assumption**: [From assumption registry]

**Test Type**: Unmoderated User Test (Maze)

**Sample Size**: 20 practicing clinicians

**Duration**: 15 minutes per participant, 3-day test window

**Success Criteria**:
- 85%+ task completion rate for primary workflow
- Average task time < 2 minutes
- 7+/10 ease of use rating

**Failure Criteria**:
- Completion rate < 70%
- Multiple users unable to find key feature

**Measurement Method**:
- Maze task recording and analytics
- Time-on-task from click stream
- Post-task survey (3 questions)

**Participants**: Clinicians with 2+ years specialty experience, daily EHR users

**Success Outcome**: Proceed to development kickoff
**Failure Outcome**: Redesign Option B and retest
```

**Key principle**: Tests should be proportional to risk — high-risk assumptions warrant formal tests; low-risk assumptions can be validated through conversation.

---

### Agent 9 — Metrics Definer

**Role**: Define success metrics and KPIs for each solution.

**Input**: Solution options from Agent 5 and test experiments from Agent 8

**Process**:
1. For each solution option, define success metrics across:
   - **User Adoption**: % of target users who activate the feature within 30 days
   - **Engagement**: Frequency of use (e.g., times per week), session duration
   - **Task Efficiency**: Time to complete workflow, steps required, error rate
   - **User Satisfaction**: NPS or CSAT for the feature
   - **Clinical Safety**: Adverse events, near-misses, workflow deviations
   - **Business Impact**: Revenue impact, cost savings, retention impact
   - **Quality**: Bug reports, support tickets related to feature

2. For each metric, document:
   - **Leading indicator**: What predicts success early? (e.g., prototype task completion)
   - **Lagging indicator**: What's the true measure of long-term success? (e.g., 30-day active use)
   - **Target**: What's the goal? (e.g., 70% adoption, 4 uses/week)
   - **Measurement method**: How do we collect this data? (analytics, survey, support ticket count, etc.)
   - **Cadence**: How often do we check? (real-time, daily, weekly, monthly)

3. Create a metrics framework that connects experiments to long-term KPIs
   - "Maze test showed 85% task completion → we expect 65% adoption launch week"
   - "If engagement drops below 2x/week after 60 days, we pivot"

**Output**: Metrics framework (markdown, 2-3 pages) published to Confluence child page "Agent 9 — Metrics"

**Structure**:
```
## Primary KPIs: [Priority Opportunity]

### Adoption
- **Leading**: Prototype task completion rate (target: 80%+)
- **Lagging**: % of eligible users with at least 1 use in first 30 days (target: 65%)
- **Measurement**: Analytics dashboard (feature flag tracking)
- **Cadence**: Daily in first 30 days, then weekly

### Engagement
- **Leading**: % of users who complete full workflow in Maze (target: 75%+)
- **Lagging**: Average weekly uses per active user (target: 3+)
- **Measurement**: Analytics event tracking, weekly cohort analysis
- **Cadence**: Weekly

### Clinical Safety
- **Leading**: Zero high-severity issues in QA testing
- **Lagging**: Zero adverse events in first 90 days; ≤2 support escalations
- **Measurement**: QA sign-off, incident tracking, support ticket analysis
- **Cadence**: Real-time monitoring, weekly review

### User Satisfaction
- **Leading**: Average task ease rating in Maze (target: 7+/10)
- **Lagging**: Feature-specific NPS (target: 40+)
- **Measurement**: In-app survey after 10th use
- **Cadence**: Monthly cohort surveys, aggregated quarterly
```

**Key principle**: Metrics should be actionable — if a leading indicator fails, you pivot before sinking months into a lagging indicator. Leading and lagging indicators should show cause-and-effect.

---

## Phase 4: Communication — Alignment and Planning

The Communication phase ensures stakeholders understand the strategy and upcoming work is organized into sprints.

### Agent 10 — Stakeholder Communicator

**Role**: Tailor updates for different audiences.

**Input**: All previous agents' outputs (context, opportunities, design, validation)

**Process**:
1. Identify stakeholder audiences:
   - **Executives**: Care about impact, timeline, resource needs
   - **Engineering**: Care about technical approach, effort, dependencies
   - **Design**: Care about UX, user feedback, usability risks
   - **Product**: Care about strategy, metrics, go/no-go decisions

2. For each audience, create a tailored update (1-2 pages):
   - **Headline**: What's the key news?
   - **Context**: Why are we doing this?
   - **Opportunity**: What's at stake?
   - **Recommendation**: Which solution option? Why?
   - **Next Steps**: What happens next? Timeline?
   - **Asks**: What do we need from you? (budget, headcount, approval, etc.)

3. Use audience-appropriate language:
   - Executives: revenue impact, clinical value, competitive advantage
   - Engineering: architecture, technical risk, code impact
   - Design: user pain points, prototype feedback, usability testing results
   - Product: metrics, experiments, go/no-go criteria

**Output**: Stakeholder updates (markdown, 3-4 pages total) published to Confluence child page "Agent 10 — Communications"

**Structure**:
```
## Executive Summary

[2-3 paragraphs on opportunity, impact, timeline, resource ask]

## Engineering Brief

[Technical architecture, dependencies, effort estimate, risk]

## Design Brief

[UX approach, user workflows, prototype feedback, design risk]

## Product Brief

[Metrics framework, validation plan, go/no-go criteria, timeline]
```

**Key principle**: Same content, different lenses. Execs see ROI; engineers see risk; designers see UX. Each update should feel native to its audience.

---

### Agent 11 — Sprint Planner

**Role**: Break the recommended solution into sprint-ready work items.

**Input**: Recommended solution from Agent 5, experiments from Agent 8, metrics from Agent 9

**Process**:
1. Decompose the recommended solution into work streams:
   - Backend/Infrastructure
   - Frontend/UX
   - QA/Safety
   - Launch/Communication

2. For each work stream, identify sprints (1-3 month effort blocks):
   - **Sprint 0 (Validation)**: Run key experiments, validate assumptions
   - **Sprint 1-2 (MVP)**: Build minimum viable version of the solution
   - **Sprint 3 (Polish)**: UX refinement, edge cases, performance
   - **Sprint 4 (Launch)**: Production hardening, documentation, go-live

3. For each sprint, document:
   - **Goals**: What's the objective?
   - **Work items**: Specific tickets (user stories, bugs, refactors)
   - **Capacity**: How many engineering/design/PM days?
   - **Dependencies**: What needs to be done first?
   - **Risks**: What could go wrong?
   - **Success criteria**: How do we know we've finished?

4. Identify cross-team dependencies (e.g., "Backend API must be ready before Frontend can start")

5. Create a **Gantt-like timeline** showing which teams are active in which weeks

**Output**: Sprint plan (markdown, 4-5 pages) published to Confluence child page "Agent 11 — Sprint Plan"

**Structure**:
```
## Sprint 0: Validation (Weeks 1-2)

**Goal**: Validate core assumptions before committing to full build

**Engineering Effort**: 4 days (spike on integration points)
**Design Effort**: 3 days (prototype refinement)
**QA Effort**: 2 days (test plan review)

**Work Items**:
- [ ] Backend spike: Load testing for 10K msg/min throughput (2 days)
- [ ] Frontend spike: Notification system integration with existing nav (1.5 days)
- [ ] UX research: 3-user prototype feedback session (1.5 days design, 1 day analysis)
- [ ] QA review: Document safety testing strategy (2 days)

**Risks**:
- Load test reveals performance bottleneck → May need to redesign data model
- Users confused by navigation → May need to redesign prototype

**Success Criteria**:
- Load test passes for target throughput
- Prototype achieves 80%+ task completion
- No safety red flags identified

---

## Sprint 1: MVP Build (Weeks 3-6)

**Goal**: Deliver minimum viable version of the solution

**Capacity**: 6 engineers (backend), 3 engineers (frontend), 2 designers, 1 QA

**Dependencies**: Backend spike complete, design finalized

**Work Items**:
- [ ] Backend: User notification service (3 sprints-worth)
- [ ] Frontend: Notification UI component library (2 sprints-worth)
- [ ] Design: User onboarding flow (1 sprint)
- [ ] QA: Functional testing plan, edge case catalog (ongoing)

...
```

**Key principle**: Sprints are planning units, not execution units. This plan is a hypothesis. As teams move through sprints, they'll learn and adjust. The plan should be reviewed every 2 weeks and updated as needed.

---

## Phase 5: Testing — Preparing for Launch Validation

The Testing phase creates Maze-native unmoderated test blueprints ready for setup and execution.

### Agent 12 — Maze Test Designer

**Role**: Create production-ready Maze unmoderated test blueprints.

**Input**: Recommended solution prototype from Agent 6, experiments from Agent 8

**Process**:
1. Design the Maze test structure with 6 blocks (Maze standard):
   - **Welcome Block**: Introduce the test, explain scenario
   - **Statement Block**: Context-setting statement (e.g., "You're a cardiologist reviewing a patient case")
   - **Prototype Task Block**: Show the prototype, ask user to complete a workflow (e.g., "Refer this patient to a specialist. Please show us how you'd do this in the app.")
   - **Opinion Scale Block**: 1-10 rating of ease, confidence, or satisfaction
   - **Open Question Block**: Open-ended feedback (e.g., "What was confusing about the referral process?")
   - **Thank You Block**: Closing, incentive info

2. Create realistic personas with scenarios:
   - **Persona 1**: Cardiologist, 15+ years experience, uses EHR daily
     - Scenario: "You need to refer a complex case to a colleague at another clinic. Walk us through how you'd do it."
   - **Persona 2**: Generalist, 5-10 years experience, uses EHR 4+ hours daily
     - Scenario: "A patient asks for a specialist referral. Show us how you'd handle it."

3. Document task instructions clearly:
   - What's the user's goal?
   - What are success criteria? (e.g., "Successfully send referral to a specific specialist")
   - What's the expected difficulty? (easy/moderate/hard)
   - Explain any non-obvious UI elements

4. Plan for open-ended feedback:
   - Ask about specific pain points from assumptions
   - Invite suggestions for improvements
   - Ask about adoption likelihood ("Would you use this in your daily workflow?")

5. Define screening criteria:
   - Target audience (specialist type, experience level, location)
   - Technical requirements (browser, device)
   - Exclusion criteria (prior involvement in project, competitive interest)

6. Create a Maze project blueprint document that can be directly implemented:
   - Block-by-block copy/paste text
   - Question wording
   - Success criteria per task
   - Analysis plan (which metrics matter most?)

**Output**: Maze test blueprints (markdown with structured, copy-paste-ready content, 5-6 pages) published to Confluence child page "Agent 12 — Maze Tests"

**Structure**:
```
## Maze Test: [Solution Option A] - Referral Workflow

### Test Overview
- **Objective**: Validate that clinicians can intuitively refer specialists using the new workflow
- **Audience**: Cardiologists and generalists with 5+ years experience
- **Sample Size**: 20 participants
- **Duration**: 12-15 minutes per participant
- **Success Criteria**: 80%+ task completion, 7+/10 ease rating

---

### Block 1: Welcome

**Maze Block Type**: Welcome Screen

**Heading**: "Thanks for testing our new referral system!"

**Description**:
"We're designing a new way for you to refer patients to specialists. This test takes about 12-15 minutes. You'll see a prototype of the new interface and complete a referral task in it."

**CTA Button**: "Start Test"

---

### Block 2: Statement

**Maze Block Type**: Statement

**Content**:
"You're a [cardiologist/generalist] seeing a patient today. The patient needs a referral to a specialist, and you need to send it through the hospital's network. Let's see how you'd do this in our new system."

---

### Block 3: Prototype Task

**Maze Block Type**: Prototype

**Embedded Prototype**: [Link to prototype or file upload]

**Task Instruction**:
"Please complete this task in the prototype below:

Your patient needs a referral to a nephrologist (kidney specialist) at a specific hospital in your network. Using the interface below, show us how you would send that referral. Once you've sent the referral, take a screenshot or tell us you're done.

**What counts as completion**: The referral is successfully sent and you see a confirmation message."

**Help Text** (optional, for if user is stuck):
"Look for a 'Referral' or 'Refer Patient' option in the main menu or navigation."

**Success Criteria**:
- User navigates to referral form
- User selects correct specialist type
- User selects correct hospital
- User completes form and submits
- User receives confirmation

**Task Difficulty**: Moderate

---

### Block 4: Opinion Scale

**Maze Block Type**: Rating (1-10 scale)

**Question**: "How easy was it to send that referral?"

**Scale Labels**: 1 = Very Difficult, 10 = Very Easy

---

### Block 5: Open Question

**Maze Block Type**: Open-Ended Question

**Question**: "What was the most confusing part of the referral process, if anything?"

**Max Response Length**: 500 characters

---

### Block 6: Thank You

**Maze Block Type**: Thank You Screen

**Heading**: "Thank you for testing!"

**Description**: "Your feedback is invaluable. We'll use it to refine the design before launch."

---

### Analysis Plan

**Primary Metrics**:
- Task completion rate (target: 80%+)
- Average time-on-task (baseline from prototype)
- Ease of use rating (target: 7+/10)

**Secondary Insights**:
- Bottleneck steps (where did users struggle?)
- Terminology clarity (did users understand "referral", "specialist", etc.?)
- Feature discoverability (could they find the referral function?)

**Go/No-Go Decision**:
- **Go**: 80%+ completion, 7+ ease rating, no critical usability issues mentioned
- **No-Go**: <70% completion OR 3+ users report critical confusion OR safety concerns raised

---

### Participant Screening

**Target Audience**:
- Cardiologists (50%), Internists/Generalists (50%)
- 5+ years clinical experience
- Use hospital EHR daily

**Geographic**: [Location if relevant, e.g., Switzerland]

**Exclusion Criteria**:
- <5 years experience
- Works outside hospital setting (private practice only)
- Prior involvement in this project

**Tech Requirements**:
- Desktop or tablet (Chrome, Safari, Edge preferred)
- Broadband internet
- Quiet environment
```

**Key principle**: The blueprint should be complete enough that someone without design or research experience could copy-paste it into Maze and launch the test. Every question, instruction, and criterion is explicit.

---

## Confluence Structure

All outputs publish to the **PTA** (Product Testing & Analysis) space on Confluence with this hierarchy:

**IMPORTANT**: All run parent pages MUST be created as children of the **AI-Product Management Team** page (ID: `3870819267`, URL: https://doctolib.atlassian.net/wiki/spaces/PTA/pages/3870819267/AI-Product+Management+Team). This is the central hub for all pipeline runs. Never create run pages at the top level of the PTA space — they must always be nested under this parent page.

```
PTA (Space)
└── AI-Product Management Team (Page ID: 3870819267)
    └── YYYY-MM-DD-N — AI PM Agent Run ([Product Area]) (Run Parent Page)
        ├── Agent 1 — Context (Child)
        ├── Agent 2 — Opportunities (Child)
        ├── Agent 3 — Opportunity Solution Tree (Child)
        ├── Agent 4 — Prioritization (Child)
        ├── Agent 5 — Solution Design (Child)
        ├── Agent 6 — Prototypes (Child)
        ├── Agent 7 — Assumptions (Child)
        ├── Agent 8 — Test Design (Child)
        ├── Agent 9 — Metrics (Child)
        ├── Agent 10 — Communications (Child)
        ├── Agent 11 — Sprint Plan (Child)
        └── Agent 12 — Maze Tests (Child)
```

### How to Create Confluence Pages (Required MCP Tools)

All Confluence page creation and updates use the Atlassian MCP tools — specifically `createConfluencePage`, `updateConfluencePage`, and `getConfluencePageDescendants`. These are fast, reliable, and handle authentication automatically. Do NOT use Chrome browser automation or bash/curl for Confluence operations — they are slow, fragile, and often fail due to editor timeouts.

**Creating a page — `createConfluencePage`:**
```
createConfluencePage(
  cloudId: "doctolib.atlassian.net",
  spaceKey: "PTA",
  parentId: "<PARENT_PAGE_ID>",     ← see below for which ID to use
  title: "Page Title Here",
  body: "<markdown content>",
  contentFormat: "markdown"
)
```

The tool returns the new page's `id` — save it, because you'll use it as `parentId` when creating child pages.

**For the run parent page**, `parentId` is always `"3870819267"` (the AI-Product Management Team hub page). Every pipeline run page is a child of this page — no exceptions.

**For each agent child page**, `parentId` is the run parent page ID you got back from the step above.

**Updating a page — `updateConfluencePage`:**
```
updateConfluencePage(
  cloudId: "doctolib.atlassian.net",
  pageId: "<PAGE_ID_TO_UPDATE>",
  body: "<updated markdown content>",
  contentFormat: "markdown"
)
```

**Checking existing child pages — `getConfluencePageDescendants`:**
```
getConfluencePageDescendants(
  cloudId: "doctolib.atlassian.net",
  pageId: "3870819267",
  depth: 1
)
```

Use this to determine the run number N before creating a new run page (count how many pages matching today's date already exist).

### Progressive Publishing (Publish-As-You-Go)

The pipeline publishes to Confluence incrementally — after EACH agent completes, not in a batch at the end. This ensures stakeholders can follow along in real-time and that no work is lost if the pipeline is interrupted mid-run.

**Execution order for Confluence publishing:**

1. **Before Agent 1 runs**: Use `createConfluencePage` with `parentId: "3870819267"` to create the run parent page (e.g., `2026-03-22-1 — AI PM Agent Run (TLE)`). The parent page initially contains only the header metadata (date, scope, data sources, pipeline version) and an empty Agent Output Index table. Save the returned page ID — all subsequent child pages use this as their `parentId`.

2. **After EACH agent completes**: Immediately use `createConfluencePage` with `parentId: "<run_parent_page_id>"` to publish that agent's output as a child page. Do NOT wait for subsequent agents to finish. The child page should be fully written and published before the next agent begins its work.

3. **IMMEDIATELY validate parentId**: After every `createConfluencePage` call, call `getConfluencePage` on the returned page ID to verify its actual parent matches the intended parent. If the parentId is wrong, fix it immediately with `updateConfluencePage`. This is mandatory — in Run 4 (2026-03-22), 3 of 13 pages were orphaned because sub-agents used incorrect parentIds. See the `documentation-checker` skill for the full validation procedure.

4. **After EACH agent publishes (and parentId is verified)**: Use `updateConfluencePage` to update the run parent page's Agent Output Index table, adding a link to the newly published child page. This means the parent page is updated N times during a run (once per agent), progressively building out the index. Anyone viewing the parent page mid-run can see which agents have completed and click through to their outputs.

5. **After the FINAL agent completes**: Do one last `updateConfluencePage` on the run parent page to fill in the Outcomes, Feedback Analyzed, and Recommended Learnings sections (which require all agent outputs to write). The Agent Output Index should already be complete from the incremental updates.

**Why this matters:**
- If the pipeline fails at Agent 7, Agents 1-6 are already published and accessible — no work is lost
- Stakeholders can review early outputs (context, opportunities) while later agents are still running
- The run parent page serves as a live progress tracker during execution

### Run Numbering Convention

Every pipeline run creates a new run parent page as a **child of page ID `3870819267`** (AI-Product Management Team) in Confluence — even if multiple runs happen on the same day. The naming format is:

```
YYYY-MM-DD-N — AI PM Agent Run ([Product Area])
```

Note the format carefully: the run number N comes right after the date, then an em dash (—), then "AI PM Agent Run", then the product area in parentheses.

Where **N** is the sequential run number for that date:
- First run of the day: `2026-03-22-1 — AI PM Agent Run (TLE)`
- Second run same day: `2026-03-22-2 — AI PM Agent Run (TLE)`
- Third run same day: `2026-03-22-3 — AI PM Agent Run (TLE)`

**How to determine N**: Before creating the parent page, use `getConfluencePageDescendants` on page `3870819267` and count child pages matching today's date. Increment to get N. If none exist, N=1.

**When creating the run parent page**, always use `createConfluencePage` with `parentId: "3870819267"`. Then create all agent child pages with their `parentId` set to the newly created run parent page ID.

This ensures every run is preserved and traceable — re-running a pipeline never overwrites previous results. Stakeholders can compare Run 1 vs Run 2 to see how the analysis evolved.

### Run Summary Page Structure

The run parent page is the primary entry point for stakeholders. Its content should be focused on outcomes and process — not raw data dumps. Use this exact structure:

```markdown
# AI PM Agent Run — [Product Area] (Run N)

**Date:** [date]
**Scope:** [product area] — Full 12-Agent Pipeline
**Data Sources:** [list sources used]
**Pipeline Version:** v2 (12-agent, 5-phase)

---

## Outcomes

[1-2 sentences describing what was produced — how many prototypes, how many priorities.]

**[View all prototypes →]([link to Agent 6 — Prototypes child page])**

[Embed a screenshot/preview image of the prototype landing page here. Do NOT attempt to programmatically upload images to Confluence — instead, leave a placeholder instruction for the user to drag the image from their workspace folder into the page.]

---

## Feedback Analyzed

[1 paragraph: how many verbatim feedback items were ingested, from which sources (Slack channels, Jira tickets, Confluence docs), and how many distinct opportunities were identified.]

### Top Pain Points

[For each prototype-worthy opportunity, write 1-2 sentences: the problem, why it matters, and its weighted ICE score.]

### Solutions Considered

[Table with columns: Priority | Solutions (list A-E names) | Detail (link to Agent 5 child page)]

**Recommended options:** [list the recommended option for each priority]

---

## Recommended Learnings

[Agent retrospective on the pipeline run itself. What worked, what didn't, what should change. Write 6-10 bullet points covering topics like: data quality issues, token/size limits hit, bottlenecks in the process, mistakes made during the run, missing validation steps, late-surfacing dependencies, and suggestions for improving the pipeline or skill instructions.]

---

## Agent Output Index

[Table with columns: Phase | Agent # | Title (as clickable link to child page)]
```

**Key principles for the summary page:**
- Focus on outcomes and process, not raw data
- Do NOT include a "Current State" metrics table — that belongs in Agent 1 (Context)
- Do NOT include a "What Changed Since Run N-1" section — the page should stand on its own
- The Recommended Learnings section is a genuine retrospective where the agent reflects on what went wrong and what could be improved — be honest and specific, not generic
- Keep it scannable — a stakeholder should understand the run's value in 30 seconds

---

## How to Run the Pipeline

### Prerequisites
1. **Confluence Access**: Write permissions in the PTA space
2. **Slack Access**: Ability to search for product discussions and feedback
3. **Jira Access**: Ability to search for tickets in the product area
4. **Prototype Baseline**: Doctolib Chrome Shell HTML template (Oxygen Design System)
5. **Optional Skills**: strategic-context, doctolib-prototyper, maze-test-designer (if available)
6. **Documentation Checker**: The `documentation-checker` skill (if available) validates Confluence structure after each agent and at the end of the run. Use it.

### Execution Steps

**IMPORTANT — Publish-as-you-go**: Every step below follows the same pattern: do the agent work → publish child page to Confluence → run documentation-checker → move to next agent. Never defer publishing to the end.

**IMPORTANT — Documentation Checker**: After EVERY agent publishes its child page, and again after the final agent completes, run the `documentation-checker` skill to verify the page was created correctly, is under the right parent, has content, and the index table is updated with a link. If the documentation-checker finds problems, fix them before moving on. At the end of the full pipeline run, run the documentation-checker in "full audit" mode to verify the entire Confluence structure.

**IMPORTANT — parentId Validation**: After EVERY `createConfluencePage` call (whether for the run parent page or any agent child page), immediately verify the parentId by reading the page back with `getConfluencePage` and checking its actual parent. If wrong, fix immediately with `updateConfluencePage`. This is not optional — it prevents the orphaned-page bug observed in Run 4. When spawning sub-agents, always pass the run parent page ID explicitly as a parameter; sub-agents must NOT look up or infer the parentId themselves.

0. **Create Run Parent Page** (before any agent runs)
   - Determine the run number N by searching for existing child pages of page `3870819267` matching today's date
   - Create the run parent page as a child of `3870819267` with the title `YYYY-MM-DD-N — AI PM Agent Run ([Product Area])`
   - Initial content: header metadata (date, scope, data sources, pipeline version) and an empty Agent Output Index table
   - **Save the parent page ID** — every subsequent step uses this as `parentId` for child pages
   - This page is the live progress tracker; stakeholders can watch it fill in as agents complete

1. **Load Strategic Context** (Agent 1)
   - **Check for reusable context first**: If a previous pipeline run exists for the **same product area** from **today** (same calendar day), you may reuse that run's Agent 1 context instead of re-gathering from scratch. This saves significant time without sacrificing freshness (validated in Run 4 reusing Run 2 context, only 7 hours old). When reusing, add a prominent notice to the output: `"⚡ Context reused from Run N (YYYY-MM-DD), originally gathered at [time]. Freshness: [X] hours. For a different product area or next-day runs, fresh context is always gathered."`
   - If no reusable context exists, or if the product area differs: use the `strategic-context` skill if available, otherwise manually search Confluence, Slack, Jira for product area info
   - For Jira specifically: use **lightweight extraction** — query with JQL but pull only `summary`, `status`, `key`, `priority`, and `assignee` fields. Do not fetch full ticket JSON. Categorize and count rather than dump raw data.
   - **PUBLISH NOW**: Create Confluence child page "Agent 1 — Context" under the run parent page
   - **VALIDATE parentId**: Immediately verify the child page's parent is the run parent page ID
   - **UPDATE PARENT**: Add Agent 1 link to the Agent Output Index table on the run parent page

2. **Run Opportunity Discovery** (Agent 2)
   - Input: Context from Agent 1
   - Analyze support tickets, Slack discussions, user feedback
   - Generate 8-12 ranked opportunities
   - **PUBLISH NOW**: Create Confluence child page "Agent 2 — Opportunities" under the run parent page
   - **UPDATE PARENT**: Add Agent 2 link to the Agent Output Index table on the run parent page

3. **Build OST** (Agent 3)
   - Input: Opportunities from Agent 2
   - Structure in a hierarchy (Outcomes → Opportunities → Solutions)
   - **PUBLISH NOW**: Create Confluence child page "Agent 3 — Opportunity Solution Tree" under the run parent page
   - **VALIDATE parentId**: Immediately verify the child page's parent is the run parent page ID (Agent 3 was orphaned in Run 4)
   - **UPDATE PARENT**: Add Agent 3 link to the Agent Output Index table on the run parent page

3.5. **Write PRDs** (Agent 3.5)
   - Input: OST from Agent 3, Context from Agent 1, Opportunities from Agent 2
   - Extract all solution options from OST
   - For each solution option, write Doctolib-standard PRD with metadata, context, discovery highlights, solution description, rollout strategy, impact measurement
   - Publish individual PRDs as child pages under the pipeline run page
   - **VALIDATE parentId on EVERY PRD page**: Agent 3.5 spawns sub-agents per PRD — each sub-agent must receive the run parent page ID explicitly as a parameter and validate parentId after creating its page (Agent 3.5 was orphaned in Run 4)
   - Create index page "Agent 3.5 — PRDs" linking to all individual PRDs

4. **Prioritize** (Agent 4)
   - Input: Opportunities from Agent 2, OST from Agent 3, PRDs from Agent 3.5
   - Score using ICE + clinical safety weighting
   - Identify prototype-worthy opportunities
   - **PUBLISH NOW**: Create Confluence child page "Agent 4 — Prioritization" under the run parent page
   - **VALIDATE parentId**: Immediately verify the child page's parent is the run parent page ID (Agent 4 was orphaned in Run 4)
   - **UPDATE PARENT**: Add Agent 4 link to the Agent Output Index table on the run parent page

5. **Design Solutions** (Agent 5)
   - Input: Prototype-worthy opportunities from Agent 4, with PRDs from Agent 3.5 for detailed requirements
   - Generate 3-5 solution options per priority
   - Document pros/cons, effort, risk for each
   - **PUBLISH NOW**: Create Confluence child page "Agent 5 — Solution Design" under the run parent page
   - **UPDATE PARENT**: Add Agent 5 link to the Agent Output Index table on the run parent page

6. **Build Prototypes** (Agent 6)
   - Input: Solution options from Agent 5
   - Create interactive HTML prototypes using Doctolib Chrome Shell
   - Include floating nav bar to switch between options
   - If available, use the `doctolib-prototyper` skill
   - **PUBLISH NOW**: Create Confluence child page "Agent 6 — Prototypes" under the run parent page
   - **UPDATE PARENT**: Add Agent 6 link to the Agent Output Index table on the run parent page with links/attachments

8. **Map Assumptions** (Agent 7)
   - Input: Solution options from Agent 5
   - Identify 5-10 critical assumptions per option
   - Categorize by type (Desirability, Viability, Feasibility, Usability)
   - Rank by riskiness
   - **PUBLISH NOW**: Create Confluence child page "Agent 7 — Assumptions" under the run parent page
   - **UPDATE PARENT**: Add Agent 7 link to the Agent Output Index table on the run parent page

9. **Design Experiments** (Agent 8)
   - Input: Assumption registry from Agent 7
   - Design tests (Maze, interviews, load tests) for high-risk assumptions
   - Specify sample size, success criteria, measurement methods
   - **PUBLISH NOW**: Create Confluence child page "Agent 8 — Test Design" under the run parent page
   - **UPDATE PARENT**: Add Agent 8 link to the Agent Output Index table on the run parent page

10. **Define Metrics** (Agent 9)
   - Input: Solution options from Agent 5, experiments from Agent 8
   - Define leading and lagging indicators
   - Set targets and measurement methods
   - **PUBLISH NOW**: Create Confluence child page "Agent 9 — Metrics" under the run parent page
   - **UPDATE PARENT**: Add Agent 9 link to the Agent Output Index table on the run parent page

11. **Create Stakeholder Updates** (Agent 10)
    - Input: All previous agents' outputs
    - Create tailored updates for Executives, Engineering, Design, Product
    - **PUBLISH NOW**: Create Confluence child page "Agent 10 — Communications" under the run parent page
   - **UPDATE PARENT**: Add Agent 10 link to the Agent Output Index table on the run parent page

12. **Plan Sprints** (Agent 11)
    - Input: Recommended solution from Agent 5, experiments from Agent 8
    - Break into 4-6 sprints with work items, capacity, dependencies
    - **PUBLISH NOW**: Create Confluence child page "Agent 11 — Sprint Plan" under the run parent page
   - **UPDATE PARENT**: Add Agent 11 link to the Agent Output Index table on the run parent page

13. **Design Maze Tests** (Agent 12)
    - Input: Recommended solution prototype from Agent 6, experiments from Agent 8
    - Create Maze-native test blueprints (6 blocks, personas, tasks, analysis plan)
    - If available, use the `maze-test-designer` skill
    - **PUBLISH NOW**: Create Confluence child page "Agent 12 — Maze Tests" under the run parent page
   - **UPDATE PARENT**: Add Agent 12 link to the Agent Output Index table on the run parent page

14. **Run Documentation Checker — Full Audit** (after all agents complete)
    - Use the `documentation-checker` skill in full audit mode
    - Verify: run parent page is a child of `3870819267`
    - Verify: all 12 agent child pages exist under the run parent page with content
    - Verify: Agent Output Index table on the run parent page has clickable links to every child page
    - Fix any issues found (orphaned pages, missing pages, empty content, broken links)
    - Only report the run as complete to the user after the documentation checker passes

### Iteration & Feedback

- After Agent 6 (Prototypes), share with stakeholders for feedback. Use feedback to refine solution options before moving to validation.
- After Agent 8 (Test Design), review experiments with research/QA teams. Adjust test plans if needed.
- After Agent 11 (Sprint Plan), review with engineering leadership. Adjust capacity/timeline as needed.
- The pipeline is not strictly sequential; you can loop back if new information emerges (e.g., if prototype feedback invalidates a priority, re-run Agent 4 and downstream).

---

## Key Principles

### 1. Evidence Over Speculation
Every claim should reference a source: ticket ID, Slack thread, interview, metric. "We think users want X" is weaker than "12 support tickets mention X in the last month."

### 2. Clinical Safety Comes First
In scoring and prioritization, safety always wins. If an opportunity involves patient safety, diagnosis, or compliance, it gets weighted higher than pure convenience features.

### 3. Prototypes Match Product Reality
Prototypes use real Doctolib terminology (TLE, Connect, Discussions, etc.), real Oxygen Design System colors/components, and realistic data. Viewers should feel like they're using Doctolib, not a wireframe tool.

### 4. Each Agent is Independently Rerunnable
You should be able to re-run Agent 5 (Solution Designer) with updated priorities without re-running Agents 1-4. Outputs are modular and hand off cleanly.

### 5. Transparent Trade-Offs
Solutions have trade-offs. Rather than hiding them, document them explicitly: "Option A is faster to build but requires team retraining. Option B is slower but requires minimal process change." Stakeholders can then make informed decisions.

### 6. Metrics Connect to Decisions
Success metrics aren't just nice-to-have dashboards. They're decision gates: "If adoption doesn't reach 50% in 30 days, we pivot to Option B." This makes metrics actionable.

### 7. All Content in English
All outputs, prototypes, and test materials are in English (Doctolib's primary working language for product development).

---

## When to Use This Skill

Trigger this skill when:
- Calvin says "run the pipeline" or "start a new analysis" for a product area
- Calvin asks to "do the full PM process" or "run all agents"
- Calvin references specific agents by number ("run Agents 1-4 for X product")
- Calvin asks to analyze a new product area end-to-end (e.g., "analyze the Billing product area")
- Calvin discusses the agent architecture or pipeline phases and needs a reference
- You're uncertain whether a task should be run as part of the pipeline vs. standalone

---

## Troubleshooting & Notes

- **Agent 1 (Context Loader) — Jira payloads too large**: When JQL returns many tickets (25+), the full JSON payloads are heavy and require Python extraction scripts to parse. **Always use lightweight Jira extraction**: query with JQL but request only `summary`, `status`, `key`, `priority`, and `assignee` fields. Count and categorize tickets (e.g., "14 bugs, 8 features, 3 tasks; 5 P0/P1") rather than dumping raw JSON. This was a key learning from Run 4 (2026-03-22).
- **Agent 1 (Context Loader) finds no Slack/Jira data**: This is common for newer product areas. Document what you couldn't find explicitly. Rely on stakeholder interviews to fill gaps.
- **Agent 2 (Opportunities) generates fewer than 8 opportunities**: That's okay. Fewer, well-evidenced opportunities are better than fluffy padding. Proceed with what you have.
- **Agent 4 (Prioritizer) finds opportunities too similar to rank**: Group them. If three opportunities are really "variations on the same theme," treat them as one priority with multiple sub-options.
- **Agent 6 (Prototypes) — Doctolib Chrome Shell not available**: Use a generic SPA template (React, Vue, etc.) styled with Oxygen Design System colors/components. The shell is ideal but not required.
- **Agent 8 (Test Designer) — No budget for Maze**: Design the tests anyway. Suggest lower-cost alternatives (unmoderated Lookback, synchronous user interviews, internal dog-fooding). The test design is still valuable.
- **Stakeholders want to review mid-pipeline**: This is now the default behavior. Because every agent publishes to Confluence immediately, stakeholders can follow the run parent page and click into completed agent pages at any time. If feedback changes strategy, re-run affected agents and their child pages will be updated in place.

---

## Changelog

- **2026-03-22 Retro from TLE Run 3**: Updated Agent 4 references from "top 3 priorities" to "prototype-worthy opportunities" (5-10). AI prototyping is cheap — don't artificially narrow the funnel.
