from data.db.postgres import db


class ToDoDao:
    @staticmethod
    def login(email: str) -> dict | None:
        result = db.execute(
            """
            SELECT id, password 
            FROM user_account
            WHERE email = %s
            """, [email]
        ).fetchone()

        if result is None:
            return None

        user_id, hashed_password = result

        return {
            'user_id': user_id,
            'hashed_password': hashed_password
        }

    @staticmethod
    def register(email: str, password_hash: str) -> int:
        result = db.execute(
            """
            INSERT INTO user_account (email, password, created_on) 
            VALUES (%s, %s, CURRENT_TIMESTAMP) 
            RETURNING id
            """, email, password_hash
        ).fetchone()

        user_id, = result

        return user_id

    @staticmethod
    def insert_to_do_list(user_id: int, name: str) -> int:
        result = db.execute(
            """
            INSERT INTO to_do_list (user_id, name, created_on) 
            VALUES (%s, %s, CURRENT_TIMESTAMP) 
            RETURNING id
            """, user_id, name
        ).fetchone()

        list_id, = result

        return list_id

    @staticmethod
    def get_all_to_do_lists(user_id: int) -> list:
        data = db.execute(
            """
            SELECT id, name, created_on 
            FROM to_do_list
            WHERE user_id = %s
            """, [user_id]
        ).fetchall()

        result = []

        for row in data:
            list_id, name, created_on = row
            result.append({
                'id': list_id,
                'name': name,
                'created': created_on
            })

        return result

    @staticmethod
    def update_to_do_list(user_id: int, list_id: int, updated_name: str):
        db.execute(
            """
            UPDATE to_do_list
            SET name = %s
            WHERE user_id = %s 
            AND id = %s
            """, updated_name, user_id, list_id
        )

    @staticmethod
    def delete_to_do_list(user_id: int, list_id: int):
        db.execute(
            """
            DELETE FROM to_do_list
            WHERE id = %s
            AND user_id = %s
            """, list_id, user_id
        )

    @staticmethod
    def to_do_list_exists(user_id: int, list_id: int) -> bool:
        list_exists, = db.execute(
            """
            SELECT EXISTS (
                SELECT 1 FROM to_do_list
                WHERE user_id = %s
                AND id = %s
            )
            """, user_id, list_id
        ).fetchone()

        return list_exists

    @staticmethod
    def insert_task(
            user_id: int,
            list_id: int,
            task_value: str
    ) -> int | None:
        if ToDoDao.to_do_list_exists(user_id, list_id) is False:
            return None

        task_id, = db.execute(
            """
            INSERT INTO task (list_id, value, created_on)
            VALUES (%s, %s, CURRENT_TIMESTAMP)
            RETURNING id
            """, list_id, task_value
        ).fetchone()

        return task_id

    @staticmethod
    def insert_task_with_progress(
            user_id: int,
            list_id: int,
            task_value: str,
            start: int,
            end: int,
            current: int
    ) -> int | None:
        if ToDoDao.to_do_list_exists(user_id, list_id) is False:
            return None

        task_id, = db.execute(
            """
            INSERT INTO task (list_id, value, created_on)
            VALUES (%s, %s, CURRENT_TIMESTAMP)
            RETURNING id
            """, list_id, task_value
        ).fetchone()

        db .execute(
            """
            INSERT INTO task_progress (task_id, start_value, end_value, current_progress)
            VALUES (%s, %s, %s, %s)
            """, task_id, start, end, current
        )

        return task_id

    @staticmethod
    def get_all_tasks_from_list(user_id: int, list_id: int) -> list:
        data = db.execute(
            """
            SELECT task.id, value, is_completed, completed_on, start_value, end_value, current_progress 
            FROM task
            LEFT JOIN task_progress
            ON id = task_id
            JOIN to_do_list
            ON to_do_list.id = list_id
            WHERE user_id = %s
            AND to_do_list.id = %s
            """, user_id, list_id
        )

        tasks = []
        for row in data:
            task_id, value, is_completed, completed_on, start, end, current = row
            tasks.append({
                'id': task_id,
                'list_id': list_id,
                'value': value,
                'is_completed': is_completed,
                'completed_on': completed_on,
                'start': start,
                'end': end,
                'current': current
            })

        return tasks

    @staticmethod
    def update_task_value(
            user_id: int,
            list_id: int,
            task_id: int,
            value: str
    ):
        db.execute(
            """
            UPDATE task
            SET value = %s
            JOIN to_do_list
            ON to_do_list.id = list_id
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """, value, user_id, list_id, task_id
        )

    @staticmethod
    def update_task_progress(
            user_id: int,
            list_id: int,
            task_id: int,
            start: int,
            end: int,
            current: int
    ):
        db.execute(
            """
            UPDATE task_progress
            SET start_value = %s, end_value = %s, current_progress = %s
            JOIN task
            ON task.id = task_id
            JOIN to_do_list
            ON to_do_list.id = list_id
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """, start, end, current, user_id, list_id, task_id
        )

    @staticmethod
    def set_task_as_completed(
            user_id: int,
            list_id: int,
            task_id: int,
    ):
        db.execute(
            """
            UPDATE task
            JOIN to_do_list
            ON to_do_list.id = list_id
            SET is_completed = TRUE, completed_on = CURRENT_TIMESTAMP
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """
        ), user_id, list_id, task_id

    @staticmethod
    def set_task_as_not_completed(
            user_id: int,
            list_id: int,
            task_id: int,
    ):
        db.execute(
            """
            UPDATE task
            JOIN to_do_list
            ON to_do_list.id = list_id
            SET is_completed = FALSE, completed_on = NULL
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """
        ), user_id, list_id, task_id

    @staticmethod
    def delete_task(user_id: int, list_id: int, task_id: int):
        db.execute(
            """
            DELETE FROM task
            JOIN to_do_list
            ON list_id = to_do_list.id
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """, user_id, list_id, task_id
        )
