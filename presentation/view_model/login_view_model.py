from flask import Response, make_response

from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from localization.locales import get_string_resource


class LoginViewModel:
    def __init__(self, use_case: LoginViewModelUseCases):
        self.__use_case = use_case

    def login(self, email: str, password: str, locale: str) -> Response:
        if self.__use_case.validate_email(email) is False:
            response = make_response(get_string_resource(locale, 'incorrect_email_format'))
            response.status_code = 401
            return response

        if self.__use_case.validate_password(password) is False:
            response = make_response(get_string_resource(locale, 'incorrect_password'))
            response.status_code = 401
            return response

        response = self.__use_case.login_user.login(email, password, locale)
        return response
