# src/extractors/procedimientos_extractor.py

from typing import List, Dict
from config.settings import PROCEDIMIENTOS_CLAVE


def _normalize_text(text: str) -> str:
    return text.lower()


def extract_procedimientos(text: str) -> List[Dict]:
    """
    Identifica procedimientos facturables dentro del texto OCR.
    """
    text_normalized = _normalize_text(text)
    lines = text_normalized.splitlines()

    procedimientos_encontrados = []

    for line in lines:
        for procedimiento in PROCEDIMIENTOS_CLAVE:
            if procedimiento in line:
                procedimientos_encontrados.append({
                    "procedimiento": procedimiento,
                    "linea_texto": line.strip()
                })

    return procedimientos_encontrados
