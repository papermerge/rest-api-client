# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b29
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


class PagesMoveToFolder(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "pages",
            "dst",
        }
        
        class properties:
            
            
            class pages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.UUIDSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, uuid.UUID, ]], typing.List[typing.Union[MetaOapg.items, str, uuid.UUID, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            dst = schemas.UUIDSchema
            single_page = schemas.BoolSchema
            
            
            class title_format(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "pages": pages,
                "dst": dst,
                "single_page": single_page,
                "title_format": title_format,
            }
    
    pages: MetaOapg.properties.pages
    dst: MetaOapg.properties.dst
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dst"]) -> MetaOapg.properties.dst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["single_page"]) -> MetaOapg.properties.single_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title_format"]) -> MetaOapg.properties.title_format: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pages", "dst", "single_page", "title_format", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dst"]) -> MetaOapg.properties.dst: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["single_page"]) -> typing.Union[MetaOapg.properties.single_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title_format"]) -> typing.Union[MetaOapg.properties.title_format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pages", "dst", "single_page", "title_format", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pages: typing.Union[MetaOapg.properties.pages, list, tuple, ],
        dst: typing.Union[MetaOapg.properties.dst, str, uuid.UUID, ],
        single_page: typing.Union[MetaOapg.properties.single_page, bool, schemas.Unset] = schemas.unset,
        title_format: typing.Union[MetaOapg.properties.title_format, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PagesMoveToFolder':
        return super().__new__(
            cls,
            *args,
            pages=pages,
            dst=dst,
            single_page=single_page,
            title_format=title_format,
            _configuration=_configuration,
            **kwargs,
        )
