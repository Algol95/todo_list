from models import State
from sqlalchemy.orm import Session

def createState(db: Session, name: str):
    state = State(name = name.title()) 
    db.add(state)
    db.commit
    db.refresh(state)
    return state

def findStateByName(db:Session, name:str):
    return db.query(State).filter(State.name == name).first