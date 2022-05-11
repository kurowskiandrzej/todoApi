import os

import flask
from flask import Flask, Blueprint, request, make_response
from common import constants

from dependency_injection.container import resolve
from localization.locales import get_string_resource
from presentation.view_model.login_view_model import LoginViewModel

login_view = Blueprint('login_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> LoginViewModel:
    if app.config['TESTING']:
        return resolve('LoginViewModelFake')
    else:
        return resolve(LoginViewModel)


@login_view.post('/login')
def login():
    view_model = get_view_model(flask.current_app)

    email = request.form['email']
    password = request.form['password']

    locale = request.headers.get('Accept-Language')

    response_data = view_model.login(
        email,
        password
    )

    response = make_response()
    response.status_code = response_data['status_code']
    if 'string_resource_id' in response_data:
        response.data = get_string_resource(locale, response_data['string_resource_id'])
    else:
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


@login_view.post('/logout')
def logout():
    response = make_response()
    response.delete_cookie('token', path='/', domain=constants.WEB_CLIENT_URL)
    response.status_code = 200

    return response
