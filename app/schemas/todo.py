from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None


class TodoInDBBase(TodoBase):
    id: str
    completed: bool


class Todo(TodoInDBBase):
    pass
