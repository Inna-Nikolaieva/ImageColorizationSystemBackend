import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from auth.oauth2 import oauth2_schema, get_current_user
from db import db_image
from db.database import get_db
from schemas.image_schema import ImageDisplay, ImageBase
from schemas.user_schema import UserBase

router = APIRouter(
    prefix='/image',
    tags=['image']
)

image_types = ['absolute', 'relative']


# Load image
@router.post('/upload/data', response_model=ImageDisplay)
def load_image_data(request: ImageBase, db: Session = Depends(get_db),
                    current_user: UserBase = Depends(get_current_user)):

    if request.image_type not in image_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_type can only take values \'absolute\' and \'relative\'.")

    request.creator_user_id = current_user.userId
    return db_image.load_image(db, request)


@router.post('/upload/image')
def load_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(8))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images_store/{filename}'
    with open(path, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return path


# Read images by user
@router.get('/{username}', response_model=List[ImageDisplay])
def get_images_by_current_user(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_image.get_images_by_user(db, current_user.userId)
