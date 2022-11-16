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


class DocumentVersion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A `ModelSerializer` is just a regular `Serializer`, except that:

* A set of default fields are automatically populated.
* A set of default validators are automatically populated.
* Default `.create()` and `.update()` implementations are provided.

The process of automatically determining a set of serializer fields
based on the model fields is reasonably complex, but you almost certainly
don't need to dig into the implementation.

If the `ModelSerializer` class *doesn't* generate the set of fields that
you need you should either declare the extra/differing fields explicitly on
the serializer class, or simply use a `Serializer` class.


Included Mixins:

* A mixin class to enable sparse fieldsets is included
* A mixin class to enable validation of included resources is included
    """


    class MetaOapg:
        required = {
            "pages",
            "document",
            "download_url",
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
            document = schemas.UUIDSchema
            download_url = schemas.StrSchema
            id = schemas.UUIDSchema
            number = schemas.IntSchema
            
            
            class lang(
                schemas.StrSchema
            ):
                pass
            
            
            class file_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'file_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            size = schemas.IntSchema
            page_count = schemas.IntSchema
            
            
            class short_description(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "pages": pages,
                "document": document,
                "download_url": download_url,
                "id": id,
                "number": number,
                "lang": lang,
                "file_name": file_name,
                "size": size,
                "page_count": page_count,
                "short_description": short_description,
            }
    
    pages: MetaOapg.properties.pages
    document: MetaOapg.properties.document
    download_url: MetaOapg.properties.download_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document"]) -> MetaOapg.properties.document: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download_url"]) -> MetaOapg.properties.download_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lang"]) -> MetaOapg.properties.lang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_count"]) -> MetaOapg.properties.page_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short_description"]) -> MetaOapg.properties.short_description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pages", "document", "download_url", "id", "number", "lang", "file_name", "size", "page_count", "short_description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document"]) -> MetaOapg.properties.document: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download_url"]) -> MetaOapg.properties.download_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lang"]) -> typing.Union[MetaOapg.properties.lang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> typing.Union[MetaOapg.properties.file_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_count"]) -> typing.Union[MetaOapg.properties.page_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short_description"]) -> typing.Union[MetaOapg.properties.short_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pages", "document", "download_url", "id", "number", "lang", "file_name", "size", "page_count", "short_description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pages: typing.Union[MetaOapg.properties.pages, list, tuple, ],
        document: typing.Union[MetaOapg.properties.document, str, uuid.UUID, ],
        download_url: typing.Union[MetaOapg.properties.download_url, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lang: typing.Union[MetaOapg.properties.lang, str, schemas.Unset] = schemas.unset,
        file_name: typing.Union[MetaOapg.properties.file_name, None, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page_count: typing.Union[MetaOapg.properties.page_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        short_description: typing.Union[MetaOapg.properties.short_description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentVersion':
        return super().__new__(
            cls,
            *args,
            pages=pages,
            document=document,
            download_url=download_url,
            id=id,
            number=number,
            lang=lang,
            file_name=file_name,
            size=size,
            page_count=page_count,
            short_description=short_description,
            _configuration=_configuration,
            **kwargs,
        )
