from fastapi import FastAPI

from routers.auth import router as auth_router
from routers.tasks import router as task_router

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Day 11 PostgreSQL Project"}


# Register routers (ONLY ONCE)
app.include_router(task_router)
app.include_router(auth_router)