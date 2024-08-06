from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    age: int
    created_at: datetime
    updated_at: datetime = None
