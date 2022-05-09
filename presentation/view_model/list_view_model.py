from domain.use_case.use_case_wrapper.list_view_model_use_cases import ListViewModelUseCases


class ListViewModel:
    def __init__(self, use_case: ListViewModelUseCases):
        self.__use_case = use_case

    def decode_token(self, secret: str, token: str) -> dict:
        return self.__use_case.decode_jwt(secret, token)

    def post_list(self, user_id: int, list_name: str) -> (int, str):
        return self.__use_case.post_list(user_id, list_name)

    def update_list(self, user_id: int, list_id: int, updated_name: str):
        self.__use_case.update_list_name(user_id, list_id, updated_name)

    def delete_list(self, user_id: int, list_id: int):
        self.__use_case.delete_list(user_id, list_id)

    def validate_list_name(self, list_name: str):
        return self.__use_case.validate_list_name(list_name)

    def get_all_lists(self, user_id):
        return self.__use_case.get_all_lists(user_id)
