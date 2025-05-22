from models import Task
from sqlalchemy.orm import Session
from controllers import UserController

class TaskController():
    def createTask(db: Session, title: str, description: str, state_id: int, username: str):
        try:
            user = UserController.findUserByUsername(db, username)
            if not user:
                raise ValueError("El usuario no existe")
            task = Task(title=title, description=description, state_id=state_id, user_id=user.id)
            db.add(task)
            db.commit()
            db.refresh(task)
            return f"Creaste una tarea:\n {task}"
        except Exception as e:
            db.rollback()
            return f"\nError: {e}"

    def getAllTasks(db: Session):
        try:
            tasks = db.query(Task).all()
            if not tasks:
                raise Exception("No hay tareas")
            return tasks
        except Exception as e:
            return f"Error: {e}"

    def getTaskById(db: Session, task_id: int):
        try:
            task = db.query(Task).filter(Task.id == task_id).first()
            if not task:
                raise Exception("No existe la tarea")
            return task
        except Exception as e:
            return f"Error: {e}"

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
            return f"Error: {e}"

    def deleteTask(db: Session, task_id: int):
        task = TaskController.getTaskById(db, task_id)
        if not task:
            return "No se pudo eliminar la tarea"
        db.delete(task)
        db.commit()
        return "Eliminaste la tarea"
