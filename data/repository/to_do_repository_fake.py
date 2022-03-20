from werkzeug.security import generate_password_hash

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

    def get_password_hash_by_user_email(self, email: str) -> str | None:
        if email not in self.__user_email_with_password:
            return None
        return self.__user_email_with_password[email]

    def register(self, email: str, password: str):
        pass
