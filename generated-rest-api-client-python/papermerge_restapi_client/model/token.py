# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b14
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


class Token(
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
            def type() -> typing.Type['TokenTypeEnum']:
                return TokenTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "digest",
                    }
                    
                    class properties:
                        
                        
                        class token(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 256
                        
                        
                        class digest(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 128
                        created = schemas.DateTimeSchema
                        
                        
                        class expiry(
                            schemas.DateTimeBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'date-time'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, datetime, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'expiry':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "token": token,
                            "digest": digest,
                            "created": created,
                            "expiry": expiry,
                        }
                
                digest: MetaOapg.properties.digest
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["digest"]) -> MetaOapg.properties.digest: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["expiry"]) -> MetaOapg.properties.expiry: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["token", "digest", "created", "expiry", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["digest"]) -> MetaOapg.properties.digest: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["expiry"]) -> typing.Union[MetaOapg.properties.expiry, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token", "digest", "created", "expiry", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    digest: typing.Union[MetaOapg.properties.digest, str, ],
                    token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
                    created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
                    expiry: typing.Union[MetaOapg.properties.expiry, None, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        digest=digest,
                        token=token,
                        created=created,
                        expiry=expiry,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    type: 'TokenTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TokenTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TokenTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: 'TokenTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Token':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.token_type_enum import TokenTypeEnum
