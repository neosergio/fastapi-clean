from app.repositories import todo_repository
from app.schemas.todo import TodoCreate, TodoUpdate


def create_todo(todo: TodoCreate):
    # generar el id y agregarlo a todo
    return todo_repository.create_todo(todo)


def get_todo_by_id(todo_id: str):
    return todo_repository.get_todo_by_id(todo_id)


def get_all_todos():
    return todo_repository.get_all_todos()


def update_todo(todo_id: str, todo: TodoUpdate):
    return todo_repository.update_todo(todo_id, todo)


def delete_todo_by_id(todo_id: str):
    return todo_repository.delete_todo_by_id(todo_id)
