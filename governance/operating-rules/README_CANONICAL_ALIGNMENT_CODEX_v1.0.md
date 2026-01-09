Prospera README Canonical Alignment Codex

Document Type: Engineering Compliance Codex
Scope: Repository README Alignment
Status: Canonical (Operational)
Owner: Prospera Architecture Group
Applies To: All Prospera-related repositories

Purpose

This codex defines the mandatory structural and semantic requirements for all repository-level README files within the Prospera ecosystem.

Its sole purpose is to ensure that:

Authority boundaries are non-ambiguous

System layer positioning is explicit

AI participation is correctly constrained

Canonical source-of-truth relationships are preserved

This codex does not introduce new governance rules.
It operationalizes existing governance constraints at the repository entry point.

Normative Requirement

Any repository README that fails any requirement defined in this document is considered non-conformant and must not be treated as canonical or operationally valid.

README Mandatory Compliance Requirements
R-1 Authority Boundary Declaration (Mandatory)

The README MUST explicitly declare:

Whether this repository holds authority (normally: NO)

Where authoritative definitions reside

The resolution rule in case of interpretation conflict

This declaration MUST appear within the first visible section of the README.

Ambiguity is not permitted.

R-2 Canonical System Positioning (Mandatory)

The README MUST explicitly specify its position relative to the Prospera five-layer system architecture, using one of the following forms:

System Layer X (Governance / System / Engine / Module / Interface)

Engine-class component under Layer 3

Non-system reference repository

Implicit positioning or inferred placement is invalid.

R-3 Explicit Non-Scope Declaration (Mandatory)

The README MUST contain a clearly labeled section defining what the repository explicitly does not do.

At minimum, this section must address:

Governance authority

Execution authorization

Decision-making capability

Human responsibility substitution

Absence of an explicit non-scope section constitutes non-compliance.

R-4 AI Role Constraint Declaration (Mandatory)

If AI, LLMs, agents, or automation are mentioned, the README MUST explicitly state:

AI operates as an Engineering Worker

AI holds no authority

AI holds no responsibility

AI outputs are artifacts, not decisions or outcomes

Any language implying autonomous decision authority is prohibited.

R-5 Canonical Source of Truth Reference (Mandatory)

The README MUST explicitly reference the canonical authority repository:

prospera-os

It MUST state that this repository is not the system-level source of truth.

Implicit reference or assumption is invalid.

Operational Use

This codex is intended to be used only during:

README creation

README modification

Repository review or normalization

It is not a standalone governance document and must not be extended into additional policy artifacts.

Change Control

This codex is intentionally minimal.

It may only be modified if:

A governance ambiguity cannot be prevented by existing rules

A repository-level authority failure has occurred or is imminent

Clarity or stylistic improvement alone is not a valid reason for change.

Canonical Status

This document is operationally canonical for README compliance.

It does not supersede Prospera OS governance.
It enforces it at the repository boundary.

End of Document
