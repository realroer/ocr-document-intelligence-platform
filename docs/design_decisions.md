# Design Decisions

## Overview

OCR Document Intelligence Platform was designed as a modular document processing system rather than a single monolithic parser.

The primary engineering goal is to separate document processing into independent components that can evolve without affecting the entire pipeline.

---

# Why Position-Based Parsing?

Traditional OCR processing often relies exclusively on regular expressions.

Although regex-based extraction works for simple documents, payroll documents frequently contain:

- multiple layouts
- inconsistent spacing
- OCR recognition variations
- different employer templates

Instead of depending solely on textual patterns, this platform uses document coordinates as an additional source of information.

Position-aware extraction makes the parsing process significantly more robust when processing heterogeneous document layouts.

---

# Why Modular Extractors?

Each logical document section has different extraction rules.

Instead of one large parser, extraction logic is separated into dedicated components.

Examples include:

- Position Extractor
- Payroll Deduction Extractor
- Template Loader

This architecture improves readability, maintainability and future extensibility.

---

# Why Template-Based Normalization?

Payroll terminology varies between employers.

The platform therefore separates extraction from normalization.

Extracted values are mapped into standardized field definitions using configurable templates.

This approach allows new layouts to be supported with minimal code changes.

---

# Why Batch Processing?

Real-world payroll processing rarely involves a single document.

The platform supports batch-oriented workflows to simplify large-scale document processing and downstream analytics.

---

# Why Multiple Export Formats?

The platform exports structured data as both JSON and CSV.

JSON preserves document structure for software integration.

CSV enables immediate use in spreadsheet software, BI platforms and data analysis workflows.

---

# Engineering Philosophy

The repository emphasizes:

- modular architecture
- maintainable code
- reusable components
- separation of responsibilities
- extensibility

This public repository intentionally focuses on software architecture and engineering concepts while excluding customer-specific implementations and proprietary business logic.
