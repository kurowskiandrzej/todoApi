from data.repository.to_do_repository_fake import ToDoRepositoryFake
from dependency_injection.repository_provider import repositories
from domain.repository.to_do_repository import ToDoRepository
from domain.use_case.encode_jwt_use_case import EncodeJwtUseCase
from domain.use_case.login_user_use_case import LoginUserUseCase
from domain.use_case.register_user_use_case import RegisterUserUseCase
from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases
from domain.use_case.validate_email_use_case import ValidateEmailUseCase
from domain.use_case.validate_password_use_case import ValidatePasswordUseCase
from domain.use_case.use_case_wrapper.list_view_model_use_cases import ListViewModelUseCases
from domain.use_case.decode_jwt_use_case import DecodeJwtUseCase
from domain.use_case.get_all_lists_use_case import GetAllListsUseCase
from domain.use_case.post_list_use_case import PostListUseCase

use_cases = {
    LoginViewModelUseCases: LoginViewModelUseCases(
        LoginUserUseCase(repositories[ToDoRepository]),
        ValidateEmailUseCase(),
        ValidatePasswordUseCase(),
        EncodeJwtUseCase()
    ),
    'LoginViewModelUseCasesFake': LoginViewModelUseCases(
        LoginUserUseCase(repositories[ToDoRepositoryFake]),
        ValidateEmailUseCase(),
        ValidatePasswordUseCase(),
        EncodeJwtUseCase()
    ),
    RegisterViewModelUseCases: RegisterViewModelUseCases(
        RegisterUserUseCase(repositories[ToDoRepository]),
        ValidateEmailUseCase(),
        ValidatePasswordUseCase(),
        EncodeJwtUseCase()
    ),
    ListViewModelUseCases: ListViewModelUseCases(
        DecodeJwtUseCase(),
        GetAllListsUseCase(repositories[ToDoRepository]),
        PostListUseCase(repositories[ToDoRepository])
    ),
    'ListViewModelUseCasesFake': ListViewModelUseCases(
        DecodeJwtUseCase(),
        GetAllListsUseCase(repositories[ToDoRepositoryFake]),
        PostListUseCase(repositories[ToDoRepositoryFake])
    )
}
