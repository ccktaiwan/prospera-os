Title Correction Engine – Engine Definition Sheet
Version v1.0
Category Engine Specification
Location /engine/eds
Status Stable
Owner Prospera Architecture Group

Overview
Title Correction Engine analyzes the full conversation context, extracts the true central theme, and generates a corrected title that accurately reflects the core substance of the interaction.
It eliminates incorrect, misleading, or early-phase titles assigned before the conversation completes.

Purpose

Generate precise, post-conversation titles that reflect actual content.

Maintain consistency across project folders, archives, and logs.

Ensure titles follow governance naming rules.

Improve navigability and traceability of Prospera OS conversation records.

Inputs
conversation-history
intent-object
identity-object
user-model-object
governance-title-rules
title-interface-schema

Outputs
corrected-title
title-outline
title-justification
confidence-score
writeback-directive

Internal Logic Flow
Step 1 Retrieve conversation-history from Memory System
Step 2 Identify dominant intent + final task outcome
Step 3 Filter superficial early-stage topics
Step 4 Apply governance title rules and structural patterns
Step 5 Produce corrected-title + justification metadata
Step 6 Send corrected-title to Pipeline System for writeback

Constraints
May not alter conversation content
May not infer unauthorized semantic attributes
May not modify governance or kernel rules
May not call Modules directly
May not perform execution or reasoning tasks outside title domain

Failover Modes
Soft Fail: fallback to simplified-title
Hard Fail: block-title-generation
Reset: regenerate minimal title
Rebuild: produce title using governance fallback logic

Dependency Rules
Depends on Title Correction System interface
Consumes output from Intent + Memory + User Model Engines
Pipeline System handles title writeback
Safety Engine validates title compliance

Forbidden Operations
Assigning titles without justification
Cross-conversation title generation
Overriding governance naming rules
Silent failure without pipeline logging
Using partial context

Versioning
v1.0 Initial definition
v1.1 Multi-layer context extraction
v2.x Predictive topic transition modeling

File Location
engine/eds/title-correction-engine-eds-v1.0.md

【建議 Commit message】
