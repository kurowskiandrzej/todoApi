import os

import flask
from flask import Flask, Blueprint, request, make_response, jsonify

from dependency_injection.di import resolve
from localization.locales import get_string_resource
from presentation.view_model.task_view_model import TaskViewModel

task_view = Blueprint('task_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


def get_view_model(app: Flask) -> TaskViewModel:
    if app.config['TESTING']:
        return resolve('TaskViewModelFake')
    else:
        return resolve(TaskViewModel)


@task_view.get('/todo/<int:list_id>')
def get_task(list_id):
    return f'you selected {list_id}'


@task_view.post('/todo/<int:list_id>')
def post_task(list_id):
    view_model = get_view_model(flask.current_app)

    task_id = view_model.insert_task(1, list_id, {
        'value': 'test task',
        'start': 5,
        'end': 100,
        'current': 10
    })

    return jsonify({'task_id': task_id}), 200


@task_view.patch('/todo/<int:list_id>/<int:task_id>')
def update_task(list_id, task_id):
    pass


@task_view.delete('/todo/<int:list_id>/<int:task_id>')
def delete_task(list_id, task_id):
    view_model = get_view_model(flask.current_app)

    view_model.delete_task(1, task_id)

    response = make_response()
    response.status_code = 200

    return response





