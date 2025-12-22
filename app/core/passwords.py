from argon2 import PasswordHasher


ph = PasswordHasher()


def create_password_hash(password: str) -> str:
    return ph.hash(password)


def check_password_hash(password: str, hash: str) -> bool:
    return ph.verify(hash, password)
