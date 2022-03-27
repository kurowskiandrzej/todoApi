from domain.repository.to_do_repository import ToDoRepository


class GetAllListsUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, user_id: int):
        return self.__repository.get_all_lists(user_id)
