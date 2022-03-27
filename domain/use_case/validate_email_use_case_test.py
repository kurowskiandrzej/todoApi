from domain.use_case.validate_email_use_case import ValidateEmailUseCase
from common.constants import EMAIL_MAXIMUM_LENGTH


validate_email = ValidateEmailUseCase()


def test_returns_true_when_provided_with_valid_email():
    assert validate_email('myemail@mail.com') is True


def test_returns_false_when_provided_with_email_without_at_sign():
    assert validate_email('email.com') is False


def test_returns_false_when_provided_with_email_without_dot():
    assert validate_email('email@mailcom') is False


def test_returns_false_when_provided_email_contains_white_spaces_at_the_start():
    assert validate_email(' email@mail.com') is False


def test_returns_false_when_provided_email_contains_white_spaces_at_the_end():
    assert validate_email('email@mailcom ') is False


def test_returns_false_when_provided_email_length_is_too_big():
    fake_email = "x" * (EMAIL_MAXIMUM_LENGTH + 1)
    assert validate_email(fake_email) is False
