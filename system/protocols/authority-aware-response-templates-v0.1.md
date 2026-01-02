Prospera OS
Authority-Aware Response Templates v0.1

File: system/protocols/authority-aware-response-templates-v0.1.md
Status: Draft
Owner: Prospera Architecture Group
Category: Operational Protocol

This document defines standardized response templates that MUST be used
when interpretation, explanation, or execution is restricted by authority,
governance, or SSOT constraints within Prospera OS.

Its purpose is to ensure that non-response, refusal, or escalation outputs
remain deterministic, professional, and auditable.


Purpose

This specification defines how an interpreter responds when:

- Authority cannot be resolved
- Interpretation is explicitly forbidden
- Governance blocks execution
- System information is incomplete or non-canonical

It replaces ad-hoc refusals, conversational hedging, and speculative explanations
with formal, authority-aligned responses.


Scope

These templates apply to:

- AI systems acting as engineering workers
- Human operators issuing system explanations
- Audit, review, and escalation contexts

They apply across all Prospera OS repositories and execution surfaces.


Core Principle

A blocked response is still a valid system output.

Correct refusal preserves system integrity and authority correctness.


Response Classification

All restricted responses MUST fall into one of the following classes.


Class A — SSOT Resolution Failure

Use when the requested information cannot be resolved to a canonical source.

Template:

“SSOT resolution failed.
The requested interpretation cannot be performed because no authoritative
source is defined in SYSTEM_INDEX.md.”


Class B — Authority Conflict Detected

Use when multiple sources exist but authority precedence cannot be determined.

Template:

“Authority conflict detected.
Multiple artifacts exist with overlapping scope, and no canonical authority
can be established without escalation.”


Class C — Interpretation Forbidden

Use when interpretation is explicitly blocked by governance or protocol rules.

Template:

“This interpretation is forbidden under Prospera OS governance rules.
No explanation or inference is permitted in this context.”


Class D — Scope Violation

Use when the request exceeds the scope of the current layer or role.

Template:

“The request exceeds the permitted scope for this execution context.
Escalation or re-scoping is required.”


Class E — Canonical Absence Confirmed

Use ONLY when SYSTEM_INDEX.md explicitly confirms non-existence.

Template:

“Canonical review completed.
The requested component is explicitly not defined within Prospera OS.”


Class F — Escalation Required

Use when resolution is possible only through governance or human authority.

Template:

“Resolution requires governance escalation.
No further action may be taken at this level.”


Prohibited Substitutions

Interpreters MUST NOT replace these templates with:

- Conversational apologies
- Speculative explanations
- Partial answers
- Contextual guessing
- “Helpful” alternatives

Only the defined templates are permitted.


Operational Rule

If a response does not clearly map to one response class,
the interpreter MUST select Class F (Escalation Required).


Interpretation Integrity Rule

A formally correct refusal is always preferred over an
informal or speculative answer.

Authority alignment takes precedence over completeness.


File Location

system/protocols/authority-aware-response-templates-v0.1.md

────────────────────────────────────────
End of Document
────────────────────────────────────────
