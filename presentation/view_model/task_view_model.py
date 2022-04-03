from domain.use_case.use_case_wrapper.task_view_model_use_cases import TaskViewModelUseCases


class TaskViewModel:
    def __init__(self, use_case: TaskViewModelUseCases):
        self.__use_case = use_case

    def decode_token(self, secret: str, token: str) -> dict:
        return self.__use_case.decode_jwt(secret, token)

    def validate_task_value(self, value: str) -> bool:
        return self.__use_case.validate_task_value(value)

    def validate_task_progress(
            self,
            start_value: int,
            end_value: int,
            current_progress: int
    ) -> bool:
        return self.__use_case.validate_task_progress(
            start_value,
            end_value,
            current_progress
        )

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

    def delete_task(
            self,
            user_id: int,
            list_id: int,
            task_id: int
    ):
        self.__use_case.delete_task(user_id, list_id, task_id)
