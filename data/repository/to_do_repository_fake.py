from werkzeug.security import generate_password_hash

from common.constants import SALT_LENGTH, PASSWORD_HASH_METHOD
from data.db.to_do_dao import ToDoDao
from domain.repository.to_do_repository import ToDoRepository


class ToDoRepositoryFake(ToDoRepository):
    hashed_password = generate_password_hash(
        'MyV4L!DPassword',
        method=PASSWORD_HASH_METHOD,
        salt_length=SALT_LENGTH
    )

    user_email_with_password = {
        'user@mail.com': hashed_password
    }

    def get_password_hash_by_user_email(self, email: str):
        return self.user_email_with_password['email']

    def register(self, email: str, password: str):
        ToDoDao.register(email, password)
