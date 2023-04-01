# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.9
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_tags_.post import TagsCreate
from papermerge_restapi_client.paths.api_tags_id_.delete import TagsDestroy
from papermerge_restapi_client.paths.api_tags_.get import TagsList
from papermerge_restapi_client.paths.api_tags_id_.patch import TagsPartialUpdate
from papermerge_restapi_client.paths.api_tags_id_.get import TagsRetrieve


class TagsApi(
    TagsCreate,
    TagsDestroy,
    TagsList,
    TagsPartialUpdate,
    TagsRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
