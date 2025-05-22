from sqlalchemy.orm import Session
from models import User

class UserController():

    def findUserByUsername(db: Session, username: str):
        try:
            if not username:
                raise Exception("El nombre de usuario no puede estar vacío")
            user = db.query(User).filter(User.username == username).first()
            if not user:
                raise Exception("El usuario no existe")
            return user
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"

    def createUser(db: Session, username: str, password: str):
        try:
            if not username or not password:
                raise Exception("El nombre de usuario y la contraseña no pueden estar vacíos")
            user = User(username=username, password=password)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            return f"\033[31m❌ {e}\033[0m"
