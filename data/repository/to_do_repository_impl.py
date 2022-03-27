from domain.repository.to_do_repository import ToDoRepository
from data.db.to_do_dao import ToDoDao


class ToDoRepositoryImpl(ToDoRepository):
    def login(self, email: str) -> dict | None:
        return ToDoDao.login(email)

    def register(self, email: str, password_hash: str) -> int:
        return ToDoDao.register(email, password_hash)

    def get_all_lists(self, user_id: int) -> list:
        return ToDoDao.get_all_to_do_lists(user_id)
