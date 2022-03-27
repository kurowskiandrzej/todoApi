from domain.use_case.decode_jwt_use_case import DecodeJwtUseCase
from domain.use_case.get_all_lists_use_case import GetAllListsUseCase
from domain.use_case.post_list_use_case import PostListUseCase


class ListViewModelUseCases:
    def __init__(
            self,
            decode_jwt: DecodeJwtUseCase,
            get_all_lists: GetAllListsUseCase,
            post_list: PostListUseCase
    ):
        self.get_all_lists = get_all_lists
        self.decode_jwt = decode_jwt
        self.post_list = post_list
