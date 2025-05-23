from database import SessionLocal
from models import User

def seed_users():
    """
    Función para sembrar los usuarios iniciales en la base de datos.
    Crea los usuarios "admin", "lorenitarechulona" y "angelonpelon" si no existen.

    Author:
        Lorena Martínez
        Ángel Aragón

    Raises:
        Exception: Si ocurre un error al sembrar los estados.
    """
    db = SessionLocal()
    try:
        users = [
            User(username="admin", password="admin"),
            User(username="lorenitarechulona", password="gympower"),
            User(username="angelonpelon", password="gaypower"),
        ]

        for user in users:
            exist = db.query(User).filter(User.username == user.username).first()
            if not exist:
                db.add(user)
        db.commit()
        print("Users seeded successfully.")
    except Exception as e:
        print(f"Error seeding users: {e}")
        db.rollback()
    finally:
        db.close()
