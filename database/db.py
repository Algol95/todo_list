"""
Conexión a la base de datos utilizando SQLAlchemy.
Este módulo establece la conexión a la base de datos PostgreSQL

Author:
    Lorena Martínez
    Ángel Aragón
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+pg8000://postgres:root@localhost/todo_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
