from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id: str = None
    username: str
    email: str
    age: int
    created_at: datetime = None
    updated_at: datetime = None
