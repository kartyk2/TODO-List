# api.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_tasks, create_task, get_task_info_by_id, update_task_info, delete_task_info
from database import get_db
from exceptions import TodoItemException
from schemas import Task, CreateAndUpdateTask, PaginatedTaskInfo

router = APIRouter()


# Example of Class based view
@cbv(router)
class Tasks:
    session: Session = Depends(get_db)

    # API to get the list of task info
    @router.get("/tasks", response_model=PaginatedTaskInfo)
    def list_tasks(self, limit: int = 10, offset: int = 0):

        tasks_list = get_all_tasks(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": tasks_list}

        return response

    # API endpoint to add a task info to the database
    @router.post("/tasks")
    def add_task(self, task_info: CreateAndUpdateTask):

        try:
            task_info = create_task(self.session, task_info)
            return task_info
        except TodoItemException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular task
@router.get("/tasks/{task_id}", response_model=Task)
def get_task_info(task_id: int, session: Session = Depends(get_db)):

    try:
        task_info = get_task_info_by_id(session, task_id)
        return task_info
    except TodoItemException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing task info
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, new_info: CreateAndUpdateTask, session: Session = Depends(get_db)):

    try:
        task_info = update_task_info(session, task_id, new_info)
        return task_info
    except TodoItemException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a task info from the data base
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_db)):

    try:
        return delete_task_info(session, task_id)
    except TodoItemException as cie:
        raise HTTPException(**cie.__dict__)
