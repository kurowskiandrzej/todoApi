from werkzeug.security import generate_password_hash
from sqlalchemy import exc

from common.constants import SALT_LENGTH, PASSWORD_HASH_METHOD
from domain.repository.to_do_repository import ToDoRepository


class ToDoRepositoryFake(ToDoRepository):
    __hashed_password = generate_password_hash(
        'MyV4L!DPassword',
        method=PASSWORD_HASH_METHOD,
        salt_length=SALT_LENGTH
    )

    __user_email_with_password = {
        'user@mail.com': __hashed_password
    }

    __to_do_lists = [
        {
            'id': 1,
            'name': 'first',
            'created': '01-01-2000'
        },
        {
            'id': 2,
            'name': 'second',
            'created': '01-01-2000'
        }
    ]

    def login(self, email: str) -> dict | None:
        hashed_password = self.__user_email_with_password.get(email)

        if hashed_password is None:
            return None

        return {
            'user_id': 1,
            'hashed_password': hashed_password
        }

    def register(self, email: str, password: str) -> int:
        if email in self.__user_email_with_password:
            raise exc.IntegrityError("user already exists", None, None)
        return len(self.__user_email_with_password)

    def post_list(self, user_id: int, name: str) -> int:
        self.__to_do_lists.append(
            {
                'id': user_id,
                'name': name,
                'created': '01-01-2000'
            }
        )
        return len(self.__to_do_lists)

    def update_to_do_list(self, user_id: int, list_id: int, updated_name: str):
        pass

    def get_all_lists(self, user_id: int) -> list:
        return self.__to_do_lists

    def delete_to_do_list(self, user_id: int, list_id: int):
        pass

    def insert_task(
            self,
            user_id: int,
            list_id: int,
            task_value: str
    ) -> int:
        pass

    def insert_task_with_progress(
            self,
            user_id: int,
            list_id: int,
            task_value: str,
            start: int,
            end: int,
            current: int
    ) -> int:
        pass

    def delete_task(
            self,
            user_id: int,
            list_id: int,
            task_id: int
    ):
        pass
