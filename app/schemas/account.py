from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    full_name: str
    username: str

class UserInDB(User):
    # later add validators for this model
    password: str
