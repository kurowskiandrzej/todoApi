from domain.repository.to_do_repository import ToDoRepository
from data.db.to_do_dao import ToDoDao


class ToDoRepositoryImpl(ToDoRepository):
    def get_password_hash_by_user_email(self, email: str):
        ToDoDao.get_password_by_email(email)

    def register(self, email: str, password: str):
        ToDoDao.register(email, password)
