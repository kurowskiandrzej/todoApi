from flask import g, Blueprint, request
from dependency_injection.view_model_provider import view_models
from presentation.view_model.LoginViewModel import LoginViewModel

login_view = Blueprint('login_view', __name__, url_prefix='/api')
login_view_model = view_models[LoginViewModel]


@login_view.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    g.locale = request.headers.get('Accept-Language')

    response = login_view_model.login(email, password)

    return response
