from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # tags: list[int] = []
    tags: set[int] = set()
    # image: Image | None = None
    image: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id, item: Item):
    return {"item_id": item_id, "item": item}