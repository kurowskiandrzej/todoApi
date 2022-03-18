from domain.repository.to_do_repository import ToDoRepository
from data.db.to_do_dao import ToDoDao


class ToDoRepositoryFake(ToDoRepository):
    user_email_with_password = {
        'user@mail.com': 'MyV4L!DPassword'
    }

    def get_password_by_email(self, email: str):
        return self.user_email_with_password['email']

    def register(self, email: str, password: str):
        ToDoDao.register(email, password)
