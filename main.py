from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    print(item)
    return item



@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
