from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth import oauth2
from db.database import get_db
from db.hash_password import Hash
from db.models import DBSystemUser

router = APIRouter(
    tags=['authentication']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DBSystemUser).filter(DBSystemUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Incorrect password")

    access_token = oauth2.create_access_token(data={'sub': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.username
    }