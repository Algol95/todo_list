from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from models.user import User
from models.state import State


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
    state = relationship("State", back_populates="tasks")

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, description={self.description})"
