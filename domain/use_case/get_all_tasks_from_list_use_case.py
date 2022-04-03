from domain.repository.to_do_repository import ToDoRepository


class GetAllTasksFromListUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, user_id: int, list_id: int) -> list:
        return self.__repository.get_all_tasks_from_list(user_id, list_id)