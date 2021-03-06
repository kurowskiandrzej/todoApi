from flask import Flask

from presentation.view.login_view import login_view


def get_app():
    app = Flask(__name__)
    app.register_blueprint(login_view)
    app.config['TESTING'] = True
    return app


def test_login_route_get_method_returns_status_code_405():
    app = get_app()
    client = app.test_client()
    response = client.get('/api/login')

    assert response.status_code == 405


def test_login_route_delete_method_returns_status_code_405():
    app = get_app()
    client = app.test_client()
    response = client.delete('/api/login')

    assert response.status_code == 405


def test_login_route_put_method_returns_status_code_405():
    app = get_app()
    client = app.test_client()
    response = client.put('/api/login')

    assert response.status_code == 405


def test_login_route_patch_method_returns_status_code_405():
    app = get_app()
    client = app.test_client()
    response = client.patch('/api/login')

    assert response.status_code == 405


def test_login_route_post_method_with_correct_password_returns_status_code_200():
    app = get_app()
    client = app.test_client()
    response = client.post(
        '/api/login',
        content_type='multipart/form-data',
        data={
            'email': 'user@mail.com',
            'password': 'MyV4L!DPassword'
        },
        headers={
            'Accept-Language': 'pl'
        }
    )

    assert response.status_code == 200


def test_login_route_post_method_with_invalid_password_returns_status_code_401():
    app = get_app()
    client = app.test_client()
    response = client.post(
        '/api/login',
        content_type='multipart/form-data',
        data={
            'email': 'user@mail.com',
            'password': 'xxxx'
        },
        headers={
            'Accept-Language': 'eng'
        }
    )

    assert response.status_code == 401


def test_login_route_post_method_with_invalid_email_returns_status_code_401():
    app = get_app()
    client = app.test_client()
    response = client.post(
        '/api/login',
        content_type='multipart/form-data',
        data={
            'email': 'userMail.com',
            'password': 'MyV4L!DPassword'
        },
        headers={
            'Accept-Language': 'pl'
        }
    )

    assert response.status_code == 401
