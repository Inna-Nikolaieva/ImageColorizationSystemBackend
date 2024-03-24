from fastapi import HTTPException, status
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


def get_all_users(db: Session):
    return db.query(DBSystemUser).all()


def get_user_by_name(db: Session, username: str):
    user = db.query(DBSystemUser).filter(DBSystemUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found.')
    return user


def update_user(db: Session, username: str, request: UserBase):
    user = db.query(DBSystemUser).filter(DBSystemUser.username == username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found.')
    user.update({
        DBSystemUser.username: request.username,
        DBSystemUser.email: request.email,
        DBSystemUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "ok"


def delete_user(db: Session, username: str):
    user = db.query(DBSystemUser).filter(DBSystemUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found.')
    db.delete(user)
    db.commit()
    return "ok"
