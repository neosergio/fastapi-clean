from fastapi import FastAPI

from app.api.v1 import todo

app = FastAPI()

app.include_router(todo.router, prefix='/api/v1/todos', tags=['todos'])
