import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.\n")
        return

    print("\nLISTA DE TAREAS")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['descripcion']}")
    print()


def agregar_tarea(tareas):
    descripcion = input("Ingrese la nueva tarea: ").strip()
    if descripcion:
        tareas.append({
            "descripcion": descripcion,
            "completada": False
        })
        guardar_tareas(tareas)
        print("Tarea agregada correctamente.\n")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Número de tarea a marcar como completada: ")) - 1
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.\n")
    except (ValueError, IndexError):
        print("Selección inválida.\n")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tareas.pop(indice)
        guardar_tareas(tareas)
        print("Tarea eliminada.\n")
    except (ValueError, IndexError):
        print("Selección inválida.\n")


def menu():
    print("=== GESTOR DE TAREAS ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")



def main():
    tareas = cargar_tareas()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    main()

