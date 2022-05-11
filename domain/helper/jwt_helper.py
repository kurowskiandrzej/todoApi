from flask import make_response


class JWTHelper:
    @staticmethod
    def create_invalid_jwt_response():
        """
        Returns empty response with 401 status code
        that clears token from user's browser
        """
        response = make_response()
        response.set_cookie(
            key='token',
            value='',
            secure=True,
            httponly=True,
            samesite='None',
            expires=0
        )
        response.status_code = 401

        return response
