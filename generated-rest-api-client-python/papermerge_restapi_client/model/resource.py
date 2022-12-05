# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b19
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from papermerge_restapi_client import schemas  # noqa: F401


class Resource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id",
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            attributes = schemas.DictSchema
            relationships = schemas.DictSchema
        
            @staticmethod
            def links() -> typing.Type['Links']:
                return Links
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
                "links": links,
                "meta": meta,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["type"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], typing_extensions.Literal["links"], typing_extensions.Literal["meta"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["type"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], typing_extensions.Literal["links"], typing_extensions.Literal["meta"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        links: typing.Union['Links', schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Resource':
        return super().__new__(
            cls,
            *args,
            id=id,
            type=type,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.links import Links
from papermerge_restapi_client.model.meta import Meta
