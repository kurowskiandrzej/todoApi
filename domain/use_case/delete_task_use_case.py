from domain.repository.to_do_repository import ToDoRepository


class DeleteTaskUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(self, user_id, list_id: int, task_id):
        self.__repository.delete_task(user_id, list_id, task_id)
