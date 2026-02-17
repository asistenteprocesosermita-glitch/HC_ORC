# src/extractors/medicamentos_extractor.py

import re
from typing import List, Dict
from config.settings import MEDICAMENTOS_ALTO_COSTO


def _normalize_text(text: str) -> str:
    return text.lower()


def _extract_dosis_line(line: str) -> str:
    """
    Extrae posible dosis (ej: 1g, 500 mg, 10 ml, etc.)
    """
    pattern = r"\b\d+\s?(mg|g|mcg|ml|ui|amp|tabletas?|capsulas?)\b"
    match = re.search(pattern, line, re.IGNORECASE)
    if match:
        return match.group(0)
    return ""


def extract_medicamentos(text: str) -> List[Dict]:
    """
    Identifica medicamentos de alto costo dentro del texto OCR.
    """
    text_normalized = _normalize_text(text)
    lines = text_normalized.splitlines()

    medicamentos_encontrados = []

    for line in lines:
        for medicamento in MEDICAMENTOS_ALTO_COSTO:
            if medicamento in line:
                medicamentos_encontrados.append({
                    "medicamento": medicamento,
                    "dosis_detectada": _extract_dosis_line(line),
                    "linea_texto": line.strip()
                })

    return medicamentos_encontrados
