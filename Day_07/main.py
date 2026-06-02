from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Define the Pydantic Schema for incoming data
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None  # Optional field with a default value

# Temporary database
items = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Phone", "price": 20000}
}

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return items[item_id]

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    item_list = list(items.values())
    return item_list[skip: skip + limit]

# 2. Add the POST endpoint to create items
@app.post("/items")
def create_item(item: Item):
    # Automatically generate a new incremented integer ID
    new_id = max(items.keys()) + 1 if items else 1
    
    # item.model_dump() converts the Pydantic object into a standard Python dict
    items[new_id] = item.model_dump()
    
    # Return a success message alongside the created object data
    return {"id": new_id, **items[new_id]}