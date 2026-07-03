"""
OCR Document Intelligence Platform

Position-aware OCR extraction utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class OCRLine:
    """
    Represents one OCR text element together
    with its normalized position.
    """

    text: str
    x: float
    y: float


class PositionExtractor:
    """
    Utilities for working with OCR coordinates.

    This component reconstructs document layout
    using positional information rather than
    relying solely on text recognition.
    """

    def __init__(self, tolerance: float = 0.006):
        self.tolerance = tolerance

    def extract_lines(
        self,
        document: Dict,
    ) -> List[OCRLine]:
        """
        Convert OCR document into positioned lines.

        Placeholder implementation.
        """

        return []

    def group_by_rows(
        self,
        lines: List[OCRLine],
    ) -> List[List[OCRLine]]:
        """
        Group nearby OCR elements
        into logical document rows.
        """

        rows: List[List[OCRLine]] = []

        for line in sorted(lines, key=lambda item: item.y):

            if not rows:
                rows.append([line])
                continue

            last_row = rows[-1]

            if abs(last_row[0].y - line.y) <= self.tolerance:
                last_row.append(line)
            else:
                rows.append([line])

        return rows

    def find_nearest(
        self,
        lines: List[OCRLine],
        x: float,
        y: float,
    ) -> Optional[OCRLine]:
        """
        Locate the nearest OCR element
        to a given coordinate.
        """

        if not lines:
            return None

        return min(
            lines,
            key=lambda item:
            abs(item.x - x) + abs(item.y - y),
        )
