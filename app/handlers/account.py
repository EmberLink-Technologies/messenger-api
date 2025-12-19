from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.exc import NoResultFound

from models.account import Account
from schemas.account import UserRegistrationIn, UserSearch


class AccountManager:
    @classmethod
    def create_user(cls, session: Session, data: UserRegistrationIn):
        new_account = Account(
            email=data.email,
            full_name=data.full_name,
            username=data.username,
            password=data.password
        )
        session.add(new_account)
        return new_account

    @classmethod
    def get_user(cls, session: Session, user: UserSearch):
        # Works only with id, username and email
        if user.field == 'id':
            return session.get(Account, user.value)
        elif user.field in ['email', 'username']:
            field = getattr(Account, user.field)
            return session.query(Account).filter(field == user.value).one_or_none()
        raise AttributeError('Wrong field name')

    @classmethod
    def update_user(cls, session: Session, user: UserSearch, data: dict[str, Any]):
        # Work only for id field as a search field and later I need add validation
        # for fields
        if user.field != "id":
            raise ValueError("Update allowed only by id")
        stmt = (
            update(Account)
            .where(Account.id == user.value)
            .values(**data)
            .returning(Account)
        )
        result = session.execute(stmt).scalar_one_or_none()
        if not result:
            raise NoResultFound('Account doesn\'t exist')
        return result

    @classmethod
    def delete_user(cls, session: Session, user: UserSearch):
        if user.field != "id":
            raise ValueError("Update allowed only by id")
        to_delete_account = AccountManager.get_user(session, user)
        if not to_delete_account:
            raise NoResultFound('Account doesn\'t exists')
        session.delete(to_delete_account)
        return to_delete_account
