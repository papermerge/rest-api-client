from papermerge-restapi-client.paths.api_tags_id_.get import ApiForget
from papermerge-restapi-client.paths.api_tags_id_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_tags_id_.patch import ApiForpatch


class ApiTagsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
