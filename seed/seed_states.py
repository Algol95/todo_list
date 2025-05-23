from database import SessionLocal
from models import State

def seed_states():
    """
    Función para sembrar los estados iniciales en la base de datos.
    Crea los estados "To Do", "In Progress" y "Done" si no existen.

    Author:
        Lorena Martínez
        Ángel Aragón

    Raises:
        Exception: Si ocurre un error al sembrar los estados.
    """
    db = SessionLocal()
    try:
        states = ["To Do", "In Progress", "Done"]
        for state_name in states:
            exist = db.query(State).filter(State.name == state_name).first()
            if not exist:
                db.add(State(name=state_name))
        db.commit()
        print("States seeded successfully.")
    except Exception as e:
        print(f"Error seeding states: {e}")
        db.rollback()
    finally:
        db.close()
