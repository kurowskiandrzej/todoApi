from domain.use_case.validate_password_use_case import ValidatePasswordUseCase
from common.constants import PASSWORD_MAXIMUM_LENGTH


validate_password = ValidatePasswordUseCase()


def test_returns_true_when_valid_password_is_provided():
    assert validate_password("MyV4L!DPassword") is True


def test_returns_false_when_password_is_too_short():
    assert validate_password("!A1d") is False


def test_returns_false_when_password_is_too_long():
    password = "!A1d" + "x" * PASSWORD_MAXIMUM_LENGTH
    assert validate_password(password) is False


def test_returns_false_when_password_doesnt_contain_small_letters():
    assert validate_password("MYV4!PASSWORD") is False


def test_returns_false_when_password_doesnt_contain_capital_letter():
    assert validate_password("myv4l!password") is False


def test_returns_false_when_password_doesnt_contain_number():
    assert validate_password("MYVl!Password") is False


def test_returns_false_when_password_doesnt_contain_special_character():
    assert validate_password("MYV4lPassword") is False
