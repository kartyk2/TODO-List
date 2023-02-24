# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Boolean
from database import Base
import enum




class TodoItem(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(Boolean)
