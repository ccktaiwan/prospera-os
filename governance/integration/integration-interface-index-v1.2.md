Prospera OS
Integration Interface Index v1.2 (Normalized)

File: governance/integration/integration-interface-index-v1.2.md
Status: Stable
Owner: Prospera Architecture Group
Category: Governance

Purpose

This document provides the normalized, authoritative index of all System-to-System integration interfaces for Prospera OS v1.2.

Its purpose is to eliminate duplicate listings, consolidate references, and establish a single lookup source without altering interface semantics, ownership, or behavior.

Scope

This index applies to all Integration Protocols across the System Layer.

The document is read-only with respect to interface definitions and does not introduce, remove, or modify any interface.

Architecture

The Integration Interface Index is a governance artifact that maps Systems to their declared integration interfaces.

It references authoritative Integration Protocol documents and must not be treated as an implementation or behavioral specification.

Normalization Rules

The following rules govern this index.

Each interface appears exactly once in this index.

One authoritative source document is designated per interface.

All other occurrences must reference the authoritative source.

Interface names follow the Terminology Map v1.2 (Final).

No aliases are permitted in this index.

Authoritative Interface Index
Audience System

audience classification snapshot intake
Authoritative source: system/audience/audience-system-integration-protocol-v1.2.md

audience state handoff to content
Authoritative source: system/content/content-system-integration-protocol-v1.2.md

Content System

content directive intake
Authoritative source: system/content/content-system-integration-protocol-v1.2.md

generation directive handoff
Authoritative source: system/generation/generation-system-integration-protocol-v1.2.md

Generation System

generation output reference handoff
Authoritative source: system/generation/generation-system-integration-protocol-v1.2.md

safety checkpoint validation request
Authoritative source: system/safety/safety-system-integration-protocol-v1.2.md

Execution System

execution eligibility signal intake
Authoritative source: system/execution/execution-system-integration-protocol-v1.2.md

post-execution routing request
Authoritative source: system/routing/routing-system-integration-protocol-v1.2.md

rollback invocation request
Authoritative source: system/backtracking/backtracking-system-integration-protocol-v1.2.md

Routing System

routing directive evaluation
Authoritative source: system/routing/routing-system-integration-protocol-v1.2.md

redispatch eligibility evaluation
Authoritative source: system/routing/routing-system-integration-protocol-v1.2.md

Safety System

safety clearance confirmation
Authoritative source: system/safety/safety-system-integration-protocol-v1.2.md

recovery escalation signal emission
Authoritative source: system/recovery/recovery-system-integration-protocol-v1.2.md

Backtracking System

rollback depth specification intake
Authoritative source: system/backtracking/backtracking-system-integration-protocol-v1.2.md

post-rollback routing context handoff
Authoritative source: system/backtracking/backtracking-system-integration-protocol-v1.2.md

Recovery System

recovery escalation signal intake
Authoritative source: system/recovery/recovery-system-integration-protocol-v1.2.md

Identity System

identity reference intake
Authoritative source: system/identity/identity-system-integration-protocol-v1.2.md

Intent System

intent declaration intake
Authoritative source: system/intent/intent-system-integration-protocol-v1.2.md

intent snapshot handoff
Authoritative source: system/intent/intent-system-integration-protocol-v1.2.md

Modeling System

state abstraction model handoff
Authoritative source: system/modeling/modeling-system-integration-protocol-v1.2.md

predictive model reference output
Authoritative source: system/modeling/modeling-system-integration-protocol-v1.2.md

Autonomy System

autonomous trigger evaluation
Authoritative source: system/autonomy/autonomy-system-integration-protocol-v1.2.md

Governance Notes

Duplicate interface listings detected in Phase D have been consolidated.

No interface names, parameters, or responsibilities were changed.

This index must be used as the single reference for interface discovery.

Versioning

This index is aligned with Prospera OS Kernel v1.2.

Any interface addition or removal requires a version increment.

File Location

governance/integration/integration-interface-index-v1.2.md

────────────────────────────────────────
End of Document
────────────────────────────────────────
