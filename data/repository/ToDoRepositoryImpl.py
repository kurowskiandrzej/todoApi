from domain.repository.ToDoRepository import ToDoRepository
from data.db.ToDoDao import ToDoDao


class ToDoRepositoryImpl(ToDoRepository):
    def get_password_by_email(self, email: str):
        ToDoDao.get_password_by_email(email)

    def register(self, email: str, password: str):
        ToDoDao.register(email, password)
