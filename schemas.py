# schemas.py
from pydantic import BaseModel

from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateTask(BaseModel):
    name: str
    description: str
    status: bool


# TO support list and get APIs
class Task(CreateAndUpdateTask):
    id: int

    class Config:
        orm_mode = True


# To support list tasks API
class PaginatedTaskInfo(BaseModel):
    limit: int
    offset: int
    data: List[Task]
