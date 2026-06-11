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


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str