from re import I
import string
from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get("/items", response_model=list[Item])
async def read_items():
    return items

@app.get("/keyword-weights", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 3.4, "bar": 2.4}