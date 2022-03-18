from domain.repository.to_do_repository import ToDoRepository


class LoginViewModelUseCases:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

