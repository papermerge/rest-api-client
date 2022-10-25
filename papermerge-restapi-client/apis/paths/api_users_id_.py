from papermerge-restapi-client.paths.api_users_id_.get import ApiForget
from papermerge-restapi-client.paths.api_users_id_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_users_id_.patch import ApiForpatch


class ApiUsersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
