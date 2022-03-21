from domain.repository.to_do_repository import ToDoRepository
from werkzeug.security import generate_password_hash
from common.constants import PASSWORD_HASH_METHOD, SALT_LENGTH


class RegisterUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

    def register(self, email: str, password: str) -> dict:
        password_hash = generate_password_hash(
            password,
            method=PASSWORD_HASH_METHOD,
            salt_length=SALT_LENGTH
        )


        return {}
