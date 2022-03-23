from presentation.view_model.login_view_model import LoginViewModel
from dependency_injection.di import resolve


def get_fake_view_model() -> LoginViewModel:
    return resolve('LoginViewModelFake')


def test_login_with_valid_credentials_returns_status_code_200_and_no_string_resource_id():
    view_model: LoginViewModel = get_fake_view_model()

    result = view_model.login("user@mail.com", "MyV4L!DPassword")

    assert result == {
        'status_code': 200,
        'user_id': 1
    }


def test_login_with_invalid_email_returns_status_code_401_and_proper_string_resource_id():
    view_model: LoginViewModel = get_fake_view_model()

    result = view_model.login("fakeMail.com", "fakePassword")

    assert result == {
        'status_code': 401,
        'string_resource_id': 'incorrect_email_format'
    }


def test_login_with_invalid_password_returns_status_code_401_and_proper_string_resource_id():
    view_model: LoginViewModel = get_fake_view_model()

    result = view_model.login("fake@mail.com", "fakePassword")

    assert result == {
        'status_code': 401,
        'string_resource_id': 'incorrect_password'
    }


def test_login_with_incorrect_password_returns_status_code_401_and_proper_string_resource_id():
    view_model: LoginViewModel = get_fake_view_model()

    result = view_model.login("user@mail.com", "!1fakePassword")

    assert result == {
        'status_code': 401,
        'string_resource_id': 'incorrect_password'
    }


def test_login_with_not_existing_email_returns_status_code_401_and_proper_string_resource_id():
    view_model: LoginViewModel = get_fake_view_model()

    result = view_model.login("fake@mail.com", "!1fakePassword")

    assert result == {
        'status_code': 401,
        'string_resource_id': 'no_such_user'
    }
