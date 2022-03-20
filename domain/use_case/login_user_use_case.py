from flask import make_response, Response
from werkzeug.security import check_password_hash

from domain.repository.to_do_repository import ToDoRepository
from localization.locales import get_string_resource


class LoginUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

    def login(self, email: str, password: str, locale: str) -> Response:
        hashed_pwd = self.repository.get_password_hash_by_user_email(email)

        if hashed_pwd is None:
            response = make_response(get_string_resource(locale, 'no_such_user'))
            response.status_code = 401
            return response

        is_password_correct = check_password_hash(hashed_pwd, password)

        if is_password_correct is False:
            response = make_response(get_string_resource(locale, 'incorrect_password'))
            response.status_code = 401
            return response

        response = make_response()
        response.status_code = 200
        return response
