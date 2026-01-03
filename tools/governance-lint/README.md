Prospera OS
Governance Lint Tool – Audit-Only Declaration

Version: v1.0
Status: Active
Date: 2026-01-03
Owner: Prospera Architecture Group
Scope: tools/governance-lint
Authority: Subordinate (Audit-Only)

Purpose

This document formally defines the operational boundaries of the
governance-lint tool within Prospera OS.

governance-lint exists solely as an audit and reporting mechanism.
It does not possess authority to modify, delete, rename, or normalize
any repository content.

Operational Mode

governance-lint operates in audit-only mode.

The tool may:

Scan files and directories

Detect deviations from Canonical definitions

Report violations and inconsistencies

Produce non-mutating audit logs

The tool may not:

Modify files or directories

Delete or rename content

Rewrite filenames or paths

Apply automated fixes

Interpret Canonical intent

Authority Boundary

governance-lint is subordinate to:

SYSTEM_INDEX.md

Canonical Governance Documents

Canonical Filename and Path Mapping

In case of conflict, governance-lint must defer and report.
It must never attempt remediation.

Change Control

Any change to governance-lint behavior requires:

Human-authored code changes

Explicit Architecture Group approval

Verification against Canonical governance documents

Self-modifying or self-healing behavior is prohibited.

Enforcement Principle

governance-lint enforces governance visibility, not governance action.

End of Document
