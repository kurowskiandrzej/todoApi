from domain.use_case.insert_task_use_case import InsertTaskUseCase
from domain.use_case.delete_task_use_case import DeleteTaskUseCase
from domain.use_case.validate_task_value_use_case import ValidateTaskValueUseCase
from domain.use_case.validate_task_progress_use_case import ValidateTaskProgressUseCase
from domain.use_case.decode_jwt_use_case import DecodeJwtUseCase
from domain.use_case.get_all_tasks_from_list_use_case import GetAllTasksFromListUseCase


class TaskViewModelUseCases:
    def __init__(
            self,
            decode_jwt: DecodeJwtUseCase,
            validate_task_value: ValidateTaskValueUseCase,
            insert_task: InsertTaskUseCase,
            delete_task: DeleteTaskUseCase,
            validate_task_progress: ValidateTaskProgressUseCase,
            get_all_tasks_from_list: GetAllTasksFromListUseCase
    ):
        self.decode_jwt = decode_jwt
        self.validate_task_value = validate_task_value
        self.insert_task = insert_task
        self.delete_task = delete_task
        self.validate_task_progress = validate_task_progress
        self.get_all_tasks_from_list = get_all_tasks_from_list
