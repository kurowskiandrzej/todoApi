from domain.use_case.use_case_wrapper.LoginViewModelUseCases import LoginViewModelUseCases
from dependency_injection.repository_provider import repositories
from domain.repository.ToDoRepository import ToDoRepository


use_cases = {
    LoginViewModelUseCases: LoginViewModelUseCases(repositories[ToDoRepository])
}
