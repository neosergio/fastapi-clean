from fastapi import APIRouter, HTTPException

from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from app.services import todo_service

router = APIRouter()


@router.post("/", response_model=Todo)
def create_todo(todo_in: TodoCreate):
    todo = todo_service.create_todo(todo_in)
    if not todo:
        raise HTTPException(status_code=400, detail="Todo could not be created")
    return todo


@router.get("/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: str):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=400, detail="Todo could not be found")
    return todo


@router.get("/", response_model=list[Todo])
def get_all_todos():
    todos = todo_service.get_all_todos()
    return todos


@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo_in: TodoUpdate):
    todo = todo_service.update_todo(todo_id, todo_in)
    if not todo:
        raise HTTPException(status_code=400, detail="Todo could not be updated")
    return todo


@router.delete("/{todo_id}", response_model=bool)
def delete_todo_by_id(todo_id: str):
    success = todo_service.delete_todo_by_id(todo_id)
    if not success:
        raise HTTPException(status_code=400, detail="Todo could not be deleted")
    return success
