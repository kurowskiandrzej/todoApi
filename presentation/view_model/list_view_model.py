from domain.use_case.use_case_wrapper.list_view_model_use_cases import ListViewModelUseCases


class ListViewModel:
    def __init__(self, use_case: ListViewModelUseCases):
        self.__use_case = use_case

    def decode_token(self, secret: str, token: str) -> dict:
        return self.__use_case.decode_jwt(secret, token)

    def get_all_lists(self, user_id):
        return self.__use_case.get_all_lists(user_id)
