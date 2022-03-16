from flask import Flask

from presentation.view.login_view import login_view


app = Flask(__name__)
app.register_blueprint(login_view)


def test_login_route_get_method_returns_status_code_405():
    client = app.test_client()
    url = '/api/login'
    response = client.get(url)

    assert response.status_code == 405


def test_login_route_post_method_returns_status_code_200():
    client = app.test_client()
    url = '/api/login'
    response = client.post(url)

    assert response.status_code == 200
