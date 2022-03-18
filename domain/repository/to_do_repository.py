import abc


class ToDoRepository(abc.ABC):
    @abc.abstractmethod
    def get_password_hash_by_user_email(self, email: str):
        pass

    @abc.abstractmethod
    def register(self, email: str, password: str):
        pass
