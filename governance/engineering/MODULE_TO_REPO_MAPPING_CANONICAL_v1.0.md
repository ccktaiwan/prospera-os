MODULE → REPOSITORY MAPPING CANONICAL
Governed Implementation Boundary Specification

Status: Canonical
Version: v1.0
Owner: Prospera Architecture Group
Scope: Module Implementation Governance
Authority: Prospera OS (SSOT)
Depends On:

MODULE_REGISTRY_CANONICAL_v1.0.md

ENGINE_INVENTORY_CANONICAL_v1.0.md

1. Purpose

This document defines where each canonical module is allowed to be implemented.

A module may only exist inside explicitly permitted repositories.
Any implementation outside this mapping is a governance violation.

2. Hard Governance Rule

Modules do not float across repositories.

Each module MUST map to:

One or more explicitly permitted repository types

Zero implicit fallback locations

3. Repository Classes (Normative)

prospera-os

prospera-execution-layer

prospera-generation-layer

client-repo-template

client-validation-repo

violation-sample-repo

No other repository classes are valid.

4. Canonical Mapping Table

Module ID: MOD-INTENT-CLASSIFIER
Permitted Repos:

prospera-os
Forbidden Repos:

client-repo-template

prospera-generation-layer

Module ID: MOD-MANUS-GENERATION
Permitted Repos:

prospera-generation-layer
Forbidden Repos:

prospera-os

client-repo-template

Module ID: MOD-PHASE-LOCK
Permitted Repos:

prospera-os
Forbidden Repos:

any client repository

Module ID: MOD-WORKFLOW-ROUTER
Permitted Repos:

prospera-execution-layer
Forbidden Repos:

prospera-os

5. Enforcement

If a module is detected in an unauthorized repository:

Execution MUST halt

Governance escalation is mandatory

The artifact is invalidated

6. Canonical Status

This mapping is authoritative.
Module existence outside permitted repositories is prohibited.

End of Document
