from domain.use_case.validate_password_use_case import validate_password_use_case
from common.constants import PASSWORD_MAXIMUM_LENGTH


def test_returns_true_when_valid_password_is_provided():
    assert validate_password_use_case("MyV4L!DPassword") is True


def test_returns_false_when_password_is_too_short():
    assert validate_password_use_case("!A1d") is False


def test_returns_false_when_password_is_too_long():
    password = "!A1d" + "x" * (PASSWORD_MAXIMUM_LENGTH)
    assert validate_password_use_case(password) is False


def test_returns_false_when_password_doesnt_contain_small_letters():
    assert validate_password_use_case("MYV4!PASSWORD") is False


def test_returns_false_when_password_doesnt_contain_capital_character():
    assert validate_password_use_case("myv4l!password") is False


def test_returns_false_when_password_doesnt_contain_number():
    assert validate_password_use_case("MYVl!Password") is False


def test_returns_false_when_password_doesnt_contain_special_character():
    assert validate_password_use_case("MYV4lPassword") is False
