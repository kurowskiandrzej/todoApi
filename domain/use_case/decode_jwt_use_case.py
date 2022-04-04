import jwt

from common.constants import JWT_ALGORITHM


class DecodeJwtUseCase:
    """Checks if token is valid and returns token data as dictionary,
    if not - throws exceptions when token was tampered with or is expired
    """
    def __call__(self, secret: str, token: str) -> dict:
        return jwt.decode(
            jwt=token,
            key=secret,
            algorithms=[JWT_ALGORITHM]
        )
