import os

import flask
import jwt
from flask import Flask, Blueprint, request, jsonify

from dependency_injection.di import resolve
from presentation.view_model.list_view_model import ListViewModel
from domain.helper.jwt_helper import JWTHelper

list_view = Blueprint('list_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> ListViewModel:
    if app.config['TESTING']:
        return resolve('ListViewModelFake')
    else:
        return resolve(ListViewModel)


@list_view.post('/todo')
def post_list():
    pass


@list_view.get('/todo')
def get_list():
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    lists = view_model.get_all_lists(token_data['uid'])

    return jsonify({'lists': lists}), 200


@list_view.patch('/todo')
def patch_list():
    pass


@list_view.delete('/todo')
def delete_list():
    pass
