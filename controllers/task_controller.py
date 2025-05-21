from models import Task
from sqlalchemy.orm import Session

def createTask(db: Session, title: str, description: str, state_id: int, user_id: int):
    task = Task(title=title, description=description, state_id=state_id, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def getAllTasks(db: Session):
    return db.query(Task).all

def getTaskById(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first

def updateTask(db: Session, task_id: int, new_title: str, new_description: str, new_state: int):
    task = getTaskById(db, task_id)
    if not task:
        return None
    if new_title:
        task.title = new_title
    if new_description:
        task.description = new_description
    if new_state:
        task.state = new_state
    db.commit()
    db.refresh(task)
    return task

def deleteTask(db: Session, task_id: int):
    task = getTaskById(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
