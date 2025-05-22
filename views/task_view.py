from controllers import TaskController, UserController, StateController
from database import SessionLocal
from pprint import pp

def menu():
    print("Menú:")
    print("=======================")
    print("1. Crear tarea")
    print("2. Ver todas las tareas")
    print("3. Ver tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")
    print("=======================")
    option = input("Introduce un índice: ")
    return option

def runMenu():
    db = SessionLocal()
    while True:
        option = ""
        option = menu()
        match option:
            case "1":
                print(createTask(db))
            case "2":
                pp(viewAllTasks(db))
            case "3":
                print(viewTask(db))
            case "4":
                print(updateTask(db))
            case "5":
                print(deleteTask(db))
            case "6":
                print("Saliendo...")
                db.close()
                break
            case _:
                print("No es un valor aceptado, vuelve a intentarlo\n")

def createTask(db):
    title = input("Nombre de la tarea: ")
    description = input("Descripción de la tarea: ")
    username = input("Usuario a asignar(ej: admin): ")
    state = StateController.findStateByName(db, "To Do")
    return TaskController.createTask(db, title, description, state.id, username)

def viewAllTasks(db):
    return TaskController.getAllTasks(db)

def viewTask(db):
    try:
        task_id = int(input("ID de la tarea: "))
        return TaskController.getTaskById(db, task_id)
    except ValueError as ve:
        return f"La ID debe ser un número entero: {ve}"

def updateTask(db):
    try:
        task_id = int(input("ID de la tarea: "))
        new_title = input("Nuevo título de la tarea: ")
        new_description = input("Nueva descripción de la tarea: ")
        new_state = 0
        while True:
            print("Estados disponibles:\n--------------------\n1. To Do\n2. In Progress\n3. Done\n\
--------------------\n4. Salir")
            new_state = int(input("Nuevo estado de la tarea: "))
            if new_state in [1, 2, 3]:
                break
            elif new_state == 4:
                new_state = None
                break
            else:
                print("\nEstado no válido, vuelve a intentarlo\n")
        task = TaskController.updateTask(db, task_id, new_title, new_description, new_state)
        return f"\nActualizaste la tarea:\n {task}"
    except ValueError as ve:
        print(f"El dato requerido debe ser un entero: {ve}")

def deleteTask(db):
    try:
        task_id = int(input("ID de la tarea: "))
        return TaskController.deleteTask(db, task_id)
    except ValueError as ve:
        print(f"La id debe ser un número entero: {ve}")
