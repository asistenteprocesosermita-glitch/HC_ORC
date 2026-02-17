# src/billing/facturacion_validator.py

from typing import List, Dict


def validar_items_con_cups(items: List[Dict]) -> List[Dict]:
    """
    Marca cada item como facturable o no dependiendo
    si tiene código CUPS asignado.
    """
    validated = []

    for item in items:
        cups_code = item.get("cups_codigo")

        enriched = item.copy()
        enriched["facturable"] = bool(cups_code)

        validated.append(enriched)

    return validated


def consolidar_facturacion(
    procedimientos: List[Dict],
    laboratorios: List[Dict],
    imagenes: List[Dict]
) -> List[Dict]:
    """
    Consolida todos los items facturables en una sola lista.
    """
    all_items = procedimientos + laboratorios + imagenes
    facturables = [item for item in all_items if item.get("facturable")]

    return facturables
