import jwt

from .config import SECRET_KEY, ALGORITHM


def create_token(data: dict):
    # I need ot create a schema
    return jwt.encode(data, SECRET_KEY, ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, ALGORITHM)
