"""
OCR Document Intelligence Platform

Batch processing engine.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from pipeline import OCRPipeline


class BatchProcessor:
    """
    Coordinates batch processing of OCR documents.

    Responsibilities:
        - Discover new OCR JSON files
        - Execute OCR pipeline
        - Collect processed documents
        - Merge results
        - Return analytics-ready dataset
    """

    def __init__(self, input_directory: str | Path):
        self.input_directory = Path(input_directory)

        self.documents: List[Path] = []
        self.results: List[Dict] = []

    def discover_documents(self) -> List[Path]:
        """Locate OCR JSON files."""
        self.documents = sorted(
            self.input_directory.glob("*.json")
        )

        return self.documents

    def process_document(self, document: Path) -> Dict:
        """Run OCR pipeline for a single document."""
        pipeline = OCRPipeline(document)

        return pipeline.run()

    def process_batch(self) -> List[Dict]:
        """Process every discovered document."""

        self.results = []

        for document in self.documents:
            result = self.process_document(document)
            self.results.append(result)

        return self.results

    def merge_results(self) -> List[Dict]:
        """
        Merge processed document outputs.

        Public repository version intentionally keeps this
        implementation lightweight.
        """
        return self.results

    def run(self) -> List[Dict]:
        """Execute complete batch workflow."""

        self.discover_documents()
        self.process_batch()

        return self.merge_results()
