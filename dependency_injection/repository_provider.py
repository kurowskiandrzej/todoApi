from domain.repository.to_do_repository import ToDoRepository
from data.repository.to_do_repository_impl import ToDoRepositoryImpl
from data.repository.to_do_repository_fake import ToDoRepositoryFake

repositories = {
    ToDoRepository: ToDoRepositoryImpl(),
    ToDoRepositoryFake: ToDoRepositoryFake()

}
