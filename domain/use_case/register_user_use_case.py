from domain.repository.to_do_repository import ToDoRepository
from werkzeug.security import generate_password_hash
from common.constants import PASSWORD_HASH_METHOD, SALT_LENGTH


class RegisterUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, email: str, password: str) -> int:
        hashed_password = generate_password_hash(
            password,
            method=PASSWORD_HASH_METHOD,
            salt_length=SALT_LENGTH
        )

        return self.__repository.register(email, hashed_password)
