from gestor_tareas import (
    listar_tareas,
    agregar_tarea,
    completar_tarea,
    eliminar_tarea
)


def mostrar_tareas():
    tareas = listar_tareas()

    if not tareas:
        print("\nNo hay tareas registradas.\n")
        return

    print("\nLISTA DE TAREAS")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['descripcion']}")
    print()


def menu():
    print("=== GESTOR DE TAREAS ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def solicitar_indice(mensaje):
    try:
        return int(input(mensaje)) - 1
    except ValueError:
        print("Entrada inválida.\n")
        return None


def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas()

        elif opcion == "2":
            descripcion = input("Ingrese la nueva tarea: ").strip()
            if descripcion:
                agregar_tarea(descripcion)
                print("Tarea agregada correctamente.\n")

        elif opcion == "3":
            mostrar_tareas()
            indice = solicitar_indice("Número de tarea a completar: ")
            if indice is not None:
                try:
                    completar_tarea(indice)
                    print("Tarea marcada como completada.\n")
                except IndexError:
                    print("Selección inválida.\n")

        elif opcion == "4":
            mostrar_tareas()
            indice = solicitar_indice("Número de tarea a eliminar: ")
            if indice is not None:
                try:
                    eliminar_tarea(indice)
                    print("Tarea eliminada correctamente.\n")
                except IndexError:
                    print("Selección inválida.\n")

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()
