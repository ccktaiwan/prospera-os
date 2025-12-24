Prospera OS Operation Templates
Version v1.0
Category Operational Execution Templates
Location /system/operations/templates
Status Stable
Owner Prospera Architecture Group

Purpose
The Operation Templates define the standardized execution patterns used across all Prospera OS tasks.
These templates ensure consistent, deterministic, auditable, and governance-compliant behavior across all systems and engines.

Template Index
Prospera OS provides seven core operation templates:

T1 Task Execution Template
T2 Conversation Execution Template
T3 Pipeline Execution Template
T4 Optimization Execution Template
T5 System Self-Check Template
T6 Governance Compliance Template
T7 Autonomy Invocation Template

Each template must be used by the Execution Engine and Pipeline Engine during all operations.

Template Definitions

T1 Task Execution Template
Used for any user-initiated or system-initiated task.

Step 1 Intake
Validate identity, project, phase, and intent.
Normalize input.

Step 2 Planning
Identify required engines.
Construct execution-plan.
Check governance boundaries.

Step 3 Execution
Run task step-by-step.
No skipping allowed.

Step 4 Validation
Run safety-validation.
Run governance-validation.

Step 5 Writeback
Commit state via Pipeline.
Log changes immutably.

Step 6 Output
Return final output to user or module.

T2 Conversation Execution Template
Used for conversations, iterations, and multi-turn tasks.

Step 1 Retrieve session state
Step 2 Apply identity + intent alignment
Step 3 Maintain topic and phase constraints
Step 4 Execute requested action
Step 5 Validate
Step 6 Pipeline writeback
Step 7 Title Correction Engine finalizes title

T3 Pipeline Execution Template
Used for all data flows.

Phase 1 Intake (schema validation)
Phase 2 Processing (routing + normalization)
Phase 3 Validation (Safety + Governance)
Phase 4 Writeback (SSOT + session state)

Forbidden: pipeline bypass.

T4 Optimization Execution Template
Used for system optimization, cleanup, and boundary correction.

Step 1 Identify optimization-scope
Step 2 Validate governance permissions
Step 3 Perform structure alignment
Step 4 Remove redundancy
Step 5 Correct boundaries
Step 6 Validate results
Step 7 Log via Pipeline
Step 8 Optional SSOT writeback (Mode B)

T5 System Self-Check Template
Used for health diagnostics.

Check identity-integrity
Check intent-integrity
Check pipeline-state
Check engine-health
Check governance-flags
Check SSOT-continuity
Log results

If fail → trigger Recovery or Autonomy.

T6 Governance Compliance Template
Used before any high-risk action.

Step 1 Validate authority scope
Step 2 Check G-Law
Step 3 Check Safety rules
Step 4 Check boundary rules
Step 5 Produce governance-approval packet
Step 6 Continue or block execution

T7 Autonomy Invocation Template
Used when autonomy is triggered manually or automatically.

Step 1 Validate autonomy-request
Step 2 Confirm governance permission
Step 3 Build autonomy-plan
Step 4 Execute via Execution Engine
Step 5 Validate via Safety + Governance
Step 6 Log via Pipeline
Step 7 Writeback (Mode A/B)

Forbidden: autonomy self-modification.

Enforcement
All operation templates are enforced by:

Execution Engine
Safety Engine
Governance Layer
Pipeline Engine
SSOT Validation

Violations trigger Matrix-Block or Matrix-Escalation.

Versioning
v1.0 Initial operational templates
v1.1 Expanded task templates
v2.x Adaptive template selection

File Location
system/operations/templates/operation-templates-v1.0.md
