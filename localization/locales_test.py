from localization.resources.eng import eng
from localization.resources.pl import pl
from localization.locales import get_string_resource


def test_if_resources_match_through_all_languages():
    assert eng.keys() == pl.keys()


def test_get_valid_pl_string_resource():
    assert get_string_resource('pl', 'no_such_user') == pl['no_such_user']


def test_get_valid_eng_string_resource():
    assert get_string_resource('eng', 'no_such_user') == eng['no_such_user']


def test_get_valid_eng_string_resource_when_there_is_no_locale_provided():
    assert get_string_resource(None, 'no_such_user') == eng['no_such_user']


def test_get_valid_eng_string_resource_when_locale_doesnt_exists():
    assert get_string_resource('fake_locale', 'no_such_user') == eng['no_such_user']
