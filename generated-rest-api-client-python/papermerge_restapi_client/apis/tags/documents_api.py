# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b29
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_documents_id_ocr_text.get import DocumentOcrText
from papermerge_restapi_client.paths.api_documents_id_.delete import DocumentsDestroy
from papermerge_restapi_client.paths.api_documents_.get import DocumentsList
from papermerge_restapi_client.paths.api_documents_merge_.post import DocumentsMerge
from papermerge_restapi_client.paths.api_documents_id_.patch import DocumentsPartialUpdate
from papermerge_restapi_client.paths.api_documents_id_.get import DocumentsRetrieve
from papermerge_restapi_client.paths.api_documents_document_id_upload_file_name.put import UploadFile


class DocumentsApi(
    DocumentOcrText,
    DocumentsDestroy,
    DocumentsList,
    DocumentsMerge,
    DocumentsPartialUpdate,
    DocumentsRetrieve,
    UploadFile,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
