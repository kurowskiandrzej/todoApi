from werkzeug.security import check_password_hash

from domain.repository.to_do_repository import ToDoRepository


class LoginUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

    def login(self, email: str, password: str) -> dict:
        hashed_pwd = self.repository.get_password_hash_by_user_email(email)

        if hashed_pwd is None:
            return {
                'status_code': 401,
                'string_resource_id': 'no_such_user'
            }

        is_password_correct = check_password_hash(
            hashed_pwd,
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
