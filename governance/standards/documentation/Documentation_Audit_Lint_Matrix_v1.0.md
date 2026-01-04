Document Title
Documentation Audit Checklist / Lint Matrix

Document Type
Governance Enforcement Standard

Status
Canonical

Version
v1.0

Date
2026-01-06

Owner / Maintained by
Prospera Architecture Group

Governing Authority
Prospera OS Governance Kernel

Purpose
This document defines enforceable, machine-verifiable documentation audit rules for all Prospera OS repositories.

It establishes a deterministic linting matrix that enables automated validation, classification, and enforcement of documentation quality and governance compliance.

Scope
This standard applies to all Markdown documentation files across the repository.

Included assets encompass governance, architecture, system, engine, module, and client-facing documentation.

Excluded assets include binary files and explicitly declared non-canonical artifacts.

Enforcement Model
Documentation audits MUST be executed via automated CI pipelines.

Violations SHALL be classified as BLOCKER, ERROR, or WARNING.

BLOCKER and ERROR violations MUST fail the CI execution.

WARNING violations MAY pass CI but MUST be reported.

Mandatory Document Header Rules
Each documentation file MUST include the following header fields in the specified order.

| Field | Requirement |
|------|------------|
| Document Title | MUST exist |
| Document Type | MUST exist |
| Status | MUST exist |
| Version | MUST exist |
| Date | MUST exist |
| Owner / Maintained by | MUST exist |
| Governing Authority | MUST exist |

Missing any mandatory header field is classified as a BLOCKER.

Formatting Rules
Bullet Point Spacing

- Each bullet point MUST be followed by exactly one blank line.

- Additional blank lines between bullet points are PROHIBITED.

Header Spacing

- No blank line is permitted immediately after a header.

- Content MUST begin directly on the line following the header.

Excessive Blank Lines

- More than one consecutive blank line is PROHIBITED.

Table Integrity Rules
All tables MUST use standard Markdown pipe syntax.

All rows in a table MUST have an identical number of columns.

Header separators MUST align with the column count.

Language and Modality Rules
All normative statements MUST use explicit normative language.

Permitted terms include MUST, SHALL, MUST NOT, and PROHIBITED.

Speculative or advisory terms including should, could, may, or might are PROHIBITED.

Traceability Rules
All governance documentation MUST reference a governing authority.

Orphaned documentation without governance linkage is PROHIBITED.

Audit Output Requirements
Each audit execution MUST generate a report containing:

- Total number of files scanned.

- Violations grouped by severity.

- File path and line number for each violation.

- Associated rule identifier.

Change Control
Any modification to this document MUST increment the version number.

All changes MUST be reviewed under Prospera OS governance authority.

End of Document
