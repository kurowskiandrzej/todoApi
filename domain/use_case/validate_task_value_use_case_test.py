from domain.use_case.validate_task_value_use_case import ValidateTaskValueUseCase
from common.constants import TASK_VALUE_LENGTH_LIMIT


validate_task_value = ValidateTaskValueUseCase()


def test_returns_true_when_value_is_one_character_long():
    assert validate_task_value("x") is True


def test_returns_true_when_value_length_is_max_of_allowed_length():
    assert validate_task_value("x" * TASK_VALUE_LENGTH_LIMIT) is True


def test_returns_false_when_value_is_empty():
    assert validate_task_value("") is False


def test_returns_false_when_value_is_too_long():
    assert validate_task_value("x" * (TASK_VALUE_LENGTH_LIMIT + 1)) is False
