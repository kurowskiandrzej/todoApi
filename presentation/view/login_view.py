import flask
from flask import Flask, Blueprint, request, g

from dependency_injection.di import inject
from presentation.view_model.login_view_model import LoginViewModel

login_view = Blueprint('login_view', __name__, url_prefix='/api')


def get_view_model(app: Flask) -> LoginViewModel:
    if app.config['TESTING']:
        return inject('LoginViewModelFake')
    else:
        return inject(LoginViewModel)


@login_view.route('/login', methods=['POST'])
def login():
    view_model = get_view_model(flask.current_app)

    email = request.form['email']
    password = request.form['password']

    locale = request.headers.get('Accept-Language')

    response = view_model.login(
        email,
        password,
        locale
    )

    return response
