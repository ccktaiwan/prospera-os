Prospera OS
Kernel Naming Law v1.0

File: kernel/kernel-naming-law-v1.0.md
Status: Stable
Owner: Prospera Architecture Group
Category: Kernel Specification

──────────────────────────────────

Purpose

The Kernel Naming Law defines the immutable naming conventions for all Prospera OS artifacts, including systems, engines, modules, documents, files, protocols, and internal identifiers.

The goal is to ensure absolute consistency, prevent semantic drift, eliminate naming ambiguity, and provide deterministic naming across all future extensions of Prospera OS.

No layer may override or bypass the Kernel Naming Law.

──────────────────────────────────

Scope

This law applies to naming of:

• Systems
• Engines
• Modules
• Specifications
• Protocols
• Maps
• Schemas
• Manifests
• Files
• Directories
• Execution artifacts
• Routing identifiers
• Internal state labels

All naming rules defined in this document are permanently immutable.

──────────────────────────────────

Naming Principles

3.1 Uniqueness
Every name must uniquely identify one and only one artifact.

3.2 Determinism
A name must always refer to the same meaning and function.

3.3 Non-Ambiguity
Names must not be interpretable in multiple ways.

3.4 Stability
Names cannot change across versions unless the functional definition changes.

3.5 Simplicity
Names must avoid unnecessary complexity, prefixes, or abbreviations.

3.6 Layer Separation
Names must reflect the correct OS layer.

3.7 Non-Pollution
Names from one layer may not appear in another unless explicitly required by Kernel.

3.8 Predictability
A new engineer must be able to guess the name of any component based on rules.

──────────────────────────────────

Canonical Naming Format

4.1 Systems
Format:
<name>-system
Example:
identity-system
intent-system
memory-system

4.2 Engines
Format:
Example:
identity-system
intent-system
memory-system

4.2 Engines
Format:
Example:
intent-engine
safety-engine

4.3 Modules
Format:
Example:
intent-engine
safety-engine

4.3 Modules
Format:
<platform>-module
Example:
wix-module
ga4-module
line-module

4.4 Specifications
Format:Example:
wix-module
ga4-module
line-module

4.4 Specifications
Format:
<topic>-spec-vX.Y
Example:
pipeline-architecture-spec-v1.0

4.5 Protocols
Format:
<topic>-protocol-vX.Y
Example:
phase-lock-protocol-v1.0

4.6 Maps
Format:
<topic>-map-vX.Y
Example:
engine-interaction-map-v1.0

4.7 Schemas
Format:
<topic>-schema-vX.Y
4.8 Manifests
Format:
4.8 Manifests
Format:
Example:
prospera-os-layer-spec-v1.0.md

4.10 Directory Names
Directory names must be lowercase and hyphen-separated.
Examples:
kernel
governance
system
engine
module
pipeline

──────────────────────────────────

Forbidden Naming Patterns

The following naming patterns are permanently forbidden:

5.1 Mixed Case
No CamelCase, PascalCase, or snake_case allowed.

5.2 Abbreviations
Unless globally recognized (e.g., SSOT, GA4, GSC).

5.3 Numeric Prefixes
Names must not begin with numbers.

5.4 Spaces
Spaces are permanently forbidden.

5.5 Ambiguous Names
Names that imply multiple meanings.

5.6 Cross-Layer Contamination
Examples of forbidden contamination:
• engine name used as system name
• module prefix used as system prefix
• governance names used in engine layer

5.7 Auto-Generated Random Identifiers
No UUID, random strings, hashed names unless explicitly permitted by Kernel.

──────────────────────────────────

Enforcement Mechanisms

6.1 Kernel Naming Validator
A static validator ensures all names comply with this law.

6.2 Consistency Checker
Ensures identical names refer to identical artifacts.

6.3 Governance Review
Governance audits naming during specification submission.

6.4 Drift Isolation Integration
Naming drift triggers drift isolation procedures.

6.5 SSOT Enforcement
SSOT only accepts Kernel-compliant names.

──────────────────────────────────

Compliance Requirements

7.1 Systems must use only canonical system names.
7.2 Engines must strictly follow engine format.
7.3 Modules must follow module naming rules.
7.4 All technical documents must follow naming law.
7.5 All directories and files must be Kernel-compliant.
7.6 Names must remain stable across versions.

──────────────────────────────────

Versioning

v1.x — Clarifications only (no naming changes allowed).
v2.0 — Reserved for OS-wide naming redesign (extremely rare).
v3.x — Reserved for generational OS restructuring.

Current Version: v1.0

──────────────────────────────────

File Location

kernel/kernel-naming-law-v1.0.md
