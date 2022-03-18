from flask import Blueprint, request
from dependency_injection.di import inject
from presentation.view_model.RegisterViewModel import RegisterViewModel

register_view = Blueprint('register_view', __name__, url_prefix='/api')
register_view_model = inject(RegisterViewModel)


@register_view.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    response = register_view_model.register(email, password)

    return response
