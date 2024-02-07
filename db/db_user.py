from sqlalchemy.orm import Session

from db.hash_password import Hash
from db.models import DBSystemUser
from schemas.user_schema import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DBSystemUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
