from pydantic import BaseModel


class TodoModel(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
