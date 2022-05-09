import os

import flask
import jwt
from flask import Flask, Blueprint, request, jsonify, make_response
from sqlalchemy import exc

from dependency_injection.container import resolve
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


@list_view.post('/todo')
def post_list():
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_data = request.get_json()
    list_name = user_data['list_name'].strip()
    locale = request.headers.get('Accept-Language')
    user_id = token_data['uid']

    if view_model.validate_list_name(list_name) is False:
        response = make_response()
        response.status_code = 403
        response.data = get_string_resource(locale, 'incorrect_name')
        return response

    try:
        list_id, created_on = view_model.post_list(user_id, list_name)
    except exc.IntegrityError:
        response = make_response()
        response.status_code = 409
        response.data = get_string_resource(locale, 'list_with_name_already_exists')
        return response

    return jsonify({
        'list_id': list_id,
        'created_on': created_on
    }), 200


@list_view.get('/todo')
def get_all_lists():
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    lists = view_model.get_all_lists(token_data['uid'])

    return jsonify({'lists': lists}), 200


@list_view.patch('/todo/<int:list_id>')
def patch_list(list_id):
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    updated_name = (request.args.get('updated_name')).strip()
    locale = request.headers.get('Accept-Language')
    user_id = token_data['uid']
    response = make_response()

    if view_model.validate_list_name(updated_name) is False:
        response.status_code = 403
        response.data = get_string_resource(locale, 'incorrect_name')
        return response

    try:
        view_model.update_list(user_id, list_id, updated_name)
    except exc.IntegrityError:
        response.status_code = 409
        response.data = get_string_resource(locale, 'list_with_name_already_exists')
        return response

    response.status_code = 200

    return response


@list_view.delete('/todo/<int:list_id>')
def delete_list(list_id):
    view_model = get_view_model(flask.current_app)
    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']

    view_model.delete_list(user_id, list_id)

    response = make_response()
    response.status_code = 200

    return response
