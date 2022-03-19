import flask
from flask import Blueprint, request

from dependency_injection.di import inject
from presentation.view_model.login_view_model import LoginViewModel

login_view = Blueprint('login_view', __name__, url_prefix='/api')


def get_view_model(app):
    if app.config['TESTING']:
        view_model = inject('LoginViewModelFake')
    else:
        view_model = inject(LoginViewModel)
    return view_model


@login_view.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    response = get_view_model(flask.current_app).login(email, password)

    return response
