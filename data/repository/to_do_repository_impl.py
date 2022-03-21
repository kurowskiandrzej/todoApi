from domain.repository.to_do_repository import ToDoRepository
from data.db.to_do_dao import ToDoDao


class ToDoRepositoryImpl(ToDoRepository):
    def get_password_hash_by_user_email(self, email: str) -> str:
        return ToDoDao.get_password_by_email(email)

    def register(self, email: str, password_hash: str) -> int:
        return ToDoDao.register(email, password_hash)
