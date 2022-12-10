# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b27
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


class DocumentsMerge(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A `Serializer` is a model-less serializer class with additional
support for JSON:API spec features.

As in JSON:API specification a type is always required you need to
make sure that you define `resource_name` in your `Meta` class
when deriving from this class.

Included Mixins:

* A mixin class to enable sparse fieldsets is included
* A mixin class to enable validation of included resources is included
    """


    class MetaOapg:
        required = {
            "dst",
            "src",
        }
        
        class properties:
            src = schemas.UUIDSchema
            dst = schemas.UUIDSchema
            __annotations__ = {
                "src": src,
                "dst": dst,
            }
    
    dst: MetaOapg.properties.dst
    src: MetaOapg.properties.src
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["src"]) -> MetaOapg.properties.src: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dst"]) -> MetaOapg.properties.dst: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["src", "dst", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["src"]) -> MetaOapg.properties.src: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dst"]) -> MetaOapg.properties.dst: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["src", "dst", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dst: typing.Union[MetaOapg.properties.dst, str, uuid.UUID, ],
        src: typing.Union[MetaOapg.properties.src, str, uuid.UUID, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentsMerge':
        return super().__new__(
            cls,
            *args,
            dst=dst,
            src=src,
            _configuration=_configuration,
            **kwargs,
        )
