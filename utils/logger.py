# src/utils/date_utils.py

import re
from datetime import datetime
from typing import List, Optional

DATE_REGEX = [
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    r"\b\d{1,2}-\d{1,2}-\d{2,4}\b",
    r"\b\d{4}-\d{1,2}-\d{1,2}\b",
]

DATE_FORMATS = [
    "%d/%m/%Y",
    "%d/%m/%y",
    "%d-%m-%Y",
    "%d-%m-%y",
    "%Y-%m-%d",
]


def extract_dates(text: str) -> List[str]:
    """
    Extrae todas las fechas encontradas en el texto.
    """
    found = []
    for pattern in DATE_REGEX:
        matches = re.findall(pattern, text)
        found.extend(matches)

    return list(set(found))


def parse_date(date_str: str) -> Optional[datetime]:
    """
    Convierte string a datetime si el formato es válido.
    """
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def days_between(start_date: str, end_date: str) -> Optional[int]:
    """
    Calcula diferencia en días entre dos fechas.
    """
    start = parse_date(start_date)
    end = parse_date(end_date)

    if start and end:
        return (end - start).days

    return None


def get_first_and_last_date(text: str) -> dict:
    """
    Retorna la primera y última fecha detectada en el texto.
    """
    dates = extract_dates(text)
    parsed_dates = [parse_date(d) for d in dates if parse_date(d)]

    if not parsed_dates:
        return {"fecha_inicial": None, "fecha_final": None}

    parsed_dates.sort()

    return {
        "fecha_inicial": parsed_dates[0].strftime("%Y-%m-%d"),
        "fecha_final": parsed_dates[-1].strftime("%Y-%m-%d"),
    }
