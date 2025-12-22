from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer

import jwt

from .config import SECRET_KEY, ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(payload: dict):
    to_encode = payload.copy()
    expire = datetime.now() + timedelta(hours=1)
    to_encode.update({'exp': expire})
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)


def create_refresh_token():
    pass


def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, ALGORITHM)
