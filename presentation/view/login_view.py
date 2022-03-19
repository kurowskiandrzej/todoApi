import flask
from flask import Blueprint, request

from dependency_injection.di import inject
from presentation.view_model.login_view_model import LoginViewModel

login_view = Blueprint('login_view', __name__, url_prefix='/api')


login_view_model = inject(LoginViewModel)


@login_view.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    response = login_view_model.login(email, password)

    return response
