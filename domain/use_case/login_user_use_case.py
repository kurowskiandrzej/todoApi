from werkzeug.security import check_password_hash

from domain.repository.to_do_repository import ToDoRepository


class LoginUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, email: str, password: str) -> dict:
        login_result = self.__repository.login(email)

        if login_result is None:
            return {
                'status_code': 401,
                'string_resource_id': 'no_such_user'
            }

        is_password_correct = check_password_hash(
            login_result['hashed_password'],
            password
        )

        if is_password_correct is False:
            return {
                'status_code': 401,
                'string_resource_id': 'incorrect_password'
            }

        return {
            'user_id': login_result['user_id']
        }
