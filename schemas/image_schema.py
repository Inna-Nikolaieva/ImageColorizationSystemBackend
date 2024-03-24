from datetime import datetime

from pydantic import BaseModel, validator


class ImageBase(BaseModel):
    image_file_url: str
    image_type: str
    color_style: int
    additional_parameters: int
    status: bool
    result_image_url: str
    creator_user_id: int

# Custom validator here
@validator('color_style', 'color_style','result_image_url', pre=True)
def allow_none(cls, v):
    if v is None:
         return None
    else:
        return v


# User inside ImageDisplay
class User(BaseModel):
    username: str

    class Config():
        orm_mode = True


class ImageDisplay(BaseModel):
    image_file_url: str
    image_type: str
    color_style: int
    additional_parameters: int
    timestamp: datetime
    status: bool
    result_image_url: str
    user: User

    class Config():
        orm_mode = True


# Image inside UserDisplay
class Image(BaseModel):
    image_file: str
    color_style: int
    additional_parameters: int
    status: bool
    result_image: str
    timestamp: datetime

    class Config():
        orm_mode = True
