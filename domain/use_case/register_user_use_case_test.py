import pytest
from sqlalchemy import exc

from data.repository.to_do_repository_fake import ToDoRepositoryFake
from dependency_injection.di import resolve
from domain.use_case.register_user_use_case import RegisterUserUseCase

register_user = RegisterUserUseCase(resolve(ToDoRepositoryFake))


def test_registering_user_returns_user_id():
    user_id = register_user("newUser@mail.com", "MyS3C0N!#sPass")

    assert type(user_id) is int


def test_registering_with_existing_email_throws_error():
    with pytest.raises(exc.IntegrityError):
        register_user("user@mail.com", "MyV4L!DPassword")
