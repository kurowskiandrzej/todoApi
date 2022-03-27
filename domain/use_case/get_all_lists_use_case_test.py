from get_all_lists_use_case import GetAllListsUseCase
from dependency_injection.di import resolve
from data.repository.to_do_repository_fake import ToDoRepositoryFake


use_case = GetAllListsUseCase(resolve(ToDoRepositoryFake))
lists = use_case(1)


def test_returns_proper_list():
    assert len(lists) > 0


def test_first_element_of_returned_list_has_proper_id():
    assert lists[0]['id'] == 1


def test_first_element_of_returned_list_has_proper_name():
    assert lists[0]['name'] == 'first'
