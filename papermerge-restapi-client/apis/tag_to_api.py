import typing_extensions

from papermerge-restapi-client.apis.tags import TagValues
from papermerge-restapi-client.apis.tags.auth_api import AuthApi
from papermerge-restapi-client.apis.tags.document_versions_api import DocumentVersionsApi
from papermerge-restapi-client.apis.tags.documents_api import DocumentsApi
from papermerge-restapi-client.apis.tags.folders_api import FoldersApi
from papermerge-restapi-client.apis.tags.groups_api import GroupsApi
from papermerge-restapi-client.apis.tags.nodes_api import NodesApi
from papermerge-restapi-client.apis.tags.ocr_api import OcrApi
from papermerge-restapi-client.apis.tags.pages_api import PagesApi
from papermerge-restapi-client.apis.tags.permissions_api import PermissionsApi
from papermerge-restapi-client.apis.tags.preferences_api import PreferencesApi
from papermerge-restapi-client.apis.tags.schema_api import SchemaApi
from papermerge-restapi-client.apis.tags.search_api import SearchApi
from papermerge-restapi-client.apis.tags.tags_api import TagsApi
from papermerge-restapi-client.apis.tags.tokens_api import TokensApi
from papermerge-restapi-client.apis.tags.users_api import UsersApi
from papermerge-restapi-client.apis.tags.version_api import VersionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH: AuthApi,
        TagValues.DOCUMENTVERSIONS: DocumentVersionsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.NODES: NodesApi,
        TagValues.OCR: OcrApi,
        TagValues.PAGES: PagesApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.SCHEMA: SchemaApi,
        TagValues.SEARCH: SearchApi,
        TagValues.TAGS: TagsApi,
        TagValues.TOKENS: TokensApi,
        TagValues.USERS: UsersApi,
        TagValues.VERSION: VersionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH: AuthApi,
        TagValues.DOCUMENTVERSIONS: DocumentVersionsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.NODES: NodesApi,
        TagValues.OCR: OcrApi,
        TagValues.PAGES: PagesApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PREFERENCES: PreferencesApi,
        TagValues.SCHEMA: SchemaApi,
        TagValues.SEARCH: SearchApi,
        TagValues.TAGS: TagsApi,
        TagValues.TOKENS: TokensApi,
        TagValues.USERS: UsersApi,
        TagValues.VERSION: VersionApi,
    }
)
