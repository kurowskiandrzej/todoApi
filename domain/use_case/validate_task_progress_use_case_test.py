from domain.use_case.validate_task_progress_use_case import ValidateTaskProgressUseCase


validate_task_progress = ValidateTaskProgressUseCase()


def test_returns_false_when_start_value_is_the_same_as_end_value():
    assert validate_task_progress(10, 10, 10) is False


def test_returns_false_when_progress_is_smaller_than_start_and_end_values():
    assert validate_task_progress(10, 20, 1) is False


def test_returns_false_when_progress_is_bigger_than_start_and_end_values():
    assert validate_task_progress(10, 20, 30) is False


def test_returns_true_when_progress_is_bigger_than_start_value_and_smaller_than_end_value():
    assert validate_task_progress(10, 20, 15) is True


def test_returns_true_when_progress_is_smaller_than_start_value_and_bigger_than_end_value():
    assert validate_task_progress(20, 10, 15) is True


def test_returns_true_when_progress_is_equal_to_start_value():
    assert validate_task_progress(10, 20, 10) is True


def test_returns_true_when_progress_is_equal_to_end_value():
    assert validate_task_progress(10, 20, 20) is True
