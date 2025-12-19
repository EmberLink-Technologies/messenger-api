from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.exc import NoResultFound

from models.account import Account
from schemas.account import UserRegistrationSchema


class AccountManager:
    @classmethod
    def create_user(cls, session: Session, data: UserRegistrationSchema):
        new_account = Account(
            email=data.email,
            full_name=data.full_name,
            username=data.username,
            password=data.password
        )
        session.add(new_account)
        return new_account

    @classmethod
    def get_user(cls, session: Session, search_data: tuple):
        # search data is a tuple with (field_name, value_to_search) data
        #! Need to change tuple to smth more appropriate
        if search_data[0] == 'id':
            return session.get(Account, search_data[1])
        elif search_data[0] in ['email', 'username']:
            field = getattr(Account, search_data[0])
            return session.query(Account).filter(field == search_data[1]).one_or_none()
        raise AttributeError('Wrong field name')

    @classmethod
    def update_user(cls, session: Session, search_data: tuple, data: dict[str, Any]):
        # Here I also use search data but I need to switch it to smth better
        #? but I need to keep in head only one thing, here I use only id value
        if search_data[0] != "id":
            raise ValueError("Update allowed only by id")
        stmt = (
            update(Account)
            .where(Account.id == search_data[1])
            .values(**data)
            .returning(Account)
        )
        result = session.execute(stmt).scalar_one_or_none()
        if not result:
            raise NoResultFound('Account doesn\'t exist')
        return result

    @classmethod
    def delete_user(cls, session: Session, search_data: tuple):
        to_delete_account = AccountManager.get_user(session, search_data)
        if not to_delete_account:
            raise NoResultFound('Account doesn\'t exists')
        session.delete(to_delete_account)
        return to_delete_account
