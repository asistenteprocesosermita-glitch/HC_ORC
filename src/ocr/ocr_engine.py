# src/ocr/ocr_engine.py

import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io
from config.settings import OCR_LANGUAGE, OCR_DPI, OCR_PSM

# Si necesitas ruta explícita en Windows:
# from config.settings import TESSERACT_CMD
# pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


def pdf_to_images(pdf_bytes: bytes) -> list:
    """
    Convierte PDF (bytes) a lista de imágenes PIL.
    """
    images = convert_from_bytes(pdf_bytes, dpi=OCR_DPI)
    return images


def image_bytes_to_pil(image_bytes: bytes) -> Image.Image:
    """
    Convierte bytes de imagen a objeto PIL.
    """
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")


def image_to_text(image: Image.Image) -> str:
    """
    Ejecuta OCR sobre una imagen PIL.
    """
    config = f"--psm {OCR_PSM}"
    text = pytesseract.image_to_string(
        image,
        lang=OCR_LANGUAGE,
        config=config
    )
    return text


def images_to_text(images: list) -> str:
    """
    Ejecuta OCR sobre múltiples imágenes y concatena el texto.
    """
    full_text = []
    for img in images:
        text = image_to_text(img)
        full_text.append(text)
    return "\n\n".join(full_text)


def process_file(file_bytes: bytes, file_type: str) -> str:
    """
    Procesa archivo PDF o imagen y devuelve texto OCR completo.
    """
    if file_type == "application/pdf":
        images = pdf_to_images(file_bytes)
    else:
        image = image_bytes_to_pil(file_bytes)
        images = [image]

    return images_to_text(images)
