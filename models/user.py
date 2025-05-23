from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    """
    Modelo de la tabla users

    Author:
            Lorena Martínez
            Ángel Aragón

    Attributes:
        id (int): ID del usuario
        username (str): Nombre de usuario
        password (str): Contraseña del usuario
        tasks (list): Lista de tareas asociadas al usuario, relacionado con el modelo Task

    Methods:
        __repr__(): Representación en cadena del objeto User
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

#
