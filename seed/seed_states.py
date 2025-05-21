from database import SessionLocal
from models import State

def seed_states():
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
