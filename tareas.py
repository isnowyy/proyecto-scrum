
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

def menuTareas():
    while True:
        print("\n--- TaskFlow CLI ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


menuTareas()