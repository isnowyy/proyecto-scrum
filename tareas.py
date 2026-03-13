
tareas = []

#variable para generar los id
siguiente_id = 1


def crear_tarea():

    global siguiente_id #global sirve para que se pueda modificar una variable que esta afuera de una funcion

    tituloTarea = input("Escribe el título de la tarea: ")

    tarea = {
        "id": siguiente_id,
        "titulo": tituloTarea,
        "completada": False
    }

    #agrega la tarea a la lista
    tareas.append(tarea)

    #aumenta el numero de id
    siguiente_id += 1

    print("Tarea creada correctamente.")

def listar_tareas():

    #verifica si hay tareas
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\nLista de tareas:")
    for tarea in tareas:
        estado = "✓" if tarea["completada"] else "✗"

        print(f'{tarea["id"]}. {tarea["titulo"]} [{estado}]')

def cambiarEstadoTarea():

    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    listar_tareas()

    try:
        id_tarea = int(input("Escribe el ID de la tarea a modificar: "))
    except ValueError:
        print("Debes escribir un número válido.")
        return

    for tarea in tareas:
        if tarea["id"] == id_tarea:

            estado_actual = "completada" if tarea["completada"] else "pendiente"
            print(f"La tarea está actualmente: {estado_actual}")

            opcion = input("Quieres cambiar su estado? (s/n): ").lower()

            if opcion == "s":
                tarea["completada"] = not tarea["completada"]
                print("Estado de la tarea actualizado.")
            else:
                print("No se hicieron cambios.")

            return

    print("No se encontró una tarea con ese ID.")


def menuTareas():
    while True:
        print("\n--- TaskFlow CLI ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Cambiar el estado de la tarea")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            cambiarEstadoTarea()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


menuTareas()