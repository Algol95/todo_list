from models import State
from sqlalchemy.orm import Session

class StateController():

    def createState(db: Session, name: str):
        try:
            if not name:
                raise Exception("El nombre del estado no puede estar vacío")
            state = State(name=name.title())
            db.add(state)
            db.commit()
            db.refresh(state)
            return state
        except Exception as e:
            db.rollback()
            return f"{e}"

    def findStateByName(db: Session, name: str):
        try:
            if not name:
                raise Exception("El nombre del estado no puede estar vacío")
            state = db.query(State).filter(State.name == name).first()
            if not state:
                raise Exception("El estado no existe")
            return state
        except Exception as e:
            return f"{e}"
