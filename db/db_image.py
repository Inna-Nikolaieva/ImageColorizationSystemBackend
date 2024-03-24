import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import DBImage
from schemas.image_schema import ImageBase


def load_image(db: Session, request: ImageBase):
    new_image = DBImage(
        image_file_url=request.image_file_url,
        image_type=request.image_type,
        color_style=0,
        additional_parameters=0,
        status=False,
        result_image_url="",
        uploaded_by_user=request.creator_user_id,
        timestamp=datetime.datetime.now()
    )
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image


def get_images_by_user(db: Session, user_id: int):
    images = db.query(DBImage).filter(DBImage.uploaded_by_user == user_id).all()
    if not images:
        raise HTTPException(status_code=404,
                            detail=f'User with ID {user_id} does not have any images.')
    return images
