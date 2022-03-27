import os

import flask
from flask import Flask, Blueprint, request, make_response

from dependency_injection.di import resolve
from localization.locales import get_string_resource

to_do_task_view = Blueprint('to_do_task_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


@to_do_task_view.route('/todo/task', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def to_do_task():
    pass
