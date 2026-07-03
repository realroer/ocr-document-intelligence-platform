# OCR Document Intelligence Platform

> Automated OCR processing pipeline for extracting, normalizing, and structuring payroll data from multi-format payslip documents.

## Overview

OCR Document Intelligence Platform is a Python-based document processing system designed to convert OCR outputs into structured, analytics-ready datasets.

The platform integrates Google Document AI with custom layout-aware parsing algorithms to support payroll documents originating from multiple employers, years, and document layouts.

The project focuses on reliable extraction of payroll information while maintaining a unified output structure regardless of the original document format.

---

## Business Value

This project demonstrates the development of a production-oriented OCR processing platform 
capable of transforming unstructured payroll documents into standardized datasets suitable for reporting, 
analytics, and downstream business systems.

---

## Key Features

* Automated OCR document processing
* Google Document AI integration
* Multi-layout payslip recognition
* Layout-aware text parsing
* Employee and employer information extraction
* Salary payments extraction
* Mandatory and voluntary deductions extraction
* Pension and insurance contributions
* Vacation and sick leave accumulators
* Net salary calculations
* JSON and CSV export
* Duplicate detection
* Master dataset consolidation
* Modular extraction architecture

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas |
| OCR | Google Document AI |
| Formats | JSON, CSV |
| Techniques | ETL, OCR, Document Analysis |
| Infrastructure | Linux |
| Integration | REST APIs |

---

## Project Architecture

```text
Incoming OCR JSON
        │
        ▼
Document Classification
        │
        ▼
Layout Detection
        │
        ▼
Field Extraction
        │
        ▼
Normalization
        │
        ▼
Validation
        │
        ▼
JSON / CSV Export
        │
        ▼
Master Dataset
```

---

## Current Capabilities

* Supports multiple payroll layouts
* Layout-aware parsing using OCR coordinates
* Automatic field normalization
* Duplicate detection
* Structured exports
* Modular extraction pipeline

---

## Repository Structure

```text
src/
├── extractors/
│   ├── deductions.py
│  └── position_extractor.py
├── batch_processor.py
├─exporter.py
├─field_mapping.py
├─main.py
├─pipeline.py
├─template_loader.py

docs/
├── architecture.md
└── roadmap.md

tools/
└── inspect_raw_json.py

requirements.txt
README.md
LICENSE
```

---

## Future Improvements

* Additional payroll layouts
* Machine-learning assisted layout classification
* Confidence scoring
* REST API interface
* Docker deployment
* Automated testing

---

## Author

**Eugen Rovner**

Data Analyst | Python Automation | OCR & Document Intelligence | SQL | Business Intelligence
