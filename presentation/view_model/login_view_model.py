from flask import g, Response, make_response
from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from localization.locales import get_string_resource


class LoginViewModel:
    def __init__(self, use_case: LoginViewModelUseCases):
        self.use_case = use_case

    def login(self, email, password) -> Response:
        if self.use_case.validate_email(email) is False:
            response = make_response(get_string_resource(g.locale, 'incorrect_email_format'))
            response.status_code = 401
            return response

        if self.use_case.validate_password(password) is False:
            response = make_response(get_string_resource(g.locale, 'incorrect_password'))
            response.status_code = 401
            return response

        response = self.use_case.login_user.login(email, password)
        return response
