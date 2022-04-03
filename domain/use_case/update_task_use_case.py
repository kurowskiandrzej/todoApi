from domain.repository.to_do_repository import ToDoRepository


class UpdateTaskUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(
            self,
            user_id: int,
            list_id: int,
            task_id: int,
            value: str,
            progress: dict | None,
            is_completed: bool | None
    ):
        self.__repository.update_task(
            user_id,
            list_id,
            task_id,
            value,
            progress,
            is_completed
        )
