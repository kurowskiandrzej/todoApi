from domain.repository.ToDoRepository import ToDoRepository
from data.db.ToDoDao import ToDoDao


class ToDoRepositoryFake(ToDoRepository):
    user_email_with_password = {
        'user@mail.com': 'MyV4L!DPassword'
    }

    def get_password_by_email(self, email: str):
        return self.user_email_with_password['email']

    def register(self, email: str, password: str):
        ToDoDao.register(email, password)
