from domain.use_case.use_case_wrapper.task_view_model_use_cases import TaskViewModelUseCases


class TaskViewModel:
    def __init__(
        self,
        use_case: TaskViewModelUseCases
    ):
        self.__use_case = use_case

    def insert_task(
            self,
            user_id: int,
            list_id: int,
            task: dict
    ) -> int:
        return self.__use_case.insert_task(
            user_id,
            list_id,
            task
        )
