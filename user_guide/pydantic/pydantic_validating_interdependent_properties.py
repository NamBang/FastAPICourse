from pydantic import BaseModel, Field, root_validator

class CreateUser(BaseModel):
    username: str = Field(..., min_length=3)
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)
    confirm_password: str = Field(..., min_length=3)

    @root_validator()
    def verify_passwords_match(cls, values):
        if values["password"] != values["confirm_password"]:
            raise ValueError("Passwords do not match")
        return values

CreateUser(username="test", email="example@example.com", password="1password", confirm_password="password")