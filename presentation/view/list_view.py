import os

import flask
import jwt
from flask import Flask, Blueprint, request, jsonify, make_response
from sqlalchemy import exc

from dependency_injection.di import resolve
from presentation.view_model.list_view_model import ListViewModel
from domain.helper.jwt_helper import JWTHelper
from localization.locales import get_string_resource

list_view = Blueprint('list_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> ListViewModel:
    if app.config['TESTING']:
        return resolve('ListViewModelFake')
    else:
        return resolve(ListViewModel)


@list_view.post('/todo<list_name>')
def post_list(list_name):
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']
    locale = request.headers.get('Accept-Language')

    try:
        list_id = view_model.post_list(user_id, list_name)
    except exc.IntegrityError:
        response = make_response()
        response.status_code = 401
        response.data = get_string_resource(locale, 'list_with_name_already_exists')
        return response

    return jsonify({'list_id': list_id})


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
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()


@list_view.delete('/todo')
def delete_list():
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()
