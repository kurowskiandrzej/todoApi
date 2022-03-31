from domain.use_case.insert_task_use_case import InsertTaskUseCase


class TaskViewModelUseCases:
    def __init__(
        self,
        insert_task: InsertTaskUseCase

    ):
        self.insert_task = insert_task
