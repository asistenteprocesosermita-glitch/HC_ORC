# src/extractors/estancias_extractor.py

import re
from typing import Dict, Optional


REGEX_DIAS_ESTANCIA = r"(\d+)\s*(dias|días)\s*(de)?\s*(hospitalizacion|hospitalización|estancia)"
REGEX_FECHA = r"(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})"


def _search(pattern: str, text: str) -> Optional[str]:
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def _search_all(pattern: str, text: str):
    return re.findall(pattern, text, re.IGNORECASE)


def extract_estancia(text: str) -> Dict:
    """
    Extrae información relacionada con días de estancia hospitalaria
    y posibles fechas de ingreso/egreso.
    """
    dias_estancia = _search(REGEX_DIAS_ESTANCIA, text)

    fechas_encontradas = _search_all(REGEX_FECHA, text)

    fecha_ingreso = fechas_encontradas[0] if len(fechas_encontradas) > 0 else None
    fecha_egreso = fechas_encontradas[1] if len(fechas_encontradas) > 1 else None

    return {
        "dias_estancia": dias_estancia,
        "fecha_ingreso": fecha_ingreso,
        "fecha_egreso": fecha_egreso
    }
