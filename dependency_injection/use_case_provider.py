from domain.use_case.use_case_wrapper.LoginViewModelUseCases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.RegisterViewModelUseCases import RegisterViewModelUseCases
from dependency_injection.repository_provider import repositories
from domain.repository.ToDoRepository import ToDoRepository


use_cases = {
    LoginViewModelUseCases: LoginViewModelUseCases(repositories[ToDoRepository]),
    RegisterViewModelUseCases: RegisterViewModelUseCases(repositories[ToDoRepository])
}
