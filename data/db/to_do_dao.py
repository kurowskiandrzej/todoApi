from data.db.postgres import db


class ToDoDao:
    @staticmethod
    def get_password_by_email(email: str) -> str | None:
        user_id = db.execute(
            """
            SELECT password FROM user_account
            WHERE email = %s
            """, [email]
        ).fetchone()

        return user_id

    @staticmethod
    def register(email: str, password_hash: str) -> int:
        user_id = db.execute(
            """
            INSERT INTO user_account (email, password, created_on) 
            VALUES (%s, %s, CURRENT_TIMESTAMP) 
            RETURNING id
            """, email, password_hash
        ).fetchone()

        return user_id

    @staticmethod
    def insert_to_do():
        pass
