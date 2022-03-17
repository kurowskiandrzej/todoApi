from werkzeug.security import generate_password_hash, check_password_hash
from domain.repository.ToDoRepository import ToDoRepository
from flask import g, make_response, Response
from localization.locales import get_string_resource


class LoginUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

    def login(self, email: str) -> Response:
        password = self.repository.get_password_by_email(email)

        if password is None:
            response = make_response(get_string_resource(g.locale, 'no_such_user'))
            response.status_code = 401
            return response

        return Response()
