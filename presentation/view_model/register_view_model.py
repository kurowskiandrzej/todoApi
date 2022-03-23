from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases


class RegisterViewModel:
    def __init__(self, use_case: RegisterViewModelUseCases):
        self.__use_case = use_case

    def register(self, email, password) -> dict:
        if self.__use_case.validate_email(email) is False:
            return {
                'status_code': 401,
                'string_resource_id': 'incorrect_email_format'
            }

        if self.__use_case.validate_password(password) is False:
            return {
                'status_code': 401,
                'string_resource_id': 'incorrect_password'
            }

        user_id = self.__use_case.register_user(email, password)

        return {
            'status_code': 200,
            'user_id': user_id
        }

    def get_jwt(self, secret: str, user_id: int):
        return self.__use_case.encode_jwt(secret, user_id)
