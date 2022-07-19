from domain.repository.to_do_repository import ToDoRepository


class DeleteCompletedTasksFromListUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, user_id: int, list_id: int):
        self.__repository.delete_completed_tasks_from_list(user_id, list_id)
