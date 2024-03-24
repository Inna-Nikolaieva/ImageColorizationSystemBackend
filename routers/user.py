from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_user
from db.database import get_db
from schemas.user_schema import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)


# Read one user
@router.get('/{username}', response_model=UserDisplay)
def get_user(username: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user_by_name(db, username)


# Update user
@router.post('/{username}/update')
def update_user(username: str, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db,username,request)


# Delete user
@router.delete('/delete/{username}')
def update_user(username: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db, username)
