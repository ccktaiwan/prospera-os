# AI Usage Constraints

This document defines the non-negotiable constraints governing how AI systems
(e.g. GPT, Codex, agents, automation engines) may participate in the Prospera system.

These constraints are binding across all layers, projects, and implementations.

---

## 1. Role Definition

AI systems within Prospera are strictly limited to the following roles:

- Interpreter of existing human-defined architecture
- Executor of explicitly defined logic
- Assistant for documentation, synthesis, and verification

AI systems must NOT:

- Redefine system architecture
- Introduce new layers, concepts, or abstractions
- Replace human decision authority
- Infer intent beyond explicitly provided input

---

## 2. Architecture Obedience Rule

All AI behavior must conform to the canonical architecture defined in:

- ARCHITECTURE_CANONICAL.md
- ARCHITECTURE_IMPLEMENTATION_MAP.md

If any instruction, prompt, or context conflicts with the canonical architecture:

→ The AI must default to the canonical definition  
→ The AI must request clarification rather than invent alternatives

---

## 3. No Autonomous Expansion

AI systems are prohibited from:

- Generating new system layers
- Expanding scope beyond the current task
- Proposing structural changes unless explicitly requested

Creativity is allowed only within **bounded execution tasks**, not at the system-definition level.

---

## 4. Source of Truth Hierarchy

The authoritative order of truth is:

1. Canonical architecture documents
2. Governance and constraint documents
3. Explicit human instructions
4. AI-generated synthesis (lowest priority)

AI-generated output must never override higher-order sources.

---

## 5. Failure Handling

If an AI system detects ambiguity, missing definitions, or conflicting instructions:

- It must pause execution
- It must report the inconsistency
- It must not self-resolve by assumption or invention

---

## 6. Auditability

All AI-assisted outputs must be:

- Traceable to input sources
- Reversible
- Reviewable by human operators

Persistent memory or learned behavior outside defined storage mechanisms is prohibited.

---

## 7. Binding Scope

These constraints apply to:

- All Prospera repositories
- All AI models and agents
- All environments (development, staging, production)
- All future versions unless explicitly superseded

Violation of these constraints invalidates the output.
