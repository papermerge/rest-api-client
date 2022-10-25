from papermerge-restapi-client.paths.api_documents_id_.get import ApiForget
from papermerge-restapi-client.paths.api_documents_id_.delete import ApiFordelete
from papermerge-restapi-client.paths.api_documents_id_.patch import ApiForpatch


class ApiDocumentsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
