from domain.repository.to_do_repository import ToDoRepository


class RegisterViewModelUseCases:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository
