from domain.use_case.login_user_use_case import LoginUserUseCase
from data.repository.to_do_repository_fake import ToDoRepositoryFake
from dependency_injection.di import resolve

login_user = LoginUserUseCase(resolve(ToDoRepositoryFake))


def test_returns_user_id_when_login_with_valid_credentials():
    response = login_user("user@mail.com", "MyV4L!DPassword")

    assert response == {
        'user_id': 1
    }


def test_returns_401_error_when_login_with_proper_email_and_incorrect_password():
    response = login_user("user@mail.com", "MyNotS0V4L!DPassword")

    assert response == {
        'status_code': 401,
        'string_resource_id': 'incorrect_password'
    }


def test_returns_401_error_when_login_with_invalid_email():
    response = login_user("userMailCom", "MyV4L!DPassword")

    assert response == {
        'status_code': 401,
        'string_resource_id': 'no_such_user'
    }


def test_throws_401_error_when_login_with_not_existing_email():
    response = login_user("fake@mail.com", "MyV4L!DPassword")

    assert response == {
        'status_code': 401,
        'string_resource_id': 'no_such_user'
    }
