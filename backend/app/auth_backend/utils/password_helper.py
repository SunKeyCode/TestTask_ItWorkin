from typing import Optional, Tuple

from passlib.context import CryptContext


class PasswordHelper:
    def __init__(self, context: Optional[CryptContext] = None) -> None:
        if context is None:
            self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        else:
            self.context = context  # pragma: no cover

    def verify_and_update(
            self, plain_password: str, hashed_password: str
    ) -> Tuple[bool, str]:
        return self.context.verify_and_update(plain_password, hashed_password)

    def verify(self, password: str, hashed_password: str):
        return self.context.verify(secret=password, hash=hashed_password)

    def hash(self, password: str) -> str:
        return self.context.hash(password)
