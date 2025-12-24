Prospera OS SSOT (Single Source of Truth) Specification
Version v1.0
Category System State Specification
Location /system/ssot
Status Stable
Owner Prospera Architecture Group

Purpose
This document defines the Single Source of Truth (SSOT) architecture for Prospera OS.
The SSOT is the authoritative and immutable source for all system state, project state, identity state, and execution metadata.
All Engines and Modules must read from SSOT and may not maintain independent long-term state.

Core Principles

2.1 Uniqueness
There is only one SSOT per Prospera OS instance.
No duplication or shadow copies permitted.

2.2 Immutability
Past records are immutable.
New versions append diffs; no overwriting allowed.

2.3 Centralization
All persistent state must be written exclusively through the Pipeline Engine.

2.4 Determinism
SSOT must produce deterministic state for any given version.

2.5 Full Traceability
Every state change must be logged with:
timestamp
origin engine
action type
state diff
validation result
governance authorization

SSOT Structure
SSOT contains five major domains:

3.1 Identity Domain
user-identity
system-identity
active-role
active-project
project-permissions

3.2 Intent Domain
validated-intent
task-goal
task-boundaries
forbidden-intent-flags

3.3 Session Domain
current-phase
execution-checkpoints
backtracking-points
autonomy-flags
temporary-context

3.4 Project Domain
project-state
project-history
project-boundaries
project-constraints
version-index
governance-flags

3.5 System Domain
global-governance-state
safety-state
pipeline-state
ssot-version
engine-health-status

Writeback Contract
Only the Pipeline Engine may perform SSOT writebacks.
Writebacks must follow the flow:

Intake → Processing → Validation → Commit → Logging

4.1 Writeback Requirements
State update must:

Pass Safety validation

Pass Governance validation

Be deterministic

Generate complete log metadata

Respect immutability constraints

Update version index

4.2 Authorized Writers
Pipeline Engine (primary)
Recovery Engine (special mode, gated by governance)
Autonomy Engine (approved routines only)

All others are strictly forbidden.

Versioning Model

5.1 Version Flow
SSOT uses append-only versioning:

v1.0 → v1.1 → v1.2 → ... → vX.Y

5.2 Version Entries
Each version entry includes:

version-id
timestamp
state-diff
engine-origin
validation-packets
governance-flags
checksum-hash

5.3 Rollback Policy
Rollback does NOT modify SSOT.
Rollback creates:

rollback-marker
rollback-context
rollback-boundary

SSOT remains intact.

Forbidden Operations
SSOT may not be:
modified directly
overwritten
cross-project merged
copied into parallel states
edited by Engines other than Pipeline/Recovery

Dependency Rules
SSOT depends on:
Pipeline System
Governance System
Safety System
Identity System

All Engines depend on SSOT.

SSOT Health Checks
SSOT must pass:
integrity check
checksum validation
governance validation
state continuity check
pipeline consistency
no unauthorized diffs
no missing indexes

Versioning
v1.0 Initial SSOT definition
v1.1 Distributed SSOT model
v2.x Real-time SSOT synchronization

File Location
system/ssot/ssot-spec-v1.0.md
