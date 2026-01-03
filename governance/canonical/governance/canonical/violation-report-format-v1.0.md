Prospera OS
Canonical Violation Report Format

Version: v1.0
Status: Draft – Governance Freeze Candidate
Date: 2026-01-03
Owner: Prospera Architecture Group
Scope: Repository-wide
Authority: Canonical (Non-Overridable)

Purpose

This document defines the canonical format for reporting governance and
canonical violations within the Prospera OS repository.

All tools, CI pipelines, and AI-assisted processes MUST use this format
when detecting, reporting, or escalating violations against Canonical
governance definitions.

This format standardizes violation visibility, auditability, and
decision-making. It does not authorize automated remediation.

Applicability

This format applies to violations related to, but not limited to:

Canonical filename and path rules

Canonical governance scope declarations

SYSTEM_INDEX.md references

Authority boundary breaches

Tooling behavior exceeding assigned authority

Violation reports are informational artifacts. They do not enact changes.

Violation Severity Levels

Violations MUST be classified using one of the following severity levels:

P0 – Canonical Violation
Non-overridable breach of Canonical governance.
Immediate human review required.

P1 – Governance Violation
Breach of governance rules not classified as Canonical.
Human review required prior to merge.

P2 – Structural Deviation
Deviation from recommended structure or conventions.
Review recommended.

P3 – Informational
Non-blocking observation or advisory note.

Canonical Violation Report Structure

All violation reports MUST conform to the following structure.

Report Header

Report-ID:
Unique identifier for the violation report.

Detected-By:
Tool, CI job, or human actor generating the report.

Detection-Timestamp:
ISO 8601 timestamp of detection.

Severity:
P0, P1, P2, or P3.

Canonical-Reference:
Canonical document(s) violated.

Affected-Path:
Exact file or directory path.

Violation Summary

Concise description of the violation.
No interpretation or remediation instructions allowed.

Violation Details

Objective description of the detected condition.
No speculative language.
No automated judgment.

Expected Canonical State

Description of the expected state as defined by Canonical governance.

Observed State

Description of the observed non-compliant state.

Impact Assessment

High-level assessment of potential governance impact.
No execution decisions permitted.

Recommended Action

Human-actionable recommendation.
Must not include automated remediation.

Escalation Path

Defined escalation authority based on severity:

P0:
Architecture Group

P1:
Governance Review

P2:
Maintainer Discretion

P3:
No escalation required

Authority Boundary

Violation reports do not modify repository state.

Tools, automation, and AI agents generating reports:

May detect and describe violations

May reference Canonical documents

May recommend human actions

They may not:

Apply fixes

Rename or delete files

Alter Canonical content

Override governance decisions

Relationship to Other Governance Artifacts

This document is subordinate to:

SYSTEM_INDEX.md

governance/canonical/README.md

governance/canonical/filename-and-path-mapping-v1.0.md

In case of conflict, resolution flows strictly top-down.

End of Document
