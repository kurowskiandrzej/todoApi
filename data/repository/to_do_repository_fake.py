from werkzeug.security import generate_password_hash
from sqlalchemy import exc

from common.constants import SALT_LENGTH, PASSWORD_HASH_METHOD
from domain.repository.to_do_repository import ToDoRepository


class ToDoRepositoryFake(ToDoRepository):
    __hashed_password = generate_password_hash(
        'MyV4L!DPassword',
        method=PASSWORD_HASH_METHOD,
        salt_length=SALT_LENGTH
    )

    __user_email_with_password = {
        'user@mail.com': __hashed_password
    }

    def login(self, email: str) -> dict | None:
        hashed_password = self.__user_email_with_password.get(email)

        if hashed_password is None:
            return None

        return {
            'user_id': 1,
            'hashed_password': hashed_password
        }

    def register(self, email: str, password: str) -> int:
        if email in self.__user_email_with_password:
            raise exc.IntegrityError("user already exists", None, None)
        return len(self.__user_email_with_password)

    def get_all_lists(self, user_id: int) -> list:
        return [
            {
                'id': 1,
                'name': 'first',
                'created': '01-01-2000'
            },
            {
                'id': 2,
                'name': 'second',
                'created': '01-01-2000'
            }
        ]
