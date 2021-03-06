from domain.use_case.decode_jwt_use_case import DecodeJwtUseCase
from domain.use_case.get_all_lists_use_case import GetAllListsUseCase
from domain.use_case.insert_list_use_case import InsertListUseCase
from domain.use_case.validate_list_name_use_case import ValidateListNameUseCase
from domain.use_case.update_list_name_use_case import UpdateListNameUseCase
from domain.use_case.delete_list_use_case import DeleteListUseCase


class ListViewModelUseCases:
    def __init__(
            self,
            decode_jwt: DecodeJwtUseCase,
            get_all_lists: GetAllListsUseCase,
            post_list: InsertListUseCase,
            delete_list: DeleteListUseCase,
            update_list_name: UpdateListNameUseCase,
            validate_list_name: ValidateListNameUseCase
    ):
        self.get_all_lists = get_all_lists
        self.decode_jwt = decode_jwt
        self.post_list = post_list
        self.delete_list = delete_list
        self.update_list_name = update_list_name
        self.validate_list_name = validate_list_name
