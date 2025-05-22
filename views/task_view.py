from controllers import TaskController, UserController, StateController
from database import SessionLocal
from pprint import pp

def menu():
    print("\n\033[36m=======================")
    print("|         Menú        |")
    print("=======================")
    print("1. Crear tarea")
    print("2. Ver todas las tareas")
    print("3. Ver tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("=======================\033[0m")
    print("\033[91m6. Salir\033[0m")

    option = input("\n\033[33m► Introduce un índice: \033[0m")
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
                print("\n\033[91mSaliendo...\033[0m")
                db.close()
                break
            case _:
                print("\n\033[31m❌ No es un valor aceptado, vuelve a intentarlo\033[0m\n")

def createTask(db):
    title = input("\033[33m► Nombre de la tarea: ")
    description = input("► Descripción de la tarea: ")
    username = input("► Usuario a asignar(ej: admin): \033[0m")
    state = StateController.findStateByName(db, "To Do")
    return TaskController.createTask(db, title, description, state.id, username)

def viewAllTasks(db):
    return TaskController.getAllTasks(db)

def viewTask(db):
    try:
        task_id = int(input("\033[33m► ID de la tarea: \033[0m"))
        return TaskController.getTaskById(db, task_id)
    except ValueError as ve:
        return f"\n\033[31m❌ La ID debe ser un número entero: {ve}\033[0m"

def updateTask(db):
    try:
        task_id = int(input("\033[33m► ID de la tarea: "))
        new_title = input("► Nuevo título de la tarea: ")
        new_description = input("► Nueva descripción de la tarea: \033[0m")
        new_state = 0
        while True:
            print("\n\033[36m--------------------\nEstados disponibles:\n--------------------\n1. To Do\n\
2. In Progress\n3. Done\n--------------------\033[0m\n\033[91m4. Salir\033[0m")
            new_state = int(input("\n\033[33m► Nuevo estado de la tarea: \033[0m"))
            if new_state in [1, 2, 3]:
                break
            elif new_state == 4:
                new_state = None
                break
            else:
                print("\033[31m\nEstado no válido, vuelve a intentarlo\n\033[0m")
        return TaskController.updateTask(db, task_id, new_title, new_description, new_state)
    except ValueError as ve:
        return f"\033[31m❌ El dato requerido debe ser un entero: {ve}\033[0m"

def deleteTask(db):
    try:
        task_id = int(input("\033[33m►ID de la tarea: \033[0m"))
        return TaskController.deleteTask(db, task_id)
    except ValueError as ve:
        return f"\033[31m4❌ La id debe ser un número entero: {ve}\033[0m"
