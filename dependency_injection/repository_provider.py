from domain.repository.to_do_repository import ToDoRepository
from data.repository.to_do_repository_impl import ToDoRepositoryImpl

repositories = {
    ToDoRepository: ToDoRepositoryImpl()
}
