# src/billing/duplicados_validator.py

from typing import List, Dict, Tuple


def eliminar_duplicados(items: List[Dict]) -> List[Dict]:
    """
    Elimina registros duplicados basándose en:
    - código CUPS
    - texto original (linea_texto si existe)
    """
    seen: set[Tuple[str, str]] = set()
    unique_items: List[Dict] = []

    for item in items:
        cups = item.get("cups_codigo")
        linea = item.get("linea_texto", "")

        key = (cups, linea)

        if key not in seen:
            seen.add(key)
            unique_items.append(item)

    return unique_items


def contar_por_cups(items: List[Dict]) -> List[Dict]:
    """
    Consolida cantidad por código CUPS.
    """
    conteo = {}

    for item in items:
        cups = item.get("cups_codigo")
        if not cups:
            continue

        if cups not in conteo:
            conteo[cups] = {
                "cups_codigo": cups,
                "cantidad": 0
            }

        conteo[cups]["cantidad"] += 1

    return list(conteo.values())
