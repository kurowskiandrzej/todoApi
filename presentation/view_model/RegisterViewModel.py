from flask import make_response
from domain.use_case.use_case_wrapper.RegisterViewModelUseCases import RegisterViewModelUseCases


class LoginViewModel:
    def __init__(self, use_case: RegisterViewModelUseCases):
        self.__use_case = use_case

    @staticmethod
    def register(email, password):
        response = make_response(f'response success email: {email} password: {password}')
        response.status_code = 200

        return response
