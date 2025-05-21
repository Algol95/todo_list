from controllers import *
from database import SessionLocal


def menu():
    print("Menú:")
    print("1. Crear tarea")
    print("2. Ver todas las tareas")
    print("3. Ver tarea")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")
    option = input("Introduce un índice: ")
    return option

def runMenu ():
    db = SessionLocal()
    option = menu()
    while option !=6 :
        option = 0
        match option:
            case "1":
                print(createTask(db))
            case "2":
                print("Viste todas las tareas")
            case "3":
                print("Viste una tarea")
            case "4":
                print("Actualizaste tarea")
            case "5":
                print("Eliminaste tarea")
            case "6":
                break
            case _:
                print("No es un valor aceptado")

def createTask(db):
    try:
        title = input("Nombre de la tarea: ")
        description = input("Descripción de la tarea: ")
        username = input("Usuario a asignar(ej: admin): ")
        user = UserController.findUserByUsername(username)
        if not user:
            raise ValueError("El usuario no existe")
        state = StateController.findStateByName("To Do")
        task = TaskController.createTask(db, title, description, state.id, user.id)
        return f"Creaste una tarea:\n {task}"
    except Exception as e:
        print(f"Error: {e}")