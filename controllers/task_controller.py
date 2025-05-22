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
            return f"\n\033[32mCreaste una tarea:\n {task}\033[0m"
        except Exception as e:
            db.rollback()
            return f"\033[31m\n❌ {e}\033[0m"

    def getAllTasks(db: Session):
        try:
            tasks = db.query(Task).all()
            if not tasks:
                raise Exception("No hay tareas")
            return tasks
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"

    def getTaskById(db: Session, task_id: int):
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                raise Exception("No existe la tarea")
            return task
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"

    def updateTask(db: Session, task_id: int, new_title: str, new_description: str, new_state: int):
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
