from flask import Blueprint, request
from dependency_injection.di import resolve
from presentation.view_model.register_view_model import RegisterViewModel

register_view = Blueprint('register_view', __name__, url_prefix='/api')
register_view_model = resolve(RegisterViewModel)


@register_view.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    response = register_view_model.register(email, password)

    return response
