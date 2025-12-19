from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.account import UserRegistrationIn, UserRegistrationOut
from core.database import get_db
from core.passwords import create_password
from handlers.account import AccountManager


auth_router = APIRouter(
    prefix='/auth',
)


@auth_router.post('/register', response_model=UserRegistrationOut)
def register(data: UserRegistrationIn, db: Session = Depends(get_db)):
    data.password = create_password(data.password)
    return AccountManager.create_user(session=db, data=data)


@auth_router.post('/login')
def login():
    pass


@auth_router.post('/logout')
def logout():
    pass
