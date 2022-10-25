from papermerge-restapi-client.paths.api_folders_id_.get import ApiForget
from papermerge-restapi-client.paths.api_folders_id_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_folders_id_.patch import ApiForpatch


class ApiFoldersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
