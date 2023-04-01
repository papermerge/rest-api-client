# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.9
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


class PatchedFolder(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['FolderTypeEnum']:
                return FolderTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "title",
                    }
                    
                    class properties:
                        id = schemas.UUIDSchema
                        
                        
                        class title(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 200
                        breadcrumb = schemas.StrSchema
                        
                        
                        class tags(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['Tag']:
                                    return Tag
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple['Tag'], typing.List['Tag']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'tags':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'Tag':
                                return super().__getitem__(i)
                        created_at = schemas.DateTimeSchema
                        updated_at = schemas.DateTimeSchema
                        __annotations__ = {
                            "id": id,
                            "title": title,
                            "breadcrumb": breadcrumb,
                            "tags": tags,
                            "created_at": created_at,
                            "updated_at": updated_at,
                        }
                
                title: MetaOapg.properties.title
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["breadcrumb"]) -> MetaOapg.properties.breadcrumb: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "title", "breadcrumb", "tags", "created_at", "updated_at", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["breadcrumb"]) -> typing.Union[MetaOapg.properties.breadcrumb, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "title", "breadcrumb", "tags", "created_at", "updated_at", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    title: typing.Union[MetaOapg.properties.title, str, ],
                    id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
                    breadcrumb: typing.Union[MetaOapg.properties.breadcrumb, str, schemas.Unset] = schemas.unset,
                    tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
                    created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                    updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        title=title,
                        id=id,
                        breadcrumb=breadcrumb,
                        tags=tags,
                        created_at=created_at,
                        updated_at=updated_at,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def parent() -> typing.Type['Reltoone']:
                            return Reltoone
                        __annotations__ = {
                            "parent": parent,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'Reltoone': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['Reltoone', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parent", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    parent: typing.Union['Reltoone', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *args,
                        parent=parent,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    type: 'FolderTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'FolderTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'FolderTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: 'FolderTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PatchedFolder':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.folder_type_enum import FolderTypeEnum
from papermerge_restapi_client.model.reltoone import Reltoone
from papermerge_restapi_client.model.tag import Tag
