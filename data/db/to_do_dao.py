from data.db.postgres import db


class ToDoDao:
    @staticmethod
    def login(email: str) -> dict | None:
        result = db.execute(
            """
            SELECT id, password FROM user_account
            WHERE email = %s
            """, [email]
        ).fetchone()

        if result is None:
            return None

        user_id, hashed_password = result

        print(user_id)

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
            SELECT id, name, created_on FROM to_do_list
            WHERE user_id = user_id
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
    def delete_to_do_list(user_id: int, list_id: int):
        db.execute(
            """
            DELETE FROM to_do_list
            WHERE id = list_id
            AND user_id = user_id
            """, user_id, list_id
        )
