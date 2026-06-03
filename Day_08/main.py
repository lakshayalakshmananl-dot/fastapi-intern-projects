from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field,field_validator
from typing import Optional

app = FastAPI()

# Pydantic Model with Constraints
class Item(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    description: Optional[str] = None
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Item name cannot be empty or spaces only")
        return value

# Temporary database
items = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Phone", "price": 20000}
}

# Home Endpoint
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# Get Single Item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return items[item_id]

# Get All Items
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    item_list = list(items.values())
    return item_list[skip: skip + limit]

# Create Item
@app.post("/items")
def create_item(item: Item):
    new_id = max(items.keys()) + 1 if items else 1

    items[new_id] = item.model_dump()

    return {
        "id": new_id,
        **items[new_id]
    }