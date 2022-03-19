import re
from common.constants import EMAIL_PATTERN
from common.constants import EMAIL_MAXIMUM_LENGTH


class ValidateEmailUseCase:
    def __call__(self, email: str) -> bool:
        if len(email) > EMAIL_MAXIMUM_LENGTH:
            return False

        return bool(re.match(EMAIL_PATTERN, email))
