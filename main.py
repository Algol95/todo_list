from seed import seed_users, seed_states
from views.task_view import runMenu

def main():
    """
    Función principal que inicializa la base de datos y ejecuta el menú de la aplicación.

    Author:
        Lorena Martínez
        Ángel Aragón
    """
    seed_users()
    seed_states()

    runMenu()

if __name__ == "__main__":
    main()
