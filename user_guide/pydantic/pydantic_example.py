from typing import Optional, List
import time
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Comments(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    title: str
    description: Optional[str]
    comments: Optional[List[Comments]]
    language: Language = Language.PY
    create_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

# print(Blog(title="My fist blog",language="Go", is_active=True, comments=[{"first": 10, "last":2},]))
# time.sleep(5)
result = Blog(title="My second blog",language="Go", is_active=True, comments=[{"Third": 3, "Fourth": 4, "Fifth": 5},])
print(result.comments.__dir__)