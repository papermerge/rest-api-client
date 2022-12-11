# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b33
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


class Pagination(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def first() -> typing.Type['Pageref']:
                return Pageref
        
            @staticmethod
            def last() -> typing.Type['Pageref']:
                return Pageref
        
            @staticmethod
            def prev() -> typing.Type['Pageref']:
                return Pageref
        
            @staticmethod
            def next() -> typing.Type['Pageref']:
                return Pageref
            __annotations__ = {
                "first": first,
                "last": last,
                "prev": prev,
                "next": next,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> 'Pageref': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> 'Pageref': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prev"]) -> 'Pageref': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next"]) -> 'Pageref': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first", "last", "prev", "next", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union['Pageref', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union['Pageref', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prev"]) -> typing.Union['Pageref', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union['Pageref', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first", "last", "prev", "next", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        first: typing.Union['Pageref', schemas.Unset] = schemas.unset,
        last: typing.Union['Pageref', schemas.Unset] = schemas.unset,
        prev: typing.Union['Pageref', schemas.Unset] = schemas.unset,
        next: typing.Union['Pageref', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Pagination':
        return super().__new__(
            cls,
            *args,
            first=first,
            last=last,
            prev=prev,
            next=next,
            _configuration=_configuration,
            **kwargs,
        )

from papermerge_restapi_client.model.pageref import Pageref
