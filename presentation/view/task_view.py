import os

import flask
import jwt
from flask import Flask, Blueprint, request, make_response, jsonify

from domain.helper.jwt_helper import JWTHelper
from dependency_injection.container import resolve
from localization.locales import get_string_resource
from presentation.view_model.task_view_model import TaskViewModel

task_view = Blueprint('task_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> TaskViewModel:
    if app.config['TESTING']:
        return resolve('TaskViewModelFake')
    else:
        return resolve(TaskViewModel)


@task_view.post('/todo/<int:list_id>')
def post_task(list_id):
    view_model = get_view_model(flask.current_app)

    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']
    locale = request.headers.get('Accept-Language')

    task_value = (request.args.get('value')).strip()

    if view_model.validate_task_value(task_value) is False:
        response = make_response()
        response.status_code = 403
        response.data = get_string_resource(locale, 'incorrect_value')

        return response

    start = request.args.get('start')
    end = request.args.get('end')
    current = request.args.get('current')

    if None not in (start, end, current):
        if view_model.validate_task_progress(
                int(start),
                int(end),
                int(current)
        ) is False:
            response = make_response()
            response.status_code = 403
            response.data = get_string_resource(locale, 'incorrect_value')

            return response

    task_id = view_model.insert_task(
        user_id,
        list_id,
        task_value,
        start,
        end,
        current
    )

    return jsonify({'task_id': task_id}), 200


@task_view.get('/todo/<int:list_id>')
def get_tasks_by_list_id(list_id):
    view_model = get_view_model(flask.current_app)

    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']
    tasks = view_model.get_all_tasks_from_list(user_id, list_id)

    return jsonify({'tasks': tasks}), 200


@task_view.patch('/todo/<int:list_id>/<int:task_id>')
def update_task(list_id, task_id):
    view_model = get_view_model(flask.current_app)

    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']
    updates = request.get_json()

    locale = request.headers.get('Accept-Language')

    task_value = updates.get('value')
    if task_value is not None:
        task_value = task_value.strip()
        if view_model.validate_task_value(task_value) is False:
            response = make_response()
            response.status_code = 403
            response.data = get_string_resource(locale, 'incorrect_value')

    progress: dict[str, int | None] | None = None

    if 'start' in updates and 'end' in updates and 'current' in updates:
        progress = {
            'start': updates['start'],
            'end': updates['end'],
            'current': updates['current']
        }

    if progress is not None:
        if progress['start'] is not None \
                and progress['end'] is not None \
                and progress['current'] is not None \
                and view_model.validate_task_progress(progress['start'], progress['end'], progress['current']) is False:
            response = make_response()
            response.status_code = 403
            response.data = get_string_resource(locale, 'incorrect_value')

            return response
        else:
            if progress['current'] is not None and progress['current'] == progress['end']:
                print(progress['current'])
                is_completed = True
            else:
                is_completed = updates.get('is_completed')
    else:
        is_completed = updates.get('is_completed')

    view_model.update_task(
        user_id,
        list_id,
        task_id,
        task_value,
        progress,
        is_completed
    )

    response = make_response()
    response.status_code = 200
    return response


@task_view.delete('/todo/<int:list_id>/<int:task_id>')
def delete_task(list_id, task_id):
    view_model = get_view_model(flask.current_app)

    token = request.cookies.get('token')

    try:
        token_data = view_model.decode_token(jwt_secret_key, token)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return JWTHelper.create_invalid_jwt_response()

    user_id = token_data['uid']

    view_model.delete_task(user_id, list_id, task_id)

    response = make_response()
    response.status_code = 200

    return response
