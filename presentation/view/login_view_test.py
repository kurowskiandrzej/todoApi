from flask import Flask

from presentation.view.login_view import login_view


def get_app():
    app = Flask(__name__)
    app.register_blueprint(login_view)
    return app


def test_login_route_get_method_returns_status_code_405():
    app = get_app()
    client = app.test_client()
    response = client.get('/api/login')

    assert response.status_code == 405


def test_login_route_post_method_with_correct_password_returns_status_code_200():
    app = get_app()
    client = app.test_client()
    response = client.post(
        '/api/login',
        content_type='multipart/form-data',
        data={
            'email': 'test@mail.com',
            'password': 'MYV4L!DPassword'
        },
        headers={
            'Accept-Language': 'pl'
        }
    )

    assert response.status_code == 200


def test_login_route_post_method_with_incorrect_password_returns_status_code_401():
    app = get_app()
    client = app.test_client()
    response = client.post(
        '/api/login',
        content_type='multipart/form-data',
        data={
            'email': 'test@mail.com',
            'password': 'xxxx'
        },
        headers={
            'Accept-Language': 'pl'
        }
    )

    assert response.status_code == 401
