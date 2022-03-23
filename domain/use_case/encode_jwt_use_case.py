import datetime

import jwt

from common.constants import JWT_ALGORITHM, JWT_LIFESPAN


class EncodeJwtUseCase:
    """Generates new access token"""
    def __call__(self, secret: str, user_id: int) -> str:
        return jwt.encode(
            payload={
                'uid': user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=JWT_LIFESPAN)
            },
            key=secret,
            algorithm=JWT_ALGORITHM
        )
