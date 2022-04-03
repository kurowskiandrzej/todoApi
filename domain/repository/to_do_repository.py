import abc


class ToDoRepository(abc.ABC):
    @abc.abstractmethod
    def login(self, email: str) -> dict | None:
        pass

    @abc.abstractmethod
    def register(self, email: str, password: str) -> int:
        pass

    @abc.abstractmethod
    def post_list(self, user_id: int, name: str) -> int:
        pass

    @abc.abstractmethod
    def update_to_do_list(
            self,
            user_id: int,
            list_id: int,
            updated_name: str
    ):
        pass

    @abc.abstractmethod
    def get_all_lists(self, user_id: int) -> list:
        pass

    @abc.abstractmethod
    def delete_to_do_list(self, user_id: int, list_id: int):
        pass

    @abc.abstractmethod
    def insert_task(
            self,
            user_id: int,
            list_id: int,
            task_value: str,
            start: int | None,
            end: int | None,
            current: int | None
    ) -> int:
        pass

    @abc.abstractmethod
    def get_all_tasks_from_list(
            self,
            user_id: int,
            list_id: int
    ) -> list:
        pass

    @abc.abstractmethod
    def update_task(
            self,
            user_id: int,
            list_id: int,
            task_id: int,
            value: str,
            start: int,
            end: int,
            current: int,
            is_completed: bool
    ):
        pass

    @abc.abstractmethod
    def delete_task(
            self,
            user_id: int,
            list_id: int,
            task_id: int
    ):
        pass
