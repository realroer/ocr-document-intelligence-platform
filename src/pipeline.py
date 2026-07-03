"""
OCR Document Intelligence Platform

Core processing pipeline for converting OCR JSON documents into
structured payroll datasets.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class OCRPipeline:
    """
    High-level OCR processing pipeline.

    This class represents the main stages of a document intelligence workflow:
    loading OCR output, detecting layout, extracting fields, normalizing data,
    validating results, and preparing structured output.
    """

    def __init__(self, document_path: str | Path, template_path: Optional[str | Path] = None) -> None:
        self.document_path = Path(document_path)
        self.template_path = Path(template_path) if template_path else None

        self.document: Dict[str, Any] = {}
        self.lines: List[str] = []
        self.layout_type: str = "UNKNOWN"
        self.header: Dict[str, Any] = {}
        self.rows: List[Dict[str, Any]] = []

    def load_document(self) -> Dict[str, Any]:
        """Load OCR JSON document from disk."""
        with self.document_path.open("r", encoding="utf-8") as file:
            self.document = json.load(file)

        return self.document

    def extract_lines(self) -> List[str]:
        """Extract plain text lines from OCR document structure."""
        text = self.document.get("text", "") or ""
        pages = self.document.get("pages", []) or []

        lines: List[str] = []

        for page in pages:
            for line in page.get("lines", []) or []:
                layout = line.get("layout", {}) or {}
                segments = (
                    layout.get("textAnchor", {}) or {}
                ).get("textSegments", []) or []

                if not segments:
                    continue

                segment = segments[0]
                start = int(segment.get("startIndex", 0) or 0)
                end = int(segment.get("endIndex", 0) or 0)

                start = max(0, min(start, len(text)))
                end = max(0, min(end, len(text)))

                if start > end:
                    start, end = end, start

                value = text[start:end].replace("\n", " ").strip()

                if value:
                    lines.append(value)

        self.lines = lines
        return lines

    def detect_layout(self) -> str:
        """
        Detect document layout.

        Portfolio version uses a placeholder rule-based detector.
        Production version can include employer-specific templates,
        layout scoring, OCR coordinate analysis, and custom heuristics.
        """
        joined_text = " ".join(self.lines)

        if "salary" in joined_text.lower() or "payroll" in joined_text.lower():
            self.layout_type = "PAYROLL_LAYOUT_GENERIC"
        else:
            self.layout_type = "UNKNOWN"

        return self.layout_type

    def extract_header(self) -> Dict[str, Any]:
        """
        Extract document-level metadata.

        Public demo uses a simplified structure to avoid exposing
        sensitive payroll identifiers.
        """
        self.header = {
            "document_name": self.document_path.name,
            "layout_type": self.layout_type,
            "source": "ocr_json",
        }

        return self.header

    def extract_fields(self) -> List[Dict[str, Any]]:
        """
        Extract payroll fields from document lines.

        This method is intentionally generic in the portfolio version.
        Real extraction modules can include payments, deductions,
        accumulators, summaries, and employee/employer metadata.
        """
        rows: List[Dict[str, Any]] = []

        for idx, line in enumerate(self.lines, start=1):
            rows.append(
                {
                    "line_number": idx,
                    "group_type": "RawLine",
                    "field_title": "OCR Line",
                    "value": line,
                    "status": "EXTRACTED",
                }
            )

        self.rows = rows
        return rows

    def normalize(self) -> List[Dict[str, Any]]:
        """Normalize extracted rows into a consistent output schema."""
        normalized_rows: List[Dict[str, Any]] = []

        for row in self.rows:
            normalized_rows.append(
                {
                    "document_name": self.header.get("document_name"),
                    "layout_type": self.header.get("layout_type"),
                    "group_type": row.get("group_type"),
                    "field_title": row.get("field_title"),
                    "value": row.get("value"),
                    "status": row.get("status"),
                }
            )

        self.rows = normalized_rows
        return normalized_rows

    def validate(self) -> List[Dict[str, Any]]:
        """Apply lightweight validation rules to extracted rows."""
        for row in self.rows:
            if not row.get("value"):
                row["status"] = "EMPTY_VALUE"

        return self.rows

    def run(self) -> Dict[str, Any]:
        """Execute the complete OCR processing pipeline."""
        self.load_document()
        self.extract_lines()
        self.detect_layout()
        self.extract_header()
        self.extract_fields()
        self.normalize()
        self.validate()

        return {
            "document": self.header,
            "rows": self.rows,
        }
