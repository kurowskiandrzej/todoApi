from flask import make_response
from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases


class LoginViewModel:
    def __init__(self, use_case: LoginViewModelUseCases):
        self.__use_case = use_case

    @staticmethod
    def login(email, password):
        response = make_response(f'response success email: {email} password: {password}')
        response.status_code = 200

        return response


