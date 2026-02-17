# config/regex_patterns.py

import re

# ---------------- IDENTIFICACIÓN PACIENTE ---------------- #

PATTERN_CC = re.compile(
    r"No\.?\s*CC[:\s]*([0-9]{6,15})",
    re.IGNORECASE
)

PATTERN_NOMBRE = re.compile(
    r"Nombre[:\s]*([A-ZÁÉÍÓÚÑ\s]{5,80})",
    re.IGNORECASE
)

PATTERN_FECHA_NACIMIENTO = re.compile(
    r"(Fecha\s*de\s*nacimiento|F\.?\s*Nac\.?)[:\s]*([0-9]{2}[/-][0-9]{2}[/-][0-9]{4})",
    re.IGNORECASE
)

PATTERN_EDAD = re.compile(
    r"Edad[:\s]*([0-9]{1,3})",
    re.IGNORECASE
)

PATTERN_EPS = re.compile(
    r"(EPS|Empresa)[:\s]*([A-ZÁÉÍÓÚÑ\s\.]{3,100})",
    re.IGNORECASE
)

# ---------------- FECHAS Y HORAS ---------------- #

PATTERN_FECHA = re.compile(
    r"\b([0-9]{2}[/-][0-9]{2}[/-][0-9]{4})\b"
)

PATTERN_FECHA_ISO = re.compile(
    r"\b([0-9]{4}-[0-9]{2}-[0-9]{2})\b"
)

PATTERN_HORA = re.compile(
    r"\b([0-9]{1,2}:[0-9]{2})\b"
)

PATTERN_FECHA_HORA = re.compile(
    r"([0-9]{2}[/-][0-9]{2}[/-][0-9]{4}).{0,20}?([0-9]{1,2}:[0-9]{2})",
    re.IGNORECASE
)

# ---------------- ESTANCIAS ---------------- #

PATTERN_INGRESO = re.compile(
    r"(Ingreso|Fecha\s*de\s*ingreso)[:\s]*([0-9]{2}[/-][0-9]{2}[/-][0-9]{4})",
    re.IGNORECASE
)

PATTERN_EGRESO = re.compile(
    r"(Egreso|Fecha\s*de\s*egreso|Salida)[:\s]*([0-9]{2}[/-][0-9]{2}[/-][0-9]{4})",
    re.IGNORECASE
)

PATTERN_SERVICIO = re.compile(
    r"(UCI|Unidad\s*de\s*Cuidados\s*Intensivos|Hospitalizaci[oó]n|Urgencias)",
    re.IGNORECASE
)

# ---------------- MEDICAMENTOS ---------------- #

PATTERN_MEDICAMENTO_LINE = re.compile(
    r"([A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s\-\/]{3,60})\s+(\d+\s?(mg|mcg|g|gr|ml|ui))\s*(IV|VO|IM|SC)?",
    re.IGNORECASE
)

PATTERN_DOSIS = re.compile(
    r"\b(\d+\.?\d*)\s?(mg|mcg|g|gr|ml|ui)\b",
    re.IGNORECASE
)

PATTERN_VIA = re.compile(
    r"\b(IV|VO|IM|SC|Subcut[aá]nea|Intravenosa|Oral)\b",
    re.IGNORECASE
)

PATTERN_INFUSION = re.compile(
    r"(infusi[oó]n\s*continua|perfusi[oó]n)",
    re.IGNORECASE
)

# ---------------- TRANSFUSIONES ---------------- #

PATTERN_TRANSFUSION = re.compile(
    r"(transfusi[oó]n|plaquetas?|GRE|gl[oó]bulos\s*rojos).*?(\d{1,3})",
    re.IGNORECASE
)

PATTERN_UNIDADES = re.compile(
    r"\b(\d{1,3})\s*(unidades?|uds?)\b",
    re.IGNORECASE
)

# ---------------- PROCEDIMIENTOS ---------------- #

PATTERN_PROCEDIMIENTO = re.compile(
    r"(biopsia|cat[eé]ter|intubaci[oó]n|ventilaci[oó]n\s*mec[aá]nica|toracocentesis|sonda\s*vesical|sonda\s*orog[aá]strica)",
    re.IGNORECASE
)

# ---------------- LABORATORIOS ---------------- #

PATTERN_LAB = re.compile(
    r"(hemograma|hemocultivo|gases\s*arteriales|tp|tpt|fibrin[oó]geno|creatinina|bun|bilirrubinas?|ldh)",
    re.IGNORECASE
)

# ---------------- IMÁGENES ---------------- #

PATTERN_IMAGEN = re.compile(
    r"(tac|tomograf[ií]a|radiograf[ií]a|ecograf[ií]a|ecocardiograma)",
    re.IGNORECASE
)

# ---------------- SOPORTE CRÍTICO ---------------- #

PATTERN_VENTILACION = re.compile(
    r"(ventilaci[oó]n\s*mec[aá]nica\s*invasiva|vmni|intubaci[oó]n)",
    re.IGNORECASE
)

PATTERN_VASOPRESOR = re.compile(
    r"(norepinefrina|noradrenalina|vasopresor)",
    re.IGNORECASE
)

PATTERN_SEDACION = re.compile(
    r"(midazolam|fentanilo|sedaci[oó]n)",
    re.IGNORECASE
)
