from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    fullname: str | None = None


app = FastAPI()

####Mix path, query and body parameters
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(default=None, title="THe ID of the item to get", ge=0, le=1000),
#     q: str | None = None,
#     item: Item| None = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     if item:
#         results.update({"item":item})
#     return results

### multiple body parameters

# @app.put("/items/{item_id}")
# async def update_item(item_id: str, item: Item, user: User, importance: int = Body(default=None), q: str| None = None):
#     results = {"item_id": item_id, "user": user, "item": item}
#     return results

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(default=None, embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
