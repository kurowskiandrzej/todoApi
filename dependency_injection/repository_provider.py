from data.repository.to_do_repository_fake import ToDoRepositoryFake
from data.repository.to_do_repository_impl import ToDoRepositoryImpl
from domain.repository.to_do_repository import ToDoRepository

repositories = {
    ToDoRepository: ToDoRepositoryImpl(),
    ToDoRepositoryFake: ToDoRepositoryFake()

}
