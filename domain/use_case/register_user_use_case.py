class RegisterUserUseCase:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

    def register(self, email: str) -> Response:
        password = self.repository.get_password_by_email(email)

        if password is None:
            response = make_response(get_string_resource(g.locale, 'no_such_user'))
            response.status_code = 401
            return response

        return Response()
