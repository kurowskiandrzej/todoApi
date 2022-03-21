from werkzeug.security import check_password_hash

from domain.repository.to_do_repository import ToDoRepository


class LoginUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, email: str, password: str) -> dict:
        hashed_password = self.__repository.get_password_hash_by_user_email(email)

        if hashed_password is None:
            return {
                'status_code': 401,
                'string_resource_id': 'no_such_user'
            }

        is_password_correct = check_password_hash(
            hashed_password,
            password
        )

        if is_password_correct is False:
            return {
                'status_code': 401,
                'string_resource_id': 'incorrect_password'
            }

        return {
            'status_code': 200,
            'string_resource_id': None
        }
