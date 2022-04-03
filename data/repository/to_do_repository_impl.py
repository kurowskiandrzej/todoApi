from domain.repository.to_do_repository import ToDoRepository
from data.db.to_do_dao import ToDoDao


class ToDoRepositoryImpl(ToDoRepository):
    def login(self, email: str) -> dict | None:
        return ToDoDao.login(email)

    def register(self, email: str, password_hash: str) -> int:
        return ToDoDao.register(email, password_hash)

    def post_list(self, user_id: int, name: str) -> int:
        return ToDoDao.insert_to_do_list(user_id, name)

    def update_to_do_list(
            self,
            user_id: int,
            list_id: int,
            updated_name: str
    ):
        ToDoDao.update_to_do_list(user_id, list_id, updated_name)

    def get_all_lists(self, user_id: int) -> list:
        return ToDoDao.get_all_to_do_lists(user_id)

    def delete_to_do_list(self, user_id: int, list_id: int):
        ToDoDao.delete_to_do_list(user_id, list_id)

    def insert_task(
            self,
            user_id: int,
            list_id: int,
            task_value: str
    ) -> int:
        return ToDoDao.insert_task(
            user_id,
            list_id,
            task_value
        )

    def insert_task_with_progress(
            self,
            user_id: int,
            list_id: int,
            task_value: str,
            start: int,
            end: int,
            current: int
    ) -> int:
        return ToDoDao.insert_task_with_progress(
            user_id,
            list_id,
            task_value,
            start,
            end,
            current
        )

    def get_all_tasks_from_list(self, user_id: int, list_id: int) -> list:
        return ToDoDao.get_all_tasks_from_list(user_id, list_id)

    def delete_task(
            self,
            user_id: int,
            list_id: int,
            task_id: int
    ):
        ToDoDao.delete_task(user_id, list_id, task_id)
