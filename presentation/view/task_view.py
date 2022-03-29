import os

import flask
from flask import Flask, Blueprint, request, make_response

from dependency_injection.di import resolve
from localization.locales import get_string_resource

task_view = Blueprint('task_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


@task_view.get('/todo/<int:list_id>')
def get_task(list_id):
    return f'you selected {list_id}'


@task_view.post('/todo/<int:list_id>')
def post_task(list_id):
    pass


@task_view.patch('/todo/<int:list_id>')
def update_task(list_id):
    pass


@task_view.delete('/todo/<int:list_id>')
def delete_task(list_id):
    pass





