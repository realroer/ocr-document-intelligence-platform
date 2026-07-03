"""
OCR Document Intelligence Platform

Payroll field mapping definitions.
"""

from __future__ import annotations


class FieldMapping:
    """
    Centralized mapping definitions used during
    payroll field normalization.
    """

    PAYMENT_CODES = {
        "001": 1,
        "004": 4,
        "013": 12,
        "053": 41,
        "060": 41,
        "065": 422,
    }

    DESCRIPTION_ALIASES = {
        "ש.ב. גלובליות": "שעות נוספות גלובאליות",
        "שרי ארוחות": "שווי ארוחות",
    }

    DEDUCTION_KEYWORDS = (
        "פניקס",
        "מנורה",
        "מגדל",
        "גמל",
        "קרן",
        "קופה",
        "פנסיה",
        "ביטוח",
    )

    @classmethod
    def payment_field(cls, code: str):
        """
        Return normalized field ID for a payroll code.
        """
        return cls.PAYMENT_CODES.get(code)

    @classmethod
    def normalize_description(cls, description: str) -> str:
        """
        Normalize OCR descriptions.
        """
        return cls.DESCRIPTION_ALIASES.get(
            description,
            description,
        )

    @classmethod
    def looks_like_deduction(cls, text: str) -> bool:
        """
        Determine whether OCR text likely
        represents a deduction.
        """
        if not text:
            return False

        return any(
            keyword in text
            for keyword in cls.DEDUCTION_KEYWORDS
        )
