
from typing import Optional
import models

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from database import engine
from pydantic import BaseModel, Field

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Create the class to handle post operations
class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1 and 5")
    complete: bool

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    

@app.get("/")
async def read_db_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()

@app.get("/todo/{todo_id}")
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    print("***********************Raise exception when trying to ********************")
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/")
async def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    db.add(todo_model)
    db.commit()
    
    return {
        "stattus": 201,
        "transaction": "Successfully added"
    }

@app.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, db: Session= Depends(get_db)):
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .first()
    
    if todo_model is None:
        raise http_exception()
    
    print(f"todo_model: {todo_model}")
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    db.add(todo_model)
    db.commit()
    
    return sucessfull_response(200)

@app.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is None:
        raise http_exception()
    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()
    
    return sucessfull_response(200)

def sucessfull_response(status_code):
    return {
        "stattus": status_code,
        "transaction": "Successfully added"
    }
def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")