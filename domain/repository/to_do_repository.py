import abc


class ToDoRepository(abc.ABC):
    @abc.abstractmethod
    def login(self, email: str) -> dict | None:
        pass

    @abc.abstractmethod
    def register(self, email: str, password: str) -> int:
        pass

    @abc.abstractmethod
    def get_all_lists(self, user_id: int) -> list:
        pass
