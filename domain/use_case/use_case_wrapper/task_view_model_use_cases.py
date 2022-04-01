from domain.use_case.insert_task_use_case import InsertTaskUseCase
from domain.use_case.delete_task_use_case import DeleteTaskUseCase


class TaskViewModelUseCases:
    def __init__(
        self,
        insert_task: InsertTaskUseCase,
        delete_task: DeleteTaskUseCase
    ):
        self.insert_task = insert_task
        self.delete_task = delete_task
