OCR Document Intelligence Platform

Automated OCR processing pipeline for extracting, normalizing, and structuring payroll data from multi-format payslip documents.

Overview

OCR Document Intelligence Platform is a Python-based document processing system designed to convert OCR outputs into structured, analytics-ready datasets.

The platform integrates Google Document AI with custom layout-aware parsing algorithms to support payroll documents originating from multiple employers, years, and document layouts.

The project focuses on reliable extraction of payroll information while maintaining a unified output structure regardless of the original document format.

⸻

Key Features

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

⸻

Technology Stack

* Python
* Pandas
* Google Document AI
* JSON / CSV
* Regular Expressions
* ETL
* Data Processing
* Document Analysis
* Linux
* REST APIs

⸻

Project Architecture

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

⸻

Current Capabilities

* Supports multiple payroll layouts
* Layout-aware parsing using OCR coordinates
* Automatic field normalization
* Duplicate detection
* Structured exports
* Modular extraction pipeline

⸻

Repository Structure

src/
    extractors/
    pipeline.py
    exporter.py
    template_loader.py
tools/
docs/
config/
sample_data/
sample_output/

⸻

Future Improvements

* Additional payroll layouts
* Machine-learning assisted layout classification
* Confidence scoring
* REST API interface
* Docker deployment
* Automated testing

⸻

Author

Eugen Rovner

Data Analyst | Python Automation | OCR & Document Intelligence | SQL | Business Intelligence
