# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from papermerge-restapi-client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from papermerge-restapi-client.model.archive_type_enum import ArchiveTypeEnum
from papermerge-restapi-client.model.auth_token import AuthToken
from papermerge-restapi-client.model.custom_user_preference import CustomUserPreference
from papermerge-restapi-client.model.datum import Datum
from papermerge-restapi-client.model.document_details import DocumentDetails
from papermerge-restapi-client.model.document_version import DocumentVersion
from papermerge-restapi-client.model.document_version_ocr_text import DocumentVersionOcrText
from papermerge-restapi-client.model.documents_merge import DocumentsMerge
from papermerge-restapi-client.model.error import Error
from papermerge-restapi-client.model.errors import Errors
from papermerge-restapi-client.model.failure import Failure
from papermerge-restapi-client.model.folder import Folder
from papermerge-restapi-client.model.group import Group
from papermerge-restapi-client.model.id import Id
from papermerge-restapi-client.model.inbox_count import InboxCount
from papermerge-restapi-client.model.include_version_enum import IncludeVersionEnum
from papermerge-restapi-client.model.jsonapi import Jsonapi
from papermerge-restapi-client.model.link import Link
from papermerge-restapi-client.model.linkage import Linkage
from papermerge-restapi-client.model.links import Links
from papermerge-restapi-client.model.meta import Meta
from papermerge-restapi-client.model.node import Node
from papermerge-restapi-client.model.node_id import NodeID
from papermerge-restapi-client.model.node_move import NodeMove
from papermerge-restapi-client.model.node_tags import NodeTags
from papermerge-restapi-client.model.node_type_enum import NodeTypeEnum
from papermerge-restapi-client.model.nodes_download import NodesDownload
from papermerge-restapi-client.model.ocr import Ocr
from papermerge-restapi-client.model.onlymeta import Onlymeta
from papermerge-restapi-client.model.page import Page
from papermerge-restapi-client.model.page_reorder import PageReorder
from papermerge-restapi-client.model.page_rotate import PageRotate
from papermerge-restapi-client.model.pageref import Pageref
from papermerge-restapi-client.model.pages_move_to_document import PagesMoveToDocument
from papermerge-restapi-client.model.pages_move_to_folder import PagesMoveToFolder
from papermerge-restapi-client.model.pages_reorder import PagesReorder
from papermerge-restapi-client.model.pages_rotate import PagesRotate
from papermerge-restapi-client.model.paginated_custom_user_preference_list import PaginatedCustomUserPreferenceList
from papermerge-restapi-client.model.paginated_document_details_list import PaginatedDocumentDetailsList
from papermerge-restapi-client.model.paginated_folder_list import PaginatedFolderList
from papermerge-restapi-client.model.paginated_group_list import PaginatedGroupList
from papermerge-restapi-client.model.paginated_node_list import PaginatedNodeList
from papermerge-restapi-client.model.paginated_tag_list import PaginatedTagList
from papermerge-restapi-client.model.paginated_token_list import PaginatedTokenList
from papermerge-restapi-client.model.paginated_user_list import PaginatedUserList
from papermerge-restapi-client.model.pagination import Pagination
from papermerge-restapi-client.model.password import Password
from papermerge-restapi-client.model.patched_custom_user_preference import PatchedCustomUserPreference
from papermerge-restapi-client.model.patched_document_details import PatchedDocumentDetails
from papermerge-restapi-client.model.patched_folder import PatchedFolder
from papermerge-restapi-client.model.patched_group import PatchedGroup
from papermerge-restapi-client.model.patched_node import PatchedNode
from papermerge-restapi-client.model.patched_node_tags import PatchedNodeTags
from papermerge-restapi-client.model.patched_tag import PatchedTag
from papermerge-restapi-client.model.patched_user import PatchedUser
from papermerge-restapi-client.model.permission import Permission
from papermerge-restapi-client.model.relationship_links import RelationshipLinks
from papermerge-restapi-client.model.relationship_to_many import RelationshipToMany
from papermerge-restapi-client.model.relationship_to_one import RelationshipToOne
from papermerge-restapi-client.model.reltomany import Reltomany
from papermerge-restapi-client.model.reltoone import Reltoone
from papermerge-restapi-client.model.resource import Resource
from papermerge-restapi-client.model.resource_identifier_object import ResourceIdentifierObject
from papermerge-restapi-client.model.search_result import SearchResult
from papermerge-restapi-client.model.tag import Tag
from papermerge-restapi-client.model.token import Token
from papermerge-restapi-client.model.type import Type
from papermerge-restapi-client.model.user import User
from papermerge-restapi-client.model.version import Version
