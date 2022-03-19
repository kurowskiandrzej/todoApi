from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases
from domain.use_case.login_user_use_case import LoginUserUseCase
from domain.use_case.validate_email_use_case import ValidateEmailUseCase
from domain.use_case.validate_password_use_case import ValidatePasswordUseCase
from dependency_injection.repository_provider import repositories
from domain.repository.to_do_repository import ToDoRepository


use_cases = {
    LoginViewModelUseCases: LoginViewModelUseCases(
        LoginUserUseCase(repositories[ToDoRepository]),
        ValidateEmailUseCase(),
        ValidatePasswordUseCase()
    ),
    RegisterViewModelUseCases: RegisterViewModelUseCases(repositories[ToDoRepository])
}
