# src/utils/text_cleaner.py

import re
import unicodedata


def remove_accents(text: str) -> str:
    """
    Elimina tildes y caracteres especiales.
    """
    normalized = unicodedata.normalize("NFD", text)
    return "".join(
        char for char in normalized
        if unicodedata.category(char) != "Mn"
    )


def normalize_whitespace(text: str) -> str:
    """
    Reemplaza múltiples espacios y saltos de línea por uno solo.
    """
    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def remove_special_characters(text: str) -> str:
    """
    Elimina caracteres no alfanuméricos innecesarios
    conservando puntuación básica médica.
    """
    return re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\.\,\:\;\-\n ]", "", text)


def clean_text(text: str) -> str:
    """
    Pipeline completo de limpieza de texto OCR.
    """
    text = text.lower()
    text = remove_accents(text)
    text = remove_special_characters(text)
    text = normalize_whitespace(text)
    return text
