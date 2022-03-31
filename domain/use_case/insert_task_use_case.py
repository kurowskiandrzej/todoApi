from domain.repository.to_do_repository import ToDoRepository


class InsertTaskUseCase:
    def __init__(self, repository: ToDoRepository):
        self.__repository = repository

    def __call__(
            self,
            user_id: int,
            list_id: int,
            task: dict

    ):
        if 'start' in task:
            self.__repository.insert_task_with_progress(
                user_id,
                list_id,
                task['value'],
                task['start'],
                task['end'],
                task['current']
            )
        else:
            pass