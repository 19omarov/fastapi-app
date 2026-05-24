from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str
    password: str = Field(min_length=5, max_length=5)
    telephone: str = Field(min_length=11, max_length=11)
    cash: Optional[float] = None

class UserResponse(BaseModel):
    id: int
    name: str
    telephone: str = Field(min_length=11, max_length=11)
    cash: float

class UserLogin(BaseModel):
    telephone: str = Field(min_length=11, max_length=11)
    password: str = Field(min_length=5, max_length=5)

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str