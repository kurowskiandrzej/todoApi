import re

from common.constants import PASSWORD_MAXIMUM_LENGTH
from common.constants import PASSWORD_MINIMUM_LENGTH
from common.constants import PASSWORD_PATTERN


class ValidatePasswordUseCase:
    def __call__(self, password: str) -> bool:
        if PASSWORD_MINIMUM_LENGTH <= len(password) <= PASSWORD_MAXIMUM_LENGTH:
            return bool(re.match(PASSWORD_PATTERN, password))
        else:
            return False
