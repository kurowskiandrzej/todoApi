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
    def insert_to_do_list(user_id: int, name: str) -> (int, str):
        result = db.execute(
            """
            INSERT INTO to_do_list (user_id, name, created_on) 
            VALUES (%s, %s, CURRENT_TIMESTAMP) 
            RETURNING id, created_on
            """, user_id, name
        ).fetchone()

        list_id, created_on = result

        return list_id, created_on

    @staticmethod
    def get_all_to_do_lists(user_id: int) -> list:
        data = db.execute(
            """
            SELECT to_do_list.id, to_do_list.name, to_do_list.created_on, 
                (SELECT COUNT(task.id) FROM task WHERE is_completed = TRUE), 
                (SELECT COUNT(task.id) FROM task)
            from to_do_list
            JOIN task
            ON task.list_id = to_do_list.id
            GROUP BY to_do_list.id
            """, [user_id]
        ).fetchall()

        result = []

        for row in data:
            list_id, name, created_on, finished_tasks, all_tasks = row
            result.append({
                'id': list_id,
                'name': name,
                'created': created_on,
                'finished_tasks': finished_tasks,
                'all_tasks': all_tasks
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
            task_value: str,
            start: int | None,
            end: int | None,
            current: int | None,
            is_completed: bool
    ) -> int | None:
        if ToDoDao.to_do_list_exists(user_id, list_id) is False:
            return None

        task_id, = db.execute(
            """
            INSERT INTO task (list_id, value, is_completed, created_on, progress_start, progress_end, progress_current)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP, %s, %s, %s)
            RETURNING id
            """, list_id, task_value, is_completed, start, end, current
        ).fetchone()

        if is_completed:
            ToDoDao.set_task_as_completed(user_id, list_id, task_id)
        else:
            ToDoDao.set_task_as_not_completed(user_id, list_id, task_id)

        return task_id

    @staticmethod
    def get_all_tasks_from_list(user_id: int, list_id: int) -> list:
        data = db.execute(
            """
            SELECT task.id, value, is_completed, completed_on, progress_start, progress_end, progress_current 
            FROM task
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
            FROM task T
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
            UPDATE task
            SET progress_start = %s, progress_end = %s, progress_current = %s
            FROM task T
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
            SET is_completed = TRUE, completed_on = CURRENT_TIMESTAMP
            FROM task T
            JOIN to_do_list
            ON to_do_list.id = list_id
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """, user_id, list_id, task_id
        )

    @staticmethod
    def set_task_as_not_completed(
            user_id: int,
            list_id: int,
            task_id: int,
    ):
        db.execute(
            """
            UPDATE task
            SET is_completed = FALSE, completed_on = NULL
            FROM task T
            JOIN to_do_list
            ON to_do_list.id = list_id
            WHERE user_id = %s
            AND to_do_list.id = %s
            AND task.id = %s
            """, user_id, list_id, task_id
        )

    @staticmethod
    def delete_task(user_id: int, list_id: int, task_id: int):
        db.execute(
            """
            DELETE FROM task
            WHERE task.id = %s
            AND task.list_id = %s
            AND EXISTS(
                SELECT 1
                FROM to_do_list
                JOIN task
                ON task.list_id = to_do_list.id
                WHERE user_id = %s
            )
            """, task_id, list_id, user_id
        )
