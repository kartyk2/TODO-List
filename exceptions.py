# exceptions.py
class TodoItemException(Exception):
    ...


class TodoItemNotFoundError(TodoItemException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Item Info Not Found"


class TodoItemAlreadyExistError(TodoItemException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Item Info Already Exists"
