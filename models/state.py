from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class State(Base):
    """
    Modelo de la tabla states

    Author:
            Lorena Martínez
            Ángel Aragón

    Attributes:
        id (int): ID del estado
        name (str): Nombre del estado
        tasks (list): Lista de tareas asociadas al estado, relacionado con el modelo Task

    Methods:
        __repr__(): Representación en cadena del objeto State
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)

    tasks = relationship("Task", back_populates="state", cascade="all, delete-orphan")

    def __repr__(self):
        return f"State(id={self.id}, name={self.name})"
