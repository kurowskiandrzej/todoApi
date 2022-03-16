from flask import Blueprint

login_view = Blueprint('login_view', __name__, url_prefix='/api')


@login_view.route('/login', methods=['POST'])
def login():
    return 'ok', 200
