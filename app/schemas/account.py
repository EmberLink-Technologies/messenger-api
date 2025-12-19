from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserRegistrationIn(BaseModel):
    # later add validators for this model
    email: EmailStr
    full_name: str
    username: str
    password: str


class UserRegistrationOut(BaseModel):
    email: EmailStr
    full_name: str
    username: str


class UserSearch(BaseModel):
    field: str
    value: str | UUID
