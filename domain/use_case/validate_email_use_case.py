import re
from common.constants import EMAIL_PATTERN
from common.constants import EMAIL_MAXIMUM_LENGTH


def validate_email_use_case(email: str) -> bool:
    if len(email) > EMAIL_MAXIMUM_LENGTH:
        return False

    return bool(re.match(EMAIL_PATTERN, email))
