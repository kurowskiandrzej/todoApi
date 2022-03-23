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
    def insert_to_do():
        pass
