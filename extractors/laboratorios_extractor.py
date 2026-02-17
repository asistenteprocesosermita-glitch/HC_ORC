# src/extractors/laboratorios_extractor.py

from typing import List, Dict
from config.settings import LABORATORIOS_CLAVE


def _normalize_text(text: str) -> str:
    return text.lower()


def extract_laboratorios(text: str) -> List[Dict]:
    """
    Identifica laboratorios facturables dentro del texto OCR.
    """
    text_normalized = _normalize_text(text)
    lines = text_normalized.splitlines()

    laboratorios_encontrados = []

    for line in lines:
        for laboratorio in LABORATORIOS_CLAVE:
            if laboratorio in line:
                laboratorios_encontrados.append({
                    "laboratorio": laboratorio,
                    "linea_texto": line.strip()
                })

    return laboratorios_encontrados
