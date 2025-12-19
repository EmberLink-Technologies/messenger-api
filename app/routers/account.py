from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.account import UserSearch
from handlers.account import AccountManager

account_router = APIRouter(prefix="/account")


@account_router.get("/myself")
def get_my_account():
    pass


@account_router.patch("/myself")
def update_my_account():
    pass


@account_router.get("/{user_id}")
def get_user_account():
    pass


@account_router.delete('/{user_id}/delete')
def delete_account(user_id: UUID, session: Session = Depends(get_db)):
    user = UserSearch(field='id', value=user_id)
    return AccountManager.delete_user(session, user)
