"""
OCR Document Intelligence Platform

Export services.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


class Exporter:
    """
    Handles exporting processed OCR results
    into multiple output formats.
    """

    def __init__(self, output_directory: str | Path):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def export_json(
        self,
        filename: str,
        document: Dict[str, Any],
    ) -> Path:
        """
        Export processed document as JSON.
        """

        output_path = self.output_directory / f"{filename}.json"

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(
                document,
                file,
                indent=2,
                ensure_ascii=False,
            )

        return output_path

    def export_csv(
        self,
        filename: str,
        rows: List[Dict[str, Any]],
    ) -> Path:
        """
        Export extracted rows as CSV.
        """

        dataframe = pd.DataFrame(rows)

        output_path = self.output_directory / f"{filename}.csv"

        dataframe.to_csv(
            output_path,
            index=False,
            encoding="utf-8-sig",
        )

        return output_path

    def export_document(
        self,
        filename: str,
        document: Dict[str, Any],
        rows: List[Dict[str, Any]],
    ) -> Dict[str, Path]:
        """
        Export all supported output formats.
        """

        return {
            "json": self.export_json(filename, document),
            "csv": self.export_csv(filename, rows),
        }
