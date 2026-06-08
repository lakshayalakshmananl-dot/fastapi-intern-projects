from fastapi import FastAPI
from routers.tasks import router

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Day 11 PostgreSQL Project"}

app.include_router(router)