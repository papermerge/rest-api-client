# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b27
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_tokens_.post import TokensCreate
from papermerge_restapi_client.paths.api_tokens_digest_.delete import TokensDestroy
from papermerge_restapi_client.paths.api_tokens_.get import TokensList
from papermerge_restapi_client.paths.api_tokens_digest_.get import TokensRetrieve


class TokensApi(
    TokensCreate,
    TokensDestroy,
    TokensList,
    TokensRetrieve,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
