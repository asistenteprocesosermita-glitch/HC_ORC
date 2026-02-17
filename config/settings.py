# config/settings.py

# ---------------- APP ---------------- #

APP_NAME = "OCR Facturación HC"
APP_VERSION = "1.0.0"

# ---------------- OCR ---------------- #

OCR_LANGUAGE = "spa"
OCR_DPI = 300
OCR_PSM = 1  # Page Segmentation Mode

# Ruta opcional a tesseract (descomentar si es necesario en Windows)
# TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------- PALABRAS CLAVE FACTURABLES ---------------- #

MEDICAMENTOS_ALTO_COSTO = [
    "citarabina",
    "idarubicina",
    "meropenem",
    "vancomicina",
    "piperacilina",
    "filgrastim",
    "fluconazol",
    "aciclovir"
]

PROCEDIMIENTOS_CLAVE = [
    "biopsia",
    "cateter venoso central",
    "intubacion",
    "ventilacion mecanica",
    "toracocentesis",
    "transfusion",
    "sonda vesical",
    "sonda orogastrica"
]

LABORATORIOS_CLAVE = [
    "hemograma",
    "hemocultivo",
    "gases arteriales",
    "tp",
    "tpt",
    "fibrinogeno",
    "creatinina",
    "bun"
]

IMAGENES_CLAVE = [
    "tac",
    "tomografia",
    "radiografia",
    "ecografia",
    "ecocardiograma"
]

# ---------------- EXPORT ---------------- #

EXPORT_ENCODING = "utf-8"
EXPORT_FILENAME = "facturacion_extraida.csv"
