# src/billing/cups_mapper.py

from typing import List, Dict

# Mapeo básico palabra clave → código CUPS
CUPS_MAP = {
    # Procedimientos
    "biopsia": "901201",
    "cateter venoso central": "389501",
    "intubacion": "960401",
    "ventilacion mecanica": "939601",
    "toracocentesis": "340201",
    "transfusion": "990101",
    "sonda vesical": "570101",
    "sonda orogastrica": "960201",

    # Laboratorios
    "hemograma": "902210",
    "hemocultivo": "902305",
    "gases arteriales": "902409",
    "creatinina": "902030",
    "bun": "902031",

    # Imágenes
    "tac": "879201",
    "tomografia": "879201",
    "radiografia": "870101",
    "ecografia": "881201",
    "ecocardiograma": "889101",
}


def map_to_cups(items: List[Dict], field_name: str) -> List[Dict]:
    """
    Asigna código CUPS a cada item encontrado.
    field_name: nombre del campo que contiene la palabra clave
                (ej: 'procedimiento', 'laboratorio', 'estudio_imagen')
    """
    mapped = []

    for item in items:
        keyword = item.get(field_name, "").lower()
        cups_code = CUPS_MAP.get(keyword)

        enriched_item = item.copy()
        enriched_item["cups_codigo"] = cups_code

        mapped.append(enriched_item)

    return mapped
