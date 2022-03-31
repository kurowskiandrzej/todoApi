from common.constants import TASK_VALUE_LENGTH_LIMIT


class ValidateTaskValueUseCase:
    def __call__(self, value: str) -> bool:
        return 1 <= len(value) <= TASK_VALUE_LENGTH_LIMIT
