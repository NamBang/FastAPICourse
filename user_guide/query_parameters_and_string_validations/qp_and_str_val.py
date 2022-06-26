from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    result = {"items": [{"item_id": "foo"}]}
    
    if q:
        result.update({"q": q})
        
    return result