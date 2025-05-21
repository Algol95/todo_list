from sqlalchemy.orm import Session
from models import User

def findUserByUsername(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def createUser(db: Session, username: str, password: str):
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
