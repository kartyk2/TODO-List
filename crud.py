# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import TodoItemAlreadyExistError, TodoItemNotFoundError
from models import TodoItem
from schemas import CreateAndUpdateTask


# Function to get list of  task info
def get_all_tasks(session: Session, limit: int, offset: int) -> List[TodoItem]:
    return session.query(TodoItem).offset(offset).limit(limit).all()


# Function to  get info of a particular task
def get_task_info_by_id(session: Session, _id: int) -> TodoItem:
    task_info = session.query(TodoItem).get(_id)

    if task_info is None:
        raise TodoItemNotFoundError

    return task_info


# Function to add a new task info to the database
def create_task(session: Session, task_info: CreateAndUpdateTask) -> TodoItem:
    task_details = session.query(TodoItem).filter(TodoItem.name == task_info.name, TodoItem.description == task_info.description).first()
    if task_details is not None:
        raise TodoItemAlreadyExistError

    new_task_info = TodoItem(**task_info.dict())
    session.add(new_task_info)
    session.commit()
    session.refresh(new_task_info)
    return new_task_info


# Function to update details of the task
def update_task_info(session: Session, _id: int, info_update: CreateAndUpdateTask) -> TodoItem:
    task_info = get_task_info_by_id(session, _id)

    if task_info is None:
        raise TodoItemNotFoundError

    task_info.name = info_update.name
    task_info.description = info_update.description
    task_info.status = info_update.status

    session.commit()
    session.refresh(task_info)

    return task_info


# Function to delete a task info from the db
def delete_task_info(session: Session, _id: int):
    task_info = get_task_info_by_id(session, _id)

    if task_info is None:
        raise TodoItemNotFoundError

    session.delete(task_info)
    session.commit()
    return
