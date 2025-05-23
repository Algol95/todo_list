from models import State
from sqlalchemy.orm import Session

class StateController():
    """
    Controlador para operaciones relacionadas con el modelo State.

    Author:
        Lorena Martínez
        Ángel Aragón

    Methods:
        **createState**(db, name): Crea estado nuevo
        **findStateByName**(db, name): Busca el estado por nombre de estado
        
    """

    def createState(db: Session, name: str):
        """Crea estado nuevo

        Args:
            db (Session): Sesión activa de SQLAlchemy
            name (str): Nombre de estado

        Raises:
            Exception: El nombre de usuario no puede estar vacío

        Returns:
            State/str: Objeto State / mensaje de error
        """
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
            return f"\033[31m❌ {e}\033[0m"

    def findStateByName(db: Session, name: str):
        """Busca el estado por nombre de estado

        Args:
            db (Session): Sesión activa de SQLAlchemy
            name (str): Nombre de estado

        Raises:
            Exception: El nombre de usuario no puede estar vacío

        Returns:
            State/str: Objeto State / mensaje de error
        """
        try:
            if not name:
                raise Exception("El nombre del estado no puede estar vacío")
            state = db.query(State).filter(State.name == name).first()
            if not state:
                raise Exception("El estado no existe")
            return state
        except Exception as e:
            return f"\033[31m❌ {e}\033[0m"
