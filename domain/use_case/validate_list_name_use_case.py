from common.constants import LIST_NAME_LENGTH_LIMIT


class ValidateListNameUseCase:
    def __call__(self, list_name: str) -> bool:
        if 1 <= len(list_name) <= LIST_NAME_LENGTH_LIMIT:
            return True
        else:
            return False
