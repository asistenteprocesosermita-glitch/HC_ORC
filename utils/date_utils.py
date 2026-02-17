# src/utils/date_utils.py

import re
from datetime import datetime
from typing import Optional, List


DATE_PATTERNS = [
    r"\d{1,2}/\d{1,2}/\d{2,4}",
    r"\d{1,2}-\d{1,2}-\d{2,4}",
    r"\d{4}-\d{1,2}-\d{1,2}",
]


def extract_dates(text: str) -> List[str]:
    """
    Extrae todas las fechas encontradas en el texto.
    """
    dates = []

    for pattern in DATE_PATTERNS:
        matches = re.findall(pattern, text)
        dates.extend(matches)

    return list(set(dates))


def parse_date(date_str: str) -> Optional[datetime]:
    """
    Convierte string a objeto datetime si el formato es válido.
    """
    formats = [
        "%d/%m/%Y",
        "%d/%m/%y",
        "%d-%m-%Y",
        "%d-%m-%y",
        "%Y-%m-%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return None


def calculate_days_between(start_date: str, end_date: str) -> Optional[int]:
    """
    Calcula diferencia en días entre dos fechas.
    """
    start = parse_date(start_date)
    end = parse_date(end_date)

    if start and end:
        return (end - start).days

    return None
