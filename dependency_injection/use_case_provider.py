from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases
from dependency_injection.repository_provider import repositories
from domain.repository.to_do_repository import ToDoRepository


use_cases = {
    LoginViewModelUseCases: LoginViewModelUseCases(repositories[ToDoRepository]),
    RegisterViewModelUseCases: RegisterViewModelUseCases(repositories[ToDoRepository])
}
