import flask
from flask import Flask, Blueprint, request, make_response

from dependency_injection.di import resolve
from presentation.view_model.login_view_model import LoginViewModel
from localization.locales import get_string_resource

login_view = Blueprint('login_view', __name__, url_prefix='/api')


def get_view_model(app: Flask) -> LoginViewModel:
    if app.config['TESTING']:
        return resolve('LoginViewModelFake')
    else:
        return resolve(LoginViewModel)


@login_view.route('/login', methods=['POST'])
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
    if ['string_resource_id'] in response_data:
        response.data = get_string_resource(locale, response_data['string_resource_id'])

    return response
