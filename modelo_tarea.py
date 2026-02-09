def crear_tarea(descripcion):
    """
    Crea y retorna una nueva tarea con estado inicial no completado.
    """
    return {
        "descripcion": descripcion,
        "completada": False
    }
