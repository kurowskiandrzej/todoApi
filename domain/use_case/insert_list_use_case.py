from domain.repository.to_do_repository import ToDoRepository


class InsertListUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, user_id: int, name: str) -> int:
        return self.__repository.post_list(user_id, name)
