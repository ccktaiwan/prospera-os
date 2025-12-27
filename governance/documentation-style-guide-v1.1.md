Prospera OS
Documentation Style Guide v1.1

File: governance/documentation-style-guide-v1.1.md
Status: Stable
Owner: Prospera Architecture Group
Category: Governance

──────────────────────────────────────────────

1. Purpose

This guide defines the formal documentation standards for all Prospera OS specifications.
Version 1.1 introduces:

• corrected section ordering
• consistency requirements
• cross-document alignment
• kernel-compliant metadata formatting

──────────────────────────────────────────────

2. Required Document Structure

All Prospera OS documents must follow this exact structure:
# Document Title  
File metadata block  
──────────  
1. Purpose  
2. Scope  
3. Definitions / Architecture  
4. Core Rules / Contracts  
5. System Behavior / Requirements  
6. Error Handling  
7. Compliance  
8. Security / Safety  
9. Interaction Rules  
10. Forbidden Operations  
11. Versioning  
12. File Location  
2.1 Mandatory Blank Lines

A blank line is required:

• after each major section header
• between paragraphs
• between list groups

This improves readability and diff stability.

2.2 Section Ordering Rule

Versioning must always appear before File Location.
This is mandatory starting v1.1.

──────────────────────────────────────────────

3. Metadata Block Requirements

Every file must include:
2.1 Mandatory Blank Lines

A blank line is required:

• after each major section header
• between paragraphs
• between list groups

This improves readability and diff stability.

2.2 Section Ordering Rule

Versioning must always appear before File Location.
This is mandatory starting v1.1.

──────────────────────────────────────────────

3. Metadata Block Requirements

Every file must include:
File: <path>  
Status: <Draft | Stable | Deprecated>  
Owner: <Team>  
Category: <System | Kernel | Engine | Module | Governance | Protocol | Contract>
Metadata must appear immediately after title.

──────────────────────────────────────────────

4. Language Rules

• English only
• no mixing languages
• no colloquial tone
• formal spec style, similar to IETF / ISO

──────────────────────────────────────────────

5. Naming Rules

• snake-case filenames
• vX.Y version suffix
• title-case for top-level headings
• modules, systems, and engines use exact canonical names

──────────────────────────────────────────────

6. Formatting Rules

• monospace blocks for diagrams
• no emoji
• consistent indentation
• list markers must be hyphens or numbered lists

──────────────────────────────────────────────

7. Cross-Document Consistency

All specs must obey:

• Kernel Constitutional Rules
• Kernel Boundary Specification
• Global Inter-System Contract
• Meta-Schema v1.0

──────────────────────────────────────────────

8. Compliance

Documents violating this style are considered invalid until fixed.

──────────────────────────────────────────────

9. Versioning

v1.0 initial
v1.1 updated ordering rules, added consistency constraints

──────────────────────────────────────────────

10. File Location

governance/documentation-style-guide-v1.1.md

──────────────────────────────────────────────
