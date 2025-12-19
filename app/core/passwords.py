from argon2 import PasswordHasher


ph = PasswordHasher()


def create_password(password: str) -> str:
    return ph.hash(password)


def check_password(password: str, hash: str) -> bool:
    return ph.verify(hash, password)
