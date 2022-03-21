import flask
from flask import Blueprint, request, Flask, make_response
from dependency_injection.di import resolve
from presentation.view_model.register_view_model import RegisterViewModel
from localization.locales import get_string_resource

register_view = Blueprint('register_view', __name__, url_prefix='/api')
register_view_model = resolve(RegisterViewModel)


def get_view_model(app: Flask) -> RegisterViewModel:
    if app.config['TESTING']:
        return resolve('RegisterViewModelFake')
    else:
        return resolve(RegisterViewModel)


@register_view.route('/register', methods=['POST'])
def register():
    view_model = get_view_model(flask.current_app)

    email = request.form['email']
    password = request.form['password']

    locale = request.headers.get('Accept-Language')

    response_data = view_model.register(
        email,
        password
    )

    response = make_response()
    response.status_code = response_data['status_code']
    if ['string_resource_id'] in response_data:
        response.data = get_string_resource(locale, response_data['string_resource_id'])
    elif 'user_id' in response_data:
        response.data = {
            'user_id': response_data['user_id']
        }

    return response
