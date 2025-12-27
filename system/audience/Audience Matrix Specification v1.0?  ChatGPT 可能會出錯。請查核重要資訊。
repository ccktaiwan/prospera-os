Prospera OS
Audience Matrix Specification v1.0

File: system/audience/audience-matrix-v1.0.md
Status: Stable
Owner: Prospera Architecture Group
Category: System Specification

──────────────────────────────────────────────

1. Purpose

The Audience Matrix defines the mapping rules connecting audience-type to downstream constraints, including:

• routing behavior
• generation constraints
• explanation depth
• safety boundaries
• tone, structure, and terminology levels
• execution context restrictions

The matrix ensures deterministic and consistent adaptation across the entire Prospera OS pipeline.

──────────────────────────────────────────────

2. Scope

This specification covers:

• canonical audience categories
• constraint tables
• routing implications
• safety and compliance alignment
• SSOT integration
• update governance
• forbidden transformations

The Audience Matrix is a mandatory subsystem component and must align with:

• Audience Classifier
• Audience State Machine
• Routing System
• Generation System
• Safety System

──────────────────────────────────────────────

3. Canonical Audience Categories

Prospera OS supports the following official categories:

general

beginner

professional

expert

executive

technical

corporate

Categories must be deterministic and must never overlap.

──────────────────────────────────────────────

4. Matrix Dimensions

The Audience Matrix maps each audience-type to six deterministic dimensions:

4.1 Content Density

Values: low / medium / high / expert
Determines amount of information per unit.

4.2 Terminology Level

Values: basic / standard / specialized / domain-expert
Controls domain terminology usage.

4.3 Structural Complexity

Values: simple / guided / modular / analytical
Determines logical structure and pattern.

4.4 Tone Profile

Values: friendly / neutral / authoritative / executive
Defines target tone.

4.5 Safety Sensitivity

Values: low / medium / high / mandatory
Dictates safety restrictions.

4.6 Routing Priority

Values: explanation-first / action-first / summary-first / verification-first
Controls routing and pipeline behavior.

──────────────────────────────────────────────

5. Matrix Table (v1.0)

The v1.0 canonical audience matrix:
| Audience Type | Density | Terminology   | Structure  | Tone          | Safety | Routing Priority   |
| ------------- | ------- | ------------- | ---------- | ------------- | ------ | ------------------ |
| general       | medium  | basic         | guided     | friendly      | medium | explanation-first  |
| beginner      | low     | basic         | simple     | friendly      | high   | guided-explanation |
| professional  | medium  | standard      | modular    | neutral       | medium | action-first       |
| expert        | high    | domain-expert | analytical | authoritative | medium | verification-first |
| executive     | medium  | standard      | summary    | executive     | medium | summary-first      |
| technical     | high    | specialized   | analytical | neutral       | medium | accuracy-first     |
| corporate     | medium  | standard      | structured | executive     | high   | compliance-first   |

All values are immutable under v1.0.

──────────────────────────────────────────────

6. Routing Implications

The Audience Matrix directly modifies routing logic:

6.1 Explanation Depth

• general → medium
• beginner → extended
• expert/technical → condensed + precise
• executive → ultra-condensed summary

6.2 Format

• beginner → step-by-step
• professional → templates and checklists
• executive → high-level strategy blocks
• technical → structured models & schemas

6.3 Error Behavior

• beginner → soft error messages
• expert/technical → direct error reporting
• corporate → compliance-aligned error handling

──────────────────────────────────────────────

7. Generation Constraints

Matrix values influence Generation System as follows:

7.1 Allowed Vocabulary

Each audience type has a vocabulary whitelist/blacklist.

7.2 Forbidden Operations

• No over-simplification for technical/expert audiences
• No domain jargon for beginner audiences
• No narrative expansion for executive audiences
• No unverified implications for corporate audiences

7.3 Output Format Rules

Audience determines:
• paragraph length
• template usage
• visual vs textual bias
• terminology strictness

──────────────────────────────────────────────

8. Safety Alignment

Safety System must validate:

• terminology-risk alignment
• audience-appropriate content
• compliance needs (corporate/executive)
• drift between audience and intent
• hallucination risk based on category

If mismatch → Safety blocks pipeline.

──────────────────────────────────────────────

9. SSOT Integration

The Audience Matrix writes:

• matrix-version
• matrix-evaluation-result
• classification → matrix consistency hash
• drift-events (if matrix mismatch with classifier)

SSOT must treat matrix evaluations as immutable history.

──────────────────────────────────────────────

10. Governance Rules

Matrix updates (v1.x → v2.x) require:

• Governance Council approval
• Kernel compatibility check
• Safety review
• Regression validation

Matrix misalignment is treated as a structural drift event.

──────────────────────────────────────────────

11. Forbidden Operations

The Audience Matrix must never:

• infer personal attributes
• use probabilistic classification
• override Identity or Intent
• modify Safety constraints
• modify Generation logic directly
• contain executable logic
• bypass Routing System
• store sensitive user info

Violation → Governance escalation.

──────────────────────────────────────────────

12. Versioning

v1.0 Initial Audience Matrix
v1.1 Multi-domain extension table
v2.x Adaptive multi-context matrix model

──────────────────────────────────────────────

13. File Location

system/audience/audience-matrix-v1.0.md

──────────────────────────────────────────────
