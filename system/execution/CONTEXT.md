# Execution Context — Prospera OS

This document defines the mandatory Execution Context required for any governed execution
within Prospera OS.

No execution may occur without a valid, active Execution Context.

---

## Purpose

The Execution Context binds authority, scope, and control into a single runtime construct.

It exists to ensure that execution:
- Is explicitly authorized
- Is scope-limited
- Is time-bounded
- Is interruptible
- Cannot escalate its own authority

---

## Required Context Fields

Every execution MUST be associated with a context containing the following fields:

- authority_ref
  Reference to the authorizing document or decision
  (e.g. governance canon, control approval, human authorization)

- scope
  Explicit definition of what the execution MAY do
  Any action outside scope is forbidden

- duration
  Time-bound validity of the execution
  Execution MUST terminate when duration expires

- interrupt_handle
  Mechanism by which execution can be paused or terminated
  Must be available at all times

- escalation_policy
  Defines what happens when execution encounters uncertainty or conflict
  Default behavior: pause and escalate

---

## Enforcement Rules

- Execution without context is invalid
- Context fields may NOT be modified by the execution itself
- Any violation of context constraints MUST trigger interruption
- No execution may create or extend its own context

---

## Authority Relationship

The Execution Context is subordinate to:

1. Governance Layer
2. Control Layer
3. Execution Entry Point

The Execution Context authorizes execution,
but does not define authority.

---

## Failure Mode

Failing safely is mandatory.

If context validation fails at any point:
- Execution MUST stop
- State MUST be preserved
- Escalation MUST occur

---

## Binding Statement

Any system component executing without a valid Execution Context
is non-compliant with Prospera OS.

Execution exists to obey context.
Context exists to protect authority.
