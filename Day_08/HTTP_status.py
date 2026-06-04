from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)


items = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Phone", "price": 20000}
}


@app.get("/")
def home():
    return {"message": "HTTP Status Codes Demo"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return items[item_id]


@app.post(
    "/items",
    status_code=status.HTTP_201_CREATED
)
def create_item(item: Item):
    new_id = max(items.keys()) + 1

    items[new_id] = item.model_dump()

    return {
        "id": new_id,
        **items[new_id]
    }