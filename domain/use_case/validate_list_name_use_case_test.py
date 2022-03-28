from domain.use_case.validate_list_name_use_case import ValidateListNameUseCase
from common.constants import LIST_NAME_LENGTH_LIMIT


validate_list_name = ValidateListNameUseCase()


def test_returns_true_when_provided_with_correct_list_name():
    assert validate_list_name("Proper list name") is True


def test_returns_false_when_name_is_empty():
    assert validate_list_name("") is False


def test_returns_false_when_list_name_is_too_long():
    list_name = "x" * (LIST_NAME_LENGTH_LIMIT + 1)
    assert validate_list_name(list_name) is False
