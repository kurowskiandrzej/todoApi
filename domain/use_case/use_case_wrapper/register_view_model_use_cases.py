from domain.use_case.register_user_use_case import RegisterUserUseCase
from domain.use_case.validate_email_use_case import ValidateEmailUseCase
from domain.use_case.validate_password_use_case import ValidatePasswordUseCase


class RegisterViewModelUseCases:
    def __init__(
            self,
            register_user: RegisterUserUseCase,
            validate_email: ValidateEmailUseCase,
            validate_password: ValidatePasswordUseCase
    ):
        self.register_user = register_user
        self.validate_email = validate_email
        self.validate_password = validate_password
