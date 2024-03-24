from typing import List

from pydantic import BaseModel

from schemas.image_schema import Image


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    images: List[Image] = []

    class Config():
        orm_mode = True



