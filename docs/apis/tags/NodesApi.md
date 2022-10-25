<a name="__pageTop"></a>
# papermerge-restapi-client.apis.tags.nodes_api.NodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_append_tags**](#node_append_tags) | **patch** /api/nodes/{id}/tags/ | 
[**node_assign_tags**](#node_assign_tags) | **post** /api/nodes/{id}/tags/ | 
[**node_dissociate_tags**](#node_dissociate_tags) | **delete** /api/nodes/{id}/tags/ | 
[**nodes_create**](#nodes_create) | **post** /api/nodes/ | 
[**nodes_destroy**](#nodes_destroy) | **delete** /api/nodes/{id}/ | 
[**nodes_download_retrieve**](#nodes_download_retrieve) | **get** /api/nodes/download/ | 
[**nodes_inboxcount_retrieve**](#nodes_inboxcount_retrieve) | **get** /api/nodes/inboxcount/ | 
[**nodes_list**](#nodes_list) | **get** /api/nodes/ | 
[**nodes_move_create**](#nodes_move_create) | **post** /api/nodes/move/ | 
[**nodes_partial_update**](#nodes_partial_update) | **patch** /api/nodes/{id}/ | 
[**retrieve_node**](#retrieve_node) | **get** /api/nodes/{id}/ | 

# **node_append_tags**
<a name="node_append_tags"></a>
> NodeTags node_append_tags(id)



Appends given list of tag names to the node.  Retains all previously associated node tags. Yet another way of thinking about http PATCH method is as it **appends** input tags to the currently associated tags.  Example:      Node N1 has 'invoice', 'important' tags.      After following request:          POST /api/nodes/{N1}/tags/         {tags: ['paid']}      Node N1 will have 'invoice', 'important', 'paid' tags.     Notice that previously associated 'invoice' and 'important' tags     are still assigned to N1.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.patched_node_tags import PatchedNodeTags
from papermerge-restapi-client.model.node_tags import NodeTags
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.node_append_tags(
            path_params=path_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->node_append_tags: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = PatchedNodeTags(
        tags=[
            "tags_example"
        ],
    )
    try:
        api_response = api_instance.node_append_tags(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->node_append_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedNodeTags**](../../models/PatchedNodeTags.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#node_append_tags.ApiResponseFor200) | 

#### node_append_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeTags**](../../models/NodeTags.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **node_assign_tags**
<a name="node_assign_tags"></a>
> NodeTags node_assign_tags(idnode_tags)



Assigns given list of tag names to the node.  All tags not present in given list of tags names will be disassociated from the node; in other words upon successful completion of the request node will have ONLY tags from the list. Yet another way of thinking about http POST is as it **replaces existing node tags** with the one from input list.  Example:      Node N1 has 'invoice', 'important', 'unpaid' tags.      After following request:          POST /api/nodes/{N1}/tags/         {tags: ['invoice', 'important', 'paid']}      Node N1 will have 'invoice', 'important', 'paid' tags.     Notice that previously associated 'unpaid' tag is not     assigned to N1 anymore (because it was not in the provided list     of tags).  If you want to retain node tags not present in input tag list names then use PATCH/PUT http method of this endpoint.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.node_tags import NodeTags
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = NodeTags(
        tags=[
            "tags_example"
        ],
    )
    try:
        api_response = api_instance.node_assign_tags(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->node_assign_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeTags**](../../models/NodeTags.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#node_assign_tags.ApiResponseFor201) | 

#### node_assign_tags.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeTags**](../../models/NodeTags.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **node_dissociate_tags**
<a name="node_dissociate_tags"></a>
> node_dissociate_tags(id)



Dissociate given tags the node.  Tags models are not deleted - just dissociated from the node.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.node_dissociate_tags(
            path_params=path_params,
        )
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->node_dissociate_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#node_dissociate_tags.ApiResponseFor204) | No response body

#### node_dissociate_tags.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_create**
<a name="nodes_create"></a>
> Node nodes_create()



Creates a node.  A node can be either a Folder or a Document. In order to create a folder set required `type` attribute to `folders`. In order to create a document set `type` attribute to `documents`.  Created document won't have any file associated i.e. this REST API creates just document model in database.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.node import Node
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only optional values
    body = Node(
        data=dict(
            type="documents",
            id="id_example",
            attributes=dict(
                title="title_example",
                created_at="1970-01-01T00:00:00.00Z",
                updated_at="1970-01-01T00:00:00.00Z",
            ),
            relationships=dict(
                parent=Reltoone(
                    data=RelationshipToOne(
                        type="type_example",
                        id="id_example",
                    ),
                ),
            ),
        ),
    )
    try:
        api_response = api_instance.nodes_create(
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#nodes_create.ApiResponseFor201) | 

#### nodes_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_destroy**
<a name="nodes_destroy"></a>
> nodes_destroy(id)



Documents can be organized in folders. One folder can contain documents as well as other folders. A node is a convinient abstraction of two concepts - 'folder' and 'document'. Each node has a type field with value either 'folders' or 'documents' depending on what kind of node it is.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.nodes_destroy(
            path_params=path_params,
        )
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_destroy: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#nodes_destroy.ApiResponseFor204) | No response body

#### nodes_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_download_retrieve**
<a name="nodes_download_retrieve"></a>
> NodesDownload nodes_download_retrieve()



Expects one or multiple of following HTTP GET parameters: * node_ids (required) - a list of node IDs to download * file_name - preferred file name for downloaded archive/document file * include_version = 'only_last' or 'only_original'     In case when include_version == 'only_last', downloaded     archive/document file(s) will contain only last version     of the document     Respectively for include_version == 'only_original' downloaded     archive/document file(s) will contain only orignial version     of the document     Default value is 'only_last' * archive_type = 'zip' or 'targz'     Applies only if there is more than one node to download.     Decides on type of archive to create.     Default value is 'zip'

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.nodes_download import NodesDownload
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "json",
    }
    try:
        api_response = api_instance.nodes_download_retrieve(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_download_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
format | FormatSchema | | optional


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "vnd.api+json", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nodes_download_retrieve.ApiResponseFor200) | 

#### nodes_download_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodesDownload**](../../models/NodesDownload.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodesDownload**](../../models/NodesDownload.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_inboxcount_retrieve**
<a name="nodes_inboxcount_retrieve"></a>
> InboxCount nodes_inboxcount_retrieve()



### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.inbox_count import InboxCount
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "json",
    }
    try:
        api_response = api_instance.nodes_inboxcount_retrieve(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_inboxcount_retrieve: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
format | FormatSchema | | optional


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "vnd.api+json", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nodes_inboxcount_retrieve.ApiResponseFor200) | 

#### nodes_inboxcount_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboxCount**](../../models/InboxCount.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InboxCount**](../../models/InboxCount.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_list**
<a name="nodes_list"></a>
> PaginatedNodeList nodes_list()



Documents can be organized in folders. One folder can contain documents as well as other folders. A node is a convinient abstraction of two concepts - 'folder' and 'document'. Each node has a type field with value either 'folders' or 'documents' depending on what kind of node it is.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.paginated_node_list import PaginatedNodeList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only optional values
    query_params = {
        'filter[search]': "filter[search]_example",
        'page[number]': 1,
        'page[size]': 1,
        'sort': "sort_example",
    }
    try:
        api_response = api_instance.nodes_list(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter[search] | FilterSearchSchema | | optional
page[number] | PageNumberSchema | | optional
page[size] | PageSizeSchema | | optional
sort | SortSchema | | optional


# FilterSearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nodes_list.ApiResponseFor200) | 

#### nodes_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedNodeList**](../../models/PaginatedNodeList.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_move_create**
<a name="nodes_move_create"></a>
> NodeMove nodes_move_create(node_move)



### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.node_move import NodeMove
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = NodeMove(
        target_parent=NodeID(
            id="id_example",
        ),
        nodes=[
            NodeID()
        ],
    )
    try:
        api_response = api_instance.nodes_move_create(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_move_create: %s\n" % e)

    # example passing only optional values
    query_params = {
        'format': "json",
    }
    body = NodeMove(
        target_parent=NodeID(
            id="id_example",
        ),
        nodes=[
            NodeID()
        ],
    )
    try:
        api_response = api_instance.nodes_move_create(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_move_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeMove**](../../models/NodeMove.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
format | FormatSchema | | optional


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["json", "vnd.api+json", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nodes_move_create.ApiResponseFor200) | 

#### nodes_move_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeMove**](../../models/NodeMove.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeMove**](../../models/NodeMove.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nodes_partial_update**
<a name="nodes_partial_update"></a>
> Node nodes_partial_update(id)



Documents can be organized in folders. One folder can contain documents as well as other folders. A node is a convinient abstraction of two concepts - 'folder' and 'document'. Each node has a type field with value either 'folders' or 'documents' depending on what kind of node it is.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.node import Node
from papermerge-restapi-client.model.patched_node import PatchedNode
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.nodes_partial_update(
            path_params=path_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_partial_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = PatchedNode(
        data=dict(
            type="documents",
            id="id_example",
            attributes=dict(
                title="title_example",
                created_at="1970-01-01T00:00:00.00Z",
                updated_at="1970-01-01T00:00:00.00Z",
            ),
            relationships=dict(
                parent=Reltoone(
                    data=RelationshipToOne(
                        type="type_example",
                        id="id_example",
                    ),
                ),
            ),
        ),
    )
    try:
        api_response = api_instance.nodes_partial_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->nodes_partial_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchedNode**](../../models/PatchedNode.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nodes_partial_update.ApiResponseFor200) | 

#### nodes_partial_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_node**
<a name="retrieve_node"></a>
> Node retrieve_node(id)



Documents can be organized in folders. One folder can contain documents as well as other folders. A node is a convinient abstraction of two concepts - 'folder' and 'document'. Each node has a type field with value either 'folders' or 'documents' depending on what kind of node it is.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import nodes_api
from papermerge-restapi-client.model.node import Node
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge-restapi-client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token Authentication
configuration.api_key['Token Authentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token Authentication'] = 'Bearer'
# Enter a context with an instance of the API client
with papermerge-restapi-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.retrieve_node(
            path_params=path_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling NodesApi->retrieve_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_node.ApiResponseFor200) | 

#### retrieve_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

