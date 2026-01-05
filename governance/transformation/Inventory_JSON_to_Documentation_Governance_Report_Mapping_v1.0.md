Inventory JSON → Documentation Governance Report
Transformation Mapping Specification v1.0

Document Title
Inventory JSON to Documentation Governance Report Mapping Specification

Document Type
Governance Data Transformation Specification

Status
Canonical

Version
v1.0

Date
2026-01-07

Owner / Maintained by
Prospera Architecture Group

Governing Authority
Prospera OS Governance Kernel

Purpose

This specification defines the deterministic transformation rules that map
machine-generated documentation inventory data into the client-facing
Documentation Governance Report v1.0.

The objective is to ensure that all reported client metrics are:

Directly traceable to inventory artifacts

Machine-derivable without manual interpretation

Consistent across repositories and assessment runs

This specification prohibits subjective inference or data mutation.

Source Artifact Definition
Inventory Input

Source File
documentation-inventory-report.json

Canonical Structure (Required)
{
  "total_files": <integer>,
  "inventory": [
    {
      "file_path": <string>,
      "file_name": <string>,
      "has_document_title": <boolean>,
      "has_document_type": <boolean>,
      "has_version": <boolean>,
      "has_end_marker": <boolean>
    }
  ]
}
Any deviation from this structure invalidates transformation.

Target Artifact Definition
Client Report

Target Document
Documentation_Governance_Report_v1.0_Client.md

Transformation Output
Structured values injected into fixed report sections.

Section-Level Mapping Matrix
Section 1. Executive Summary
| Report Field                    | JSON Source | Transformation Rule                   |
| ------------------------------- | ----------- | ------------------------------------- |
| Total documents scanned         | total_files | Direct mapping                        |
| Governance-compliant documents  | inventory[] | Count where all required flags = true |
| Documents requiring remediation | inventory[] | total_files − compliant_count         |
Compliance Definition
A document is considered compliant only if:

has_document_title = true

has_document_type = true

has_version = true

has_end_marker = true

Section 2. Governance Health Snapshot
| Metric                | JSON Source | Calculation                           |
| --------------------- | ----------- | ------------------------------------- |
| Compliance percentage | inventory[] | (compliant_count / total_files) × 100 |
Health Level Mapping

Green: ≥ 80%

Yellow: 50%–79%

Red: < 50%

Thresholds are governed and MUST NOT be altered locally.

Section 3. Key Findings

Findings are grouped by missing governance attributes.
| Finding Category       | JSON Condition             | Count Rule        |
| ---------------------- | -------------------------- | ----------------- |
| Missing Document Title | has_document_title = false | Count occurrences |
| Missing Document Type  | has_document_type = false  | Count occurrences |
| Missing Version        | has_version = false        | Count occurrences |
| Missing End Marker     | has_end_marker = false     | Count occurrences |
Impact Level Assignment

High: > 20% of total_files

Medium: 5%–20%

Low: < 5%

Section 4. Governance Risk Assessment

Risk classification is derived, not subjective.
| Risk Level  | Condition                              |
| ----------- | -------------------------------------- |
| High Risk   | Any High impact finding exists         |
| Medium Risk | No High, but ≥ 1 Medium impact finding |
| Low Risk    | Only Low impact findings               |

Section 5. Remediation Prioritization (Advisory)
This section is rule-driven and non-prescriptive.
| Phase   | Trigger Condition                         |
| ------- | ----------------------------------------- |
| Phase 1 | Missing Document Title or Version present |
| Phase 2 | Missing End Marker dominant               |
| Phase 3 | Compliance < 80% after Phase 1 & 2        |

Section 6. Governance Maturity Interpretation

Maturity is derived from compliance percentage.
| Maturity Level    | Condition       |
| ----------------- | --------------- |
| Initial           | < 40% compliant |
| Managed           | 40%–59%         |
| Governed          | 60%–79%         |
| Institutionalized | ≥ 80%           |

Section 7. Next Governance Actions

Actions are condition-triggered templates.
| Condition        | Suggested Action                |
| ---------------- | ------------------------------- |
| Compliance < 50% | Approve remediation plan        |
| Any High Risk    | Schedule governance remediation |
| Compliance ≥ 80% | Enable blocking enforcement     |
This section MUST NOT include technical instructions.

Transformation Constraints

No file paths SHALL be exposed in the client report

No per-file listing SHALL be included

All numeric values MUST be derivable from JSON

No aggregation logic may be altered without version increment

Auditability Guarantees

Every reported value MUST be reproducible from inventory JSON

Transformation logic MUST be deterministic

This specification is the sole authority for JSON-to-report mapping

Change Control

Any modification requires version increment

Changes are governed by Prospera OS Governance Kernel

Backward compatibility is not guaranteed across major versions

End of Document
