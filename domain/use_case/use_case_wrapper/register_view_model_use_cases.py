from domain.use_case.register_user_use_case import RegisterUserUseCase


class RegisterViewModelUseCases:
    def __init__(self, register_user: RegisterUserUseCase):
        self.register_user = register_user
