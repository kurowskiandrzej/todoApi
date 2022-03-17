from domain.repository.ToDoRepository import ToDoRepository


class LoginViewModelUseCases:
    def __init__(self, repository: ToDoRepository):
        self.repository = repository

