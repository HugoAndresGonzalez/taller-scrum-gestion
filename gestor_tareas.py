from almacenamiento import cargar_tareas, guardar_tareas
from modelo_tarea import crear_tarea


def listar_tareas():
    """
    Retorna la lista completa de tareas.
    """
    return cargar_tareas()


def agregar_tarea(descripcion):
    """
    Agrega una nueva tarea a la lista.
    """
    tareas = cargar_tareas()
    tareas.append(crear_tarea(descripcion))
    guardar_tareas(tareas)


def completar_tarea(indice):
    """
    Marca una tarea como completada según su índice.
    """
    tareas = cargar_tareas()
    if indice < 0 or indice >= len(tareas):
        raise IndexError("Índice fuera de rango")

    tareas[indice]["completada"] = True
    guardar_tareas(tareas)


def eliminar_tarea(indice):
    """
    Elimina una tarea según su índice.
    """
    tareas = cargar_tareas()
    if indice < 0 or indice >= len(tareas):
        raise IndexError("Índice fuera de rango")

    tareas.pop(indice)
    guardar_tareas(tareas)
