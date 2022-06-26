from pydantic import BaseModel,Field, validator

class Blog(BaseModel):
    title: str = Field(...,min_length=5)
    is_active: bool

    @validator("title")
    def validate_no_sql_injection(cls, value):
        if "delete from" in value:
            raise ValueError("Our terms strictly prohobit SQLInjection Attacks")
        return value

Blog(title="delete from",is_active=True)