import os

import flask
from flask import Blueprint, request, Flask, make_response
from sqlalchemy import exc

from dependency_injection.container import resolve
from localization.locales import get_string_resource
from presentation.view_model.register_view_model import RegisterViewModel

register_view = Blueprint('register_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> RegisterViewModel:
    if app.config['TESTING']:
        return resolve('RegisterViewModelFake')
    else:
        return resolve(RegisterViewModel)


@register_view.post('/register')
def register():
    view_model = get_view_model(flask.current_app)

    email = request.form['email'].lower()
    password = request.form['password']

    locale = request.headers.get('Accept-Language')

    response = make_response()

    try:
        response_data = view_model.register(
            email,
            password
        )
    except exc.IntegrityError:
        response.status_code = 401
        response.data = get_string_resource(locale, 'user_already_exists')
        return response

    response.status_code = response_data['status_code']
    if 'string_resource_id' in response_data:
        response.data = get_string_resource(locale, response_data['string_resource_id'])
    elif 'user_id' in response_data:
        token = view_model.get_jwt(
            jwt_secret_key,
            response_data['user_id']
        )

        response.set_cookie(
            key='token',
            value=token,
            secure=True,
            httponly=True,
            samesite='None'
        )

    return response
