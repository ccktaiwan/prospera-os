# Prospera OS  
Canonical Filename and Path Mapping  

Version: v1.0  
Status: Draft – Governance Freeze Candidate  
Date: 2026-01-03  
Owner: Prospera Architecture Group  
Scope: Repository-wide  
Authority: Canonical (Non-Overridable)

This document defines the canonical and authoritative mapping between legacy filenames/paths and their normalized canonical counterparts in Prospera OS.

This mapping is mandatory, versioned, and append-only.
All refactors, tools, CI pipelines, and AI agents MUST comply with this mapping.

---

## Canonical Mapping Table

### System / Safety

| Legacy Path | Canonical Path |
|------------|----------------|
| system/safety/routing-safety-spec-v1.0.md | system/safety/spec/routing-safety/v1.0.md |
| system/safety/safety-architecture-v1.0.md | system/safety/architecture/safety/v1.0.md |
| system/safety/safety-engine-spec-v1.0.md | system/safety/spec/safety-engine/v1.0.md |
| system/safety/safety-integration-protocol-v1.0.md | system/safety/protocol/safety-integration/v1.0.md |
| system/safety/safety-system-v1.0.md | system/safety/system/safety/v1.0.md |
| system/safety/safety-system-v1.2.md | system/safety/system/safety/v1.2.md |

---

### System / SSOT

| Legacy Path | Canonical Path |
|------------|----------------|
| system/ssot/ssot-integrity-protocol-v1.0.md | system/ssot/protocol/integrity/v1.0.md |
| system/ssot/ssot-spec-v1.0.md | system/ssot/spec/core/v1.0.md |

---

### System / Core

| Legacy Path | Canonical Path |
|------------|----------------|
| system/system-master-specification-v1.0.md | system/core/spec/master/v1.0.md |
| system/system-readiness-checklist-v1.0.md | system/core/checklist/readiness/v1.0.md |
| system/system-spec-v1.0.md | system/core/spec/system/v1.0.md |

---

### Templates

| Legacy Path | Canonical Path |
|------------|----------------|
| system/template/output-format-spec-v1.0.md | system/template/spec/output-format/v1.0.md |
| system/template/style-tone-enforcement-protocol-v1.0.md | system/template/protocol/style-tone/v1.0.md |
| system/template/template-engine-spec-v1.0.md | system/template/spec/engine/v1.0.md |

---

### User Modeling

| Legacy Path | Canonical Path |
|------------|----------------|
| system/user-modeling-system-spec-v1.2.md | system/user-modeling/system/spec/v1.2.md |
| system/user-modeling/engine-spec-v1.0.md | system/user-modeling/engine/spec/v1.0.md |
| system/user-modeling/user-context-safety-spec-v1.0.md | system/user-modeling/context/safety/v1.0.md |
| system/user-modeling/user-context-state-machine-v1.0.md | system/user-modeling/context/state-machine/v1.0.md |
| system/user-modeling/user-modeling-architecture-v1.0.md | system/user-modeling/architecture/core/v1.0.md |
| system/user-modeling/user-modeling-system-v1.0.md | system/user-modeling/system/spec/v1.0.md |
| system/user-modeling/user-modeling-system-v1.2.md | system/user-modeling/system/spec/v1.2.md |
| system/user-modeling/user-traits-spec-v1.0.md | system/user-modeling/traits/spec/v1.0.md |

---

### Whitepapers

| Legacy Path | Canonical Path |
|------------|----------------|
| system/whitepapers/ai-as-engineering-worker-whitepaper.md | system/whitepaper/ai-engineering-worker/v1.0.md |

---

### Tools / Governance

| Legacy Path | Canonical Path |
|------------|----------------|
| tools/governance-lint/lint_and_fix.py | tools/governance/lint/engine/v1.0.py |

---

## Illegal or Non-Canonical Paths

Any file or directory containing:

- Non-ASCII characters
- Shell-escaped byte sequences
- Natural language sentences
- Platform-incompatible symbols

is classified as **P0 Governance Violation** and MUST be migrated or removed according to this mapping before any further development.

---

## Governance Authority

This document is a **Canonical Governance Artifact**.

- It may not be modified retroactively
- Future changes require a new version (v1.1, v2.0, etc.)
- All tooling, refactors, and AI-assisted operations MUST reference this document

Absence of a mapping implies prohibition.

---

End of Document
