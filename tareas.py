import json

# Load tasks from the JSON file
try:
    with open('Tareas.json', 'r', encoding='utf-8') as f:
        tareas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tareas = []

# Calculate the next ID based on existing tasks
siguiente_id = max((tarea["id"] for tarea in tareas), default=0) + 1


def crear_tarea():
    global siguiente_id

    tituloTarea = input("Escribe el título de la tarea: ")

    tarea = {
        "id": siguiente_id,
        "titulo": tituloTarea,
        "completada": False
    }

    tareas.append(tarea)
    siguiente_id += 1

    # Save tasks to the JSON file
    guardar_tareas()

    print("Tarea creada correctamente.")


def listar_tareas():
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
                guardar_tareas()
                print("Estado de la tarea actualizado.")
            else:
                print("No se hicieron cambios.")
            return

    print("No se encontró una tarea con ese ID.")


def guardar_tareas():
    with open("Tareas.json", "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
def eliminar_tarea():
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return
    
    listar_tareas()
    try:
        id_tarea = int(input("Escribe el ID de la tarea a eliminar:"))
        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tareas.remove(tarea)
                guardar_tareas()
                print("Tarea eliminada correctamente.")
                return
    except ValueError:
        print("Debes escribir un numero valido para el ID.")
        return
    


def menuTareas():
    while True:
        print("\n--- TaskFlow CLI ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Cambiar el estado de la tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            cambiarEstadoTarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


menuTareas()