from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases


class LoginViewModel:
    def __init__(self, use_case: LoginViewModelUseCases):
        self.__use_case = use_case

    def login(self, email: str, password: str) -> dict:
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

        login_result = self.__use_case.login_user(email, password)

        if 'string_resource_id' in login_result:
            return login_result

        return {
            'status_code': 200,
            'user_id': login_result['user_id']
        }

    def get_jwt(self, secret: str, user_id: int):
        return self.__use_case.encode_jwt(secret, user_id)
