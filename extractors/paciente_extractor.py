# src/extractors/paciente_extractor.py

import re
from typing import Dict, Optional
from src.utils.regex_patterns import (
    REGEX_NOMBRE,
    REGEX_IDENTIFICACION,
    REGEX_EDAD,
    REGEX_SEXO,
    REGEX_FECHA
)


def _search(pattern: str, text: str) -> Optional[str]:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def extract_paciente_data(text: str) -> Dict[str, Optional[str]]:
    """
    Extrae información básica del paciente desde texto OCR.
    """
    data = {
        "nombre": _search(REGEX_NOMBRE, text),
        "identificacion": _search(REGEX_IDENTIFICACION, text),
        "edad": _search(REGEX_EDAD, text),
        "sexo": _search(REGEX_SEXO, text),
        "fecha_ingreso": _search(REGEX_FECHA, text),
    }

    return data
