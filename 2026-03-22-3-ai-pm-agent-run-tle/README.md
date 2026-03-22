# Priority 1: Fix Email Validation Blocker — 3 HTML Prototypes

## Overview
Three complete HTML prototypes built from the Doctolib Chrome Shell baseline, addressing the P1 email validation issue with different approaches.

## Files Generated

### 1. **proto-p1a-hotfix-popup.html** (2311 lines)
**P1A: Direct IAM-1990 Hotfix**
- **Concept**: Before/After toggle showing the broken email validation popup vs. the fixed working version
- **Features**:
  - Toggle switch at top (Before Fix / After Fix)
  - "Before Fix" state: Greyed-out broken popup with error message
  - "After Fix" state: Working 6-digit code input, success animation, green background
  - Interactive toggle with visual feedback
- **Design**: Contrast between error state and success state
- **Navigation**: Floating nav bar with A (active), B, C options

### 2. **proto-p1b-sms-fallback.html** (2352 lines)
**P1B: SMS/2FA Bypass Strategy**
- **Concept**: Step-by-step flow showing email validation attempt → failure → SMS fallback → verification
- **Features**:
  - 3-step horizontal stepper (Email → SMS Fallback → Complete)
  - Step 1: Email input form with send button
  - Step 2: Email validation fails (error display) + SMS fallback option with phone number input
  - Step 3: 6-digit SMS code verification
  - Success state with completion message
  - Back/Next navigation between steps
- **Design**: Dual-path verification flow, clear error states
- **Navigation**: Floating nav bar with B (active), A, C options

### 3. **proto-p1c-tle-prevalidation.html** (2460 lines)
**P1C: TLE Pre-Validation Stepper**
- **Concept**: Multi-step TLE enrollment with email validation as step 1
- **Features**:
  - 3-step horizontal stepper (Email Validate → Find Expert → Confirm)
  - Step 1: Email validation with 4 inline states
    - Empty: Prompt to enter email
    - Validating: Animated spinner
    - Valid: Green checkmark + success message
    - Error: Red error indicator
  - Step 2: Expert search with dropdown + location filter + selectable expert cards
  - Step 3: Review & confirm with status indicators
  - Success state with completion confirmation
  - Full step navigation (back/next)
- **Design**: Interactive stepper with state management, realistic medical data
- **Navigation**: Floating nav bar with C (active), A, B options

## Technical Details

### Baseline Structure
All three prototypes preserve the complete Doctolib Chrome Shell:
- Full CSS variable system with design tokens
- Sidebar navigation (76px fixed left panel)
- Header with user controls (52px fixed top)
- Sub-sidebar with item list (230px expandable)
- Responsive layout foundation

### Content Replacement
Each prototype replaces **ONLY** the content inside `<main class="content"><div class="content-inner">...</div></main>` while keeping:
- All CSS (lines 1–900)
- All sidebar HTML
- All header HTML
- All sub-sidebar HTML
- Body structure and closing tags

### Floating Navigation Bar
All three include a fixed dark navy bottom bar with:
- P1 priority indicator (red dot #EF4444)
- Home link
- Active/Inactive option buttons (A, B, C)
- Hover effects on inactive buttons

### Styling & Design Tokens
- **Colors**: Uses Doctolib design tokens (`--dtl-blue: #0596DE`, `--dtl-navy: #1B2A4A`, etc.)
- **Typography**: Open Sans font family (already loaded in baseline)
- **Spacing**: Consistent padding/margins aligned with 8px grid
- **Shadows**: Use baseline shadow definitions
- **Border radius**: 6px for inputs, 8px for cards, 24px for nav bar

### Interactive Elements
- **P1A**: Toggle switch with state management
- **P1B**: Multi-step flow with forward/backward navigation
- **P1C**: Stepper with email validation states, expert selection, form submission

### Data
- Realistic names: Dr. Michel BERNARD, Sarah Leclerc, Jennifer Marshall, Dr. Michel BERNARD, Dr. Isabelle DURAND
- Real locations: Paris, Lyon, Marseille, Levallois-Perret
- Medical specialties: Cardiologist, Dermatologist, Neurologist, Ophthalmologist

## Design Distinctiveness

### P1A: Hotfix Popup
- Visual contrast: Before (greyed, broken) vs. After (green, working)
- Quick toggle for immediate before/after comparison
- Ideal for demonstrating a direct code fix

### P1B: SMS Fallback
- Flow-based approach showing realistic failure scenario
- Clear error messaging with SMS as recovery path
- Demonstrates service resilience and alternative options

### P1C: Pre-Validation
- Proactive validation before main enrollment flow
- Interactive email state machine (empty → validating → valid/error)
- Complete enrollment flow from validation through submission

## File Paths
```
/sessions/elegant-sleepy-dijkstra/prototype-build/2026-03-22-3-ai-pm-agent-run-tle/
├── proto-p1a-hotfix-popup.html        (P1A - Hotfix Popup)
├── proto-p1b-sms-fallback.html        (P1B - SMS Fallback)
└── proto-p1c-tle-prevalidation.html   (P1C - Pre-Validation Stepper)
```

## Next Steps
- Test interactive flows in browser
- Gather feedback on visual distinctiveness
- Refine UX based on user testing
- Consider motion/animation enhancements
