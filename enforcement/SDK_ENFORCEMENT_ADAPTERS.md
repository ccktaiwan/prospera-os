# Prospera OS — SDK-Facing Enforcement Adapters

Status: Canonical (v1.x Extension)
Version: v1.1
Owner: Prospera Architecture Group
Scope: Stage 04 / Stage 05 External Interfaces
Authority: SYSTEM_INDEX (SSOT)

## Purpose

This document defines the canonical SDK-facing enforcement adapter contracts
used to consume governance arbitration outputs and gate execution and
generation at Stage 04 (Execution Binding) and Stage 05 (Generation Surface).

Adapters translate governance decisions into enforceable, deterministic
controls without redefining governance logic.

## Authority References

- SYSTEM_INDEX.md
- SYSTEM_MAP.md
- governance/decision-chain/SYSTEM_COORDINATES.md
- tools/governance-lint/POLICY_REPLAY_TESTS.md

In case of conflict, governance specifications take precedence.

## Design Principles

- Governance-first consumption (no reinterpretation)
- Deterministic behavior
- Idempotent enforcement
- No side effects on governance state
- Replay-safe and audit-ready

## Adapter Responsibilities

Adapters MUST:
- Consume arbitration output (PASS | BLOCK | ESCALATE)
- Enforce coordinate-aligned constraints
- Gate execution and generation
- Emit auditable enforcement events

Adapters MUST NOT:
- Modify governance rules
- Escalate privileges
- Perform autonomous decision-making

## Adapter Interface (Canonical)

### Input (Required)

- arbitration_id
- stage (Stage 04 | Stage 05)
- vertical_level (V0–V4)
- horizontal_level (H0–H4)
- decision (PASS | BLOCK | ESCALATE)
- reason_code

### Output (Deterministic)

- enforcement_action (ALLOW | DENY | ESCALATE)
- enforcement_reason (mirrors reason_code)
- audit_event_id

## Stage-Specific Enforcement

### Stage 04 — Execution Binding

- Allowed vertical: V3
- Allowed horizontal: H0–H1
- Any generation beyond H1 MUST be DENIED
- Content or inferential generation MUST be DENIED
- ESCALATE requires human approval hook

### Stage 05 — Generation Surface

- Allowed vertical: V4
- Allowed horizontal: H0
- Any generation request MUST be DENIED
- Execution proceeds deterministically only

## Error Handling

- Missing arbitration output: DENY
- Coordinate mismatch: DENY
- Replay mismatch: DENY and flag governance violation

## Audit & Replay

- Every enforcement MUST emit an audit event
- Audit events MUST be replayable without side effects
- Replay MUST yield identical enforcement outcomes

## Compatibility

This specification defines interfaces only.
SDKs, runtimes, or platforms MUST implement adapters conforming to this contract.

END OF SDK ENFORCEMENT ADAPTER SPEC
