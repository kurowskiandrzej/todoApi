from localization.resources.eng import eng
from localization.resources.pl import pl

locales = {
    'eng': eng,
    'pl': pl
}


def get_string_resource(locale: str | None, resource_id: str) -> str:
    """Returns localized message. If provided locale is not supported then
    messages are returned in english.
    """
    if locale not in locales:
        locale = 'eng'

    return locales[locale][resource_id]
