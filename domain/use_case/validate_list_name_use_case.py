from common.constants import LIST_NAME_LENGTH_LIMIT


class ValidateListNameUseCase:
    def __call__(self, list_name: str) -> bool:
        if len(list_name) < 1 or len(list_name) > LIST_NAME_LENGTH_LIMIT:
            return False
        else:
            return True
