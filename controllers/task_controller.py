from models import Task
from sqlalchemy.orm import Session
from .user_controller import UserController

class TaskController():
    """
    Controlador para operaciones relacionadas con el modelo Task.

    Author:  
        Lorena Martínez.  
        Ángel Aragón.  

    Methods:  
        `createTask(db, title, description, state_id, usename):` Crea una nueva tarea en BBDD  
        `getAllTasks(db):` Devuelve una lista de todas las tareas  
        `getTaskById(db, task_id):` Devuelve una tarea por su id  
        `updateTask(db, task_id, new_title, new_description, new_state):` Actualiza una tarea  
        `deleteTask(db, task_id):` Elimina una tarea por su id  
    """
    def createTask(db: Session, title: str, description: str, state_id: int, username: str):
        """Crea una nueva tarea en BBDD

        Args:  
            `db (Session):` Sesión activa de SQLAlchemy  
            `title (str):` Título de la tarea  
            `description (str):` Descripción de la tarea  
            `state_id (int):` ID del estado de la tarea  
            `username (str):` Nombre de usuario del dueño de la tarea  

        Raises:  
            Exception: El título y la descripción no pueden estar vacíos  
            Exception: Id del estado no puede estar vacía  
            Exception: El usuario no existe  

        Returns:
            str: Mensaje de tarea creada o mensaje de error
        """
        try:
            if not title or not description:
                raise Exception("El título y la descripción no pueden estar vacíos")
            if not state_id:
                raise Exception("Se debe incluir una id de estado")
            user = UserController.findUserByUsername(db, username)
            if isinstance(user, str):
                raise Exception(user)
            task = Task(title=title, description=description, state_id=state_id, user_id=user.id)
            db.add(task)
            db.commit()
            db.refresh(task)
            return f"\n\033[32mCreaste una tarea:\n {task}\033[0m"
        except Exception as e:
            db.rollback()
            return f"\033[31m\n❌ {e}\033[0m"

    def getAllTasks(db: Session):
        """Devuelve una lista de todas las tareas

        Args:  
            `db (Session):` Sesión activa de SQLAlchemy

        Raises:  
            Exception: No hay tareas

        Returns:
            list[Task]/str: Lista de tareas / mensaje de error
        """
        try:
            tasks = db.query(Task).all()
            if not tasks:
                raise Exception("No hay tareas")
            return tasks
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"

    def getTaskById(db: Session, task_id: int):
        """Devuelve una tarea por su id

        Args:  
            `db (Session):` Sesión activa de SQLAlchemy  
            `task_id (int):` Id de la tarea

        Raises:  
            Exception: No existe la tarea

        Returns:
            Task/str: Objeto Task / mensaje de error
        """
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                raise Exception("No existe la tarea")
            return task
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"

    def updateTask(db: Session, task_id: int, new_title: str, new_description: str, new_state: int):
        """Actualiza una tarea

        Args:  
            `db (Session):` Sesión activa de SQLAlchemy  
            `task_id (int):` Id de la tarea  
            `new_title (str):` Nuevo titulo de la tarea  
            `new_description (str):` Nueva descripción de la tarea  
            `new_state (int):` Nuevo estado de la tarea  

        Raises:  
            Exception: La tarea a editar no existe

        Returns:
            str: Mensaje con la tarea actualizada o mensaje de error
        """
        try:
            task = TaskController.getTaskById(db, task_id)
            if isinstance(task, str):
                raise Exception(task)
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_state:
                task.state_id = new_state
            db.commit()
            db.refresh(task)
            return f"\n\033[32m-----------------------\nSe actualizó la tarea:\n-----------------------\033[0m\n{task}"
        except Exception as e:
            db.rollback()
            return f"\033[31m❌ {e}\033[0m"

    def deleteTask(db: Session, task_id: int):
        """Elimina una tarea por su id

        Args:  
            `db (Session):` Sesión activa de SQLAlchemy  
            `task_id (int):` Id de la tarea  

        Raises:  
            Exception: La tarea a eliminar no existe

        Returns:
            str: Mensaje de tarea eliminada o mensaje de error
        """
        try:
            task = TaskController.getTaskById(db, task_id)
            if isinstance(task, str):
                raise Exception(task)
            db.delete(task)
            db.commit()
            return "\033[32mEliminaste la tarea\033[0m"
        except Exception as e:
            db.rollback()
            return f"\033[31m❌ {e}\033[0m"
