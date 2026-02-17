# src/extractors/imagenes_extractor.py

from typing import List, Dict
from config.settings import IMAGENES_CLAVE


def _normalize_text(text: str) -> str:
    return text.lower()


def extract_imagenes(text: str) -> List[Dict]:
    """
    Identifica estudios de imagen facturables dentro del texto OCR.
    """
    text_normalized = _normalize_text(text)
    lines = text_normalized.splitlines()

    imagenes_encontradas = []

    for line in lines:
        for estudio in IMAGENES_CLAVE:
            if estudio in line:
                imagenes_encontradas.append({
                    "estudio_imagen": estudio,
                    "linea_texto": line.strip()
                })

    return imagenes_encontradas
