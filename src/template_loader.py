"""
OCR Document Intelligence Platform

Template loading utilities.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import pandas as pd


class TemplateLoader:
    """
    Loads payroll field templates and creates lookup maps used
    throughout the OCR processing pipeline.
    """

    REQUIRED_COLUMNS = [
        "groupType",
        "fieldId",
        "fieldTitle",
    ]

    def __init__(self, template_path: str | Path):
        self.template_path = Path(template_path)

    def load(self) -> pd.DataFrame:
        """
        Load template file.

        Supports CSV and TSV formats.
        """

        try:
            df = pd.read_csv(
                self.template_path,
                sep="\t",
                encoding="utf-8-sig",
            )
        except Exception:
            df = pd.read_csv(
                self.template_path,
                sep=None,
                engine="python",
                encoding="utf-8-sig",
            )

        # Handle comma-separated files detected as one column
        if len(df.columns) == 1 and "," in df.columns[0]:
            df = pd.read_csv(
                self.template_path,
                sep=",",
                encoding="utf-8-sig",
            )

        df.columns = [
            str(col).strip().strip('"').strip("'")
            for col in df.columns
        ]

        self.validate(df)

        return df

    def validate(self, dataframe: pd.DataFrame) -> None:
        """Validate required template structure."""

        missing = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required template columns: {missing}"
            )

    def build_lookup_maps(
        self,
        dataframe: pd.DataFrame,
    ) -> Tuple[Dict, Dict, Dict, Dict]:
        """
        Build lookup dictionaries used by the pipeline.
        """

        dataframe["fieldId"] = pd.to_numeric(
            dataframe["fieldId"],
            errors="coerce",
        )

        deduction_map = dict(
            zip(
                dataframe["fieldTitle"],
                dataframe["fieldId"],
            )
        )

        id_to_title = dict(
            zip(
                dataframe["fieldId"],
                dataframe["fieldTitle"],
            )
        )

        id_to_measure = dict(
            zip(
                dataframe["fieldId"],
                dataframe.get("measure", ""),
            )
        )

        return (
            deduction_map,
            {},
            id_to_title,
            id_to_measure,
        )
