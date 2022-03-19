from domain.use_case.login_user_use_case import LoginUserUseCase
from domain.use_case.validate_email_use_case import ValidateEmailUseCase
from domain.use_case.validate_password_use_case import ValidatePasswordUseCase


class LoginViewModelUseCases:
    def __init__(
            self,
            login_user: LoginUserUseCase,
            validate_email: ValidateEmailUseCase,
            validate_password: ValidatePasswordUseCase
    ):
        self.login_user = login_user
        self.validate_email = validate_email
        self.validate_password = validate_password
