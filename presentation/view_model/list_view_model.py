from domain.use_case.use_case_wrapper.list_view_model_use_cases import ListViewModelUseCases


class LoginViewModel:
    def __init__(self, use_case: ListViewModelUseCases):
        self.__use_case = use_case
