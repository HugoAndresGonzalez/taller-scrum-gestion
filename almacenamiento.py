import json
import os

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(ARCHIVO_TAREAS):
        return []

    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_tareas(tareas):
    """
    Guarda la lista de tareas en el archivo JSON.
    """
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
