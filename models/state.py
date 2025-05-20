from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)

    tasks = relationship("Task", back_populates="state", cascade="all, delete-orphan")

    def __repr__(self):
        return f"State(id={self.id}, name={self.name})"
