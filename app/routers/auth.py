from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..schemas.account import UserInDB, User
from ..schemas.token import Token
from ..core.database import get_db
from ..core.passwords import create_password_hash, check_password_hash
from ..core.token import create_access_token
from ..handlers.account import AccountManager


auth_router = APIRouter(
    prefix='/auth',
)


#? I need to test what data will return from this endpoint
@auth_router.post('/register', response_model=User)
def register(data: UserInDB, db: Session = Depends(get_db)):
    data.password = create_password_hash(data.password)
    return AccountManager.create_user(session=db, data=data)


def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    user = AccountManager.get_user_by_email(session=db, email=email)
    if not user:
        return False
    if not check_password_hash(password, user.password):
        return False
    return user


@auth_router.post('/token', response_model=Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post('/refresh')
def refresh_token():
    pass
