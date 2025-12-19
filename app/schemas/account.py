from pydantic import BaseModel, EmailStr


class UserRegistrationSchema(BaseModel):
    # later add validators for this model
    email: EmailStr
    full_name: str
    username: str
    password: str


class UserRegistrationOut(BaseModel):
    email: EmailStr
    full_name: str
    username: str
