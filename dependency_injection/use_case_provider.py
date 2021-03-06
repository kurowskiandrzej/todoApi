from data.repository.to_do_repository_fake import ToDoRepositoryFake
from dependency_injection.repository_provider import repositories
from domain.repository.to_do_repository import ToDoRepository
from domain.use_case.delete_completed_tasks_from_list_use_case import DeleteCompletedTasksFromListUseCase
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
from domain.use_case.insert_list_use_case import InsertListUseCase
from domain.use_case.validate_list_name_use_case import ValidateListNameUseCase
from domain.use_case.update_list_name_use_case import UpdateListNameUseCase
from domain.use_case.delete_list_use_case import DeleteListUseCase
from domain.use_case.use_case_wrapper.task_view_model_use_cases import TaskViewModelUseCases
from domain.use_case.insert_task_use_case import InsertTaskUseCase
from domain.use_case.delete_task_use_case import DeleteTaskUseCase
from domain.use_case.validate_task_value_use_case import ValidateTaskValueUseCase
from domain.use_case.validate_task_progress_use_case import ValidateTaskProgressUseCase
from domain.use_case.get_all_tasks_from_list_use_case import GetAllTasksFromListUseCase
from domain.use_case.update_task_use_case import UpdateTaskUseCase

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
        InsertListUseCase(repositories[ToDoRepository]),
        DeleteListUseCase(repositories[ToDoRepository]),
        UpdateListNameUseCase(repositories[ToDoRepository]),
        ValidateListNameUseCase()
    ),
    'ListViewModelUseCasesFake': ListViewModelUseCases(
        DecodeJwtUseCase(),
        GetAllListsUseCase(repositories[ToDoRepositoryFake]),
        InsertListUseCase(repositories[ToDoRepositoryFake]),
        DeleteListUseCase(repositories[ToDoRepositoryFake]),
        UpdateListNameUseCase(repositories[ToDoRepositoryFake]),
        ValidateListNameUseCase()
    ),
    TaskViewModelUseCases: TaskViewModelUseCases(
        DecodeJwtUseCase(),
        ValidateTaskValueUseCase(),
        InsertTaskUseCase(repositories[ToDoRepository]),
        DeleteTaskUseCase(repositories[ToDoRepository]),
        ValidateTaskProgressUseCase(),
        GetAllTasksFromListUseCase(repositories[ToDoRepository]),
        UpdateTaskUseCase(repositories[ToDoRepository]),
        DeleteCompletedTasksFromListUseCase(repositories[ToDoRepository])
    ),
    'TaskViewModelUseCasesFake': TaskViewModelUseCases(
        DecodeJwtUseCase(),
        ValidateTaskValueUseCase(),
        InsertTaskUseCase(repositories[ToDoRepositoryFake]),
        DeleteTaskUseCase(repositories[ToDoRepositoryFake]),
        ValidateTaskProgressUseCase(),
        GetAllTasksFromListUseCase(repositories[ToDoRepositoryFake]),
        UpdateTaskUseCase(repositories[ToDoRepositoryFake]),
        DeleteCompletedTasksFromListUseCase(repositories[ToDoRepositoryFake])
    )
}
