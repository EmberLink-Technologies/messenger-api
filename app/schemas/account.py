from pydantic import BaseModel, EmailStr


class UserRegistrationSchema(BaseModel):
    # later add validators for this model
    #! add password
    email: EmailStr
    full_name: str
    username: str
