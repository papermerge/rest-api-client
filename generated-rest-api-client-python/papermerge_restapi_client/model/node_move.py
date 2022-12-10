# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b31
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


class NodeMove(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "nodes",
            "target_parent",
        }
        
        class properties:
        
            @staticmethod
            def target_parent() -> typing.Type['NodeID']:
                return NodeID
            
            
            class nodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NodeID']:
                        return NodeID
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NodeID'], typing.List['NodeID']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nodes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NodeID':
                    return super().__getitem__(i)
            __annotations__ = {
                "target_parent": target_parent,
                "nodes": nodes,
            }
    
    nodes: MetaOapg.properties.nodes
    target_parent: 'NodeID'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_parent"]) -> 'NodeID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["target_parent", "nodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_parent"]) -> 'NodeID': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["target_parent", "nodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nodes: typing.Union[MetaOapg.properties.nodes, list, tuple, ],
        target_parent: 'NodeID',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeMove':
        return super().__new__(
            cls,
            *args,
            nodes=nodes,
            target_parent=target_parent,
            _configuration=_configuration,
            **kwargs,
        )

from papermerge_restapi_client.model.node_id import NodeID
