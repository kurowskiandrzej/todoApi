import os

import flask
from flask import Flask, Blueprint, request, make_response

from dependency_injection.di import resolve
from localization.locales import get_string_resource

list_view = Blueprint('list_view', __name__, url_prefix='/api')

jwt_secret_key = os.environ.get("JWT_SECRET_KEY", "fakeSecret")


@list_view.post('/todo')
def post_list():
    pass


@list_view.get('/todo')
def get_list():
    return make_response(
        {'status': 'success'}
    )


@list_view.patch('/todo')
def patch_list():
    pass


@list_view.delete('/todo')
def delete_list():
    pass
