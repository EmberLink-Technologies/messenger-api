from uuid import UUID
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from jwt import PyJWTError

from ..core.database import get_db
from ..core.token import oauth2_scheme, decode_token
from ..schemas.account import User
from ..schemas.token import TokenData
from ..handlers.account import AccountManager


account_router = APIRouter(prefix="/users")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail='Could not validate credentials',
                                         headers={'WWW-Authentication': 'Bearer'}
                                         )
    try:
        payload = decode_token(token)
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
        token_data = TokenData(
            username=username
        )
    except PyJWTError:
        return credentials_exception
    user = AccountManager.get_user_by_username(username=token_data.username, session=session)
    if user is None:
        raise credentials_exception
    return user


@account_router.get("/me", response_model=User)
def get_my_account(current_user: User = Depends(get_current_user)):
    return current_user


#! NOT FINISH
@account_router.patch("/me/update")
def update_my_account():
    pass


@account_router.get("/{user_id}")
def get_user_account(user_id: UUID, session: Session=Depends(get_db)):
    return AccountManager.get_user_by_id(id=user_id, session=session)


#! NOT FINISH
@account_router.delete('/{user_id}/delete')
def delete_account(user_id: UUID, session: Session=Depends(get_db)):
    return AccountManager.get_user_by_id(id=user_id, session=session)
