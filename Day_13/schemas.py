from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool