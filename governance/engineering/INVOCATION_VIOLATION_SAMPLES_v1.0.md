ENGINE × MODULE INVOCATION
Violation Samples (Canonical)

Status: Canonical
Version: v1.0
Owner: Prospera Architecture Group
Scope: Invocation Violation Examples
Authority: Prospera OS (SSOT)
Depends On:

ENGINE_MODULE_INVOCATION_CONTRACT_CANONICAL_v1.0.md

ENGINE_MODULE_MATRIX_CANONICAL_v1.0.md

1. Purpose

This document defines explicit forbidden invocation patterns.

These examples exist to prevent ambiguity.
They are governance hard-stops.

2. Violation B1 — Authority Escalation

Invocation-ID: INV-VIOL-001
Engine-ID: Semantic-Generation-Engine
Module-ID: Policy-Decision-Module
Decision-Authority-Level: L3
Operational-Reality-Domain: D

Result: BLOCKED

Violation:
Engine attempted to cross authority ceiling.
Generation engine cannot operate at L3.

3. Violation B2 — Execution Without Governance

Invocation-ID: INV-VIOL-002
Engine-ID: Execution-Engine
Module-ID: External-Action-Module
Decision-Authority-Level: L2
Operational-Reality-Domain: C

Result: BLOCKED

Violation:
Attempted real-world operational action without explicit governance authorization.

4. Violation B3 — Missing Human Responsibility

Invocation-ID: INV-VIOL-003
Engine-ID: Temporal-Sequence-Engine
Module-ID: Workflow-Trigger-Module
Responsible-Human: UNDEFINED

Result: BLOCKED

Violation:
No accountable human defined.
Invocation invalid by default.

5. Violation B4 — Silent Fallback Attempt

Invocation-ID: INV-VIOL-004
Engine-ID: Mobile-Context-Engine
Module-ID: Alternative-Context-Module
Fallback-Attempt: TRUE

Result: BLOCKED

Violation:
Fallback substitution without governance revalidation is forbidden.

6. Canonical Rule

Violation examples are absolute prohibitions.

Any system exhibiting these patterns is non-compliant.

End of Document
