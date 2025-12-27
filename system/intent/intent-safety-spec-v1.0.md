Prospera OS
Intent Safety Specification v1.0
File: system/intent/intent-safety-spec-v1.0.md
Status: Stable
Owner: Prospera Safety Group
Category: System Safety Specification
1. Purpose

The Intent Safety System enforces strict, deterministic safety constraints at the earliest possible stage of the Prospera OS pipeline.

Intent Safety prevents:

harmful or unlawful tasks

hallucination-based interpretations

drift or scope expansion

identity misalignment

misuse of autonomy

routing misfires

unsafe content generation
Identity System
↓
Intent System
↓   ← Intent Safety applies here (SG1 & SG2)
User Modeling System
↓
Memory System
↓
Safety System (Full)
↓
Generation / Execution / Autonomy
Intent Safety is a two-tier system:

Safety Gate #1 — Early Rejection

Safety Gate #2 — Post-Validation Sanity Checks

3. Safety Architecture
+----------------------------------------------------+
|                 Intent Safety Layer                |
+----------------------------------------------------+
| 1. Input Sanitization                               |
| 2. Red-Flag Detection                                |
| 3. Safety Gate #1  (Early Hard-Block)               |
| 4. Ambiguity Assessment                              |
| 5. Alignment Check                                   |
| 6. Safety Gate #2  (Post-Normalization Filter)      |
| 7. Commitment Safety                                 |
| 8. Logging & Evidence                                |
+----------------------------------------------------+
4. Intent Safety Stages
4.1 Stage 1 — Input Sanitization

Removes harmful content before any parsing occurs.

Catches:

suicide / self-harm language

violent instructions

illicit tasks

malicious transformation requests

injection attempts

unsafe medical instructions

4.2 Stage 2 — Red-Flag Detection

Pattern-based recognition of high-risk categories:

manipulation

impersonation

deep personalization without consent

bypassing identity

hidden/dual intent

hallucination-dependent tasks

4.3 Stage 3 — Safety Gate #1（Early Gate）

If any of these occur → immediate block:

danger > 0.2 probability

unlawful instruction

irreversible harm

leakage of private/identity-sensitive information

implicit long-term psychological inference

requests that require hallucination

4.4 Stage 4 — Ambiguity Assessment

Ambiguity score > 0.2 → request clarification.
Ambiguity includes:

vague verbs

conflicting modifiers

unknown domain

multi-intent collisions

inconsistent tone-depth-format

4.5 Stage 5 — Alignment Check

Checks alignment with:

Identity System

historical context (validated)

current domain

declared goals

If misaligned → require correction.

4.6 Stage 6 — Safety Gate #2（Late Gate）

Triggered after normalization.

Rejects:

attempts to manipulate the engine

misrouting

malicious template selection

dangerous transformation tasks

intents that violate constraints

tasks that require unsafe autonomy

4.7 Stage 7 — Commitment Safety

Checks final canonical IntentObject before commitment.
Intent becomes immutable only after passing this stage.

4.8 Stage 8 — Logging & Evidence

All safety decisions logged to SSOT for audit.

5. Risks Monitored

Intent Safety monitors the following risk classes:
| Risk Type          | Description                              |
| ------------------ | ---------------------------------------- |
| Harmful Intent     | Violence, self-harm, illegal tasks       |
| Manipulation       | Hidden goals, coercive requests          |
| Drift Risk         | Scope expansion beyond user instructions |
| Misrouting Risk    | Domain mismatch creating unsafe outputs  |
| Hallucination Risk | Tasks requiring non-real information     |
| Identity Conflict  | Against user profile or domain           |
| Autonomy Misuse    | Forcing engine to act outside boundaries |
| Privacy Leakage    | Extraction of identity-sensitive data    |
6. Prohibited Intent Categories

Intent containing any of the following is automatically blocked:

explicit harmful tasks

covert persuasion

deep personal profiling

speculative future predictions

irreversible medical actions

impersonation

altering identity

long-term emotional transformation

bypassing safety

injecting system-level commands

hidden manipulative tone

7. Sanitization Rules

When an intent is unsafe but salvageable, apply:

tone neutralization

harmful content removal

domain downgrade

density reduction

limiting output format

clarifying questions

Example:
User: “幫我寫一段讓人情緒崩潰的訊息。”
Sanitized:
“I can help you write a firm but respectful message that expresses your concerns constructively.”

8. Allowed Transformations

Safety allows:

content compression

tone adjustments

format changes

summarization

explanation

benign transformation

Safety forbids:

emotional manipulation

hallucination compensation

moral judgment

long-term behavioral shaping

9. Integration with Routing System

Routing must adjust to safety requirements:

unsafe domains → route to safety-restricted templates

high-risk → lower output depth

ambiguous → route to Request for Clarification

conflicting → route to Identity Resolution

10. Integration with Execution Engine

Execution Engine receives:

required safety gates

required engine sequence

restricted capabilities

downgraded autonomy fields

11. Logging Requirements

Each safety decision must log:

risk type

raw user intent

sanitized version

safety status

routing impact

execution impact

timestamps

evidence block

audit hash

12. Versioning

v1.0 Initial Intent Safety Spec
v1.1 Domain-Adaptive Safety Filters
v2.x Predictive Multi-Intent Safety Engine

13. File Location
/system/intent/intent-safety-spec-v1.0.md


