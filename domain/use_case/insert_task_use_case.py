from domain.repository.to_do_repository import ToDoRepository


class InsertTaskUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(
            self,
            user_id: int,
            list_id: int,
            value: str,
            start: int | None,
            end: int | None,
            current: int | None

    ) -> int:
        return self.__repository.insert_task(
            user_id,
            list_id,
            value,
            start,
            end,
            current
        )
