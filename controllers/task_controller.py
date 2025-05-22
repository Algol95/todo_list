from models import Task
from sqlalchemy.orm import Session
from .user_controller import UserController

class TaskController():
    def createTask(db: Session, title: str, description: str, state_id: int, username: str):
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
            return f"Creaste una tarea:\n {task}"
        except Exception as e:
            db.rollback()
            return f"\n{e}"

    def getAllTasks(db: Session):
        try:
            tasks = db.query(Task).all()
            if not tasks:
                raise Exception("No hay tareas")
            return tasks
        except Exception as e:
            return f"{e}"

    def getTaskById(db: Session, task_id: int):
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                raise Exception("No existe la tarea")
            return task
        except Exception as e:
            return f"{e}"

    def updateTask(db: Session, task_id: int, new_title: str, new_description: str, new_state: int):
        try:
            task = TaskController.getTaskById(db, task_id)
            if not task:
                raise Exception("No existe la tarea")
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_state:
                task.state_id = new_state
            db.commit()
            db.refresh(task)
            return task
        except Exception as e:
            db.rollback()
            return f"{e}"

    def deleteTask(db: Session, task_id: int):
        try:
            task = TaskController.getTaskById(db, task_id)
            if isinstance(task, str):
                raise Exception(task)
            db.delete(task)
            db.commit()
            return "Eliminaste la tarea"
        except Exception as e:
            db.rollback()
            return f"{e}"
