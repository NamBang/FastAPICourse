from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import models

from passlib.context import CryptContext


class CreateUser(BaseModel):
    id: int
    email: Optional[str]
    username: str
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

def get_password_hash(password):
    return bcrypt_context.hash(password)

@app.post("/create/user")
async def create_user(create_user: CreateUser):
    """_summary_

    Args:
        create_user (CreateUser): _description_

    Returns:
        _type_: _description_
    """
    create_user_model = models.Users()
    
    create_user_model.email = create_user.email
    create_user_model.username = create_user
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.password = get_password_hash(create_user.password)
    
    return create_user_model
    