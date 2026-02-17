import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import pandas as pd
import io
import re

st.set_page_config(page_title="OCR Facturación HC", layout="wide")
st.title("OCR Facturación - Historias Clínicas")

# ---------------- OCR ---------------- #

def pdf_to_images(file_bytes):
    return convert_from_bytes(file_bytes, dpi=300)

def image_to_text(image):
    return pytesseract.image_to_string(image, lang="spa")

# ---------------- Extractores básicos ---------------- #

def extract_cc(text):
    match = re.search(r"No\.?\s*CC[:\s]*([0-9]{6,15})", text, re.IGNORECASE)
    return match.group(1) if match else None

def extract_fechas(text):
    return re.findall(r"\d{2}/\d{2}/\d{4}", text)

def extract_medicamentos(text):
    meds = []
    keywords = ["citarabina", "idarubicina", "meropenem",
                "vancomicina", "piperacilina", "filgrastim"]
    for k in keywords:
        if k in text.lower():
            meds.append(k)
    return list(set(meds))

def extract_procedimientos(text):
    procs = []
    keywords = ["biopsia", "cateter", "intubacion",
                "ventilacion mecanica", "transfusion"]
    for k in keywords:
        if k in text.lower():
            procs.append(k)
    return list(set(procs))

# ---------------- UI ---------------- #

uploaded_file = st.file_uploader("Subir PDF o Imagen", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:

    file_bytes = uploaded_file.read()

    if uploaded_file.type == "application/pdf":
        images = pdf_to_images(file_bytes)
    else:
        images = [Image.open(io.BytesIO(file_bytes))]

    full_text = ""

    with st.spinner("Procesando OCR..."):
        for img in images:
            full_text += image_to_text(img) + "\n"

    st.subheader("Texto OCR (extracto)")
    st.text_area("Contenido", full_text[:10000], height=300)

    data = {
        "cc": extract_cc(full_text),
        "fechas_detectadas": extract_fechas(full_text),
        "medicamentos_detectados": extract_medicamentos(full_text),
        "procedimientos_detectados": extract_procedimientos(full_text),
    }

    st.subheader("Campos Extraídos")
    st.json(data)

    df = pd.DataFrame([data])
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name="facturacion_extraida.csv",
        mime="text/csv",
    )
