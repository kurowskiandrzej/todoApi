from domain.repository.ToDoRepository import ToDoRepository
from data.repository.ToDoRepositoryImpl import ToDoRepositoryImpl

repositories = {
    ToDoRepository: ToDoRepositoryImpl()
}
