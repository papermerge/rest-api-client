from papermerge-restapi-client.paths.api_groups_id_.get import ApiForget
from papermerge-restapi-client.paths.api_groups_id_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_groups_id_.patch import ApiForpatch


class ApiGroupsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
