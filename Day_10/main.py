from fastapi import FastAPI
from router.books import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Book API"}

app.include_router(router)