# src/ocr/pdf_processor.py

from pdf2image import convert_from_bytes
from PIL import Image
from typing import List
import io
from config.settings import OCR_DPI


def pdf_to_images(pdf_bytes: bytes) -> List[Image.Image]:
    """
    Convierte un PDF en memoria (bytes) a una lista de imágenes PIL.
    """
    images = convert_from_bytes(
        pdf_bytes,
        dpi=OCR_DPI,
        fmt="jpeg"
    )
    return images


def extract_images_from_pdf(pdf_bytes: bytes) -> List[bytes]:
    """
    Convierte cada página del PDF a bytes (JPEG).
    """
    pil_images = pdf_to_images(pdf_bytes)
    image_bytes_list = []

    for img in pil_images:
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        image_bytes_list.append(buffer.getvalue())

    return image_bytes_list


def get_pdf_page_count(pdf_bytes: bytes) -> int:
    """
    Retorna el número de páginas del PDF.
    """
    images = convert_from_bytes(pdf_bytes, dpi=50)
    return len(images)
