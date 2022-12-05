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


class PatchedTag(
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
            def type() -> typing.Type['TagTypeEnum']:
                return TagTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "name",
                    }
                    
                    class properties:
                        id = schemas.UUIDSchema
                        
                        
                        class name(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 100
                        
                        
                        class bg_color(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 7
                        
                        
                        class fg_color(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 7
                        
                        
                        class description(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 1024
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'description':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        pinned = schemas.BoolSchema
                        __annotations__ = {
                            "id": id,
                            "name": name,
                            "bg_color": bg_color,
                            "fg_color": fg_color,
                            "description": description,
                            "pinned": pinned,
                        }
                
                name: MetaOapg.properties.name
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bg_color"]) -> MetaOapg.properties.bg_color: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["fg_color"]) -> MetaOapg.properties.fg_color: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pinned"]) -> MetaOapg.properties.pinned: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "bg_color", "fg_color", "description", "pinned", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["bg_color"]) -> typing.Union[MetaOapg.properties.bg_color, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["fg_color"]) -> typing.Union[MetaOapg.properties.fg_color, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pinned"]) -> typing.Union[MetaOapg.properties.pinned, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "bg_color", "fg_color", "description", "pinned", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, ],
                    id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
                    bg_color: typing.Union[MetaOapg.properties.bg_color, str, schemas.Unset] = schemas.unset,
                    fg_color: typing.Union[MetaOapg.properties.fg_color, str, schemas.Unset] = schemas.unset,
                    description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
                    pinned: typing.Union[MetaOapg.properties.pinned, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        name=name,
                        id=id,
                        bg_color=bg_color,
                        fg_color=fg_color,
                        description=description,
                        pinned=pinned,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    type: 'TagTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TagTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TagTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: 'TagTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PatchedTag':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.tag_type_enum import TagTypeEnum
