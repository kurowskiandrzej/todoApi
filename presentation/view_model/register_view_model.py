from flask import make_response
from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases


class RegisterViewModel:
    def __init__(self, use_case: RegisterViewModelUseCases):
        self.__use_case = use_case

    @staticmethod
    def register(email, password):
        response = make_response(f'response success email: {email} password: {password}')
        response.status_code = 200

        return response