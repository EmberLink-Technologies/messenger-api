from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import update, select
from sqlalchemy.exc import NoResultFound

from ..models.account import Account
from ..schemas.account import UserInDB


class AccountManager:
    @classmethod
    def create_user(cls, session: Session, data: UserInDB):
        new_account = Account(
            email=data.email,
            full_name=data.full_name,
            username=data.username,
            password=data.password
        )
        session.add(new_account)
        return new_account

    @classmethod
    def get_user_by_id(cls, session: Session, id: UUID):
        #! Later add exception and validation
        return session.get(Account, id)

    @classmethod
    def get_user_by_email(cls, session: Session, email: str):
        #! Later add exception and validation
        stmt = (
            select(Account)
            .where(Account.email == email)
        )
        return session.execute(stmt).scalar_one_or_none()

    @classmethod
    def get_user_by_username(cls, session: Session, username: str):
        #! Later add exception and validation
        stmt = (
            select(Account)
            .where(Account.username == username)
        )
        return session.execute(stmt).scalar_one_or_none()

    @classmethod
    def update_user(cls, session: Session, user_id: UUID, data: dict[str, Any]):
        #! Later add exception and validation
        stmt = (
            update(Account)
            .where(Account.id == user_id)
            .values(**data)
            .returning(Account)
        )
        return session.execute(stmt).scalar_one_or_none()
       
    @classmethod
    def delete_user(cls, session: Session, user_id: UUID):
        to_delete_account = AccountManager.get_user_by_id(session, user_id)
        if not to_delete_account:
            raise NoResultFound('Account doesn\'t exists')
        session.delete(to_delete_account)
        return to_delete_account
