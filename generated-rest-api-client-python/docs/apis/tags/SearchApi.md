<a name="__pageTop"></a>
# papermerge_restapi_client.apis.tags.search_api.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](#search) | **get** /api/search/ | 

# **search**
<a name="search"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] search()



Performs full text search on the documents and folders.  Folders are matched by their title and assigned tags. Documents are matched by title, OCRed text and assigned tags.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge_restapi_client
from papermerge_restapi_client.apis.tags import search_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = papermerge_restapi_client.Configuration(
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
with papermerge_restapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    query_params = {
        'q': "q_example",
        'tags': "tags_example",
        'tags_op': "all",
    }
    try:
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge_restapi_client.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
q | QSchema | | optional
tags | TagsSchema | | optional
tags_op | TagsOpSchema | | optional


# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagsOpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["all", "any", ] if omitted the server will use the default value of "all"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search.ApiResponseFor200) | 

#### search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**text** | None, str,  | NoneClass, str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**[breadcrumb](#breadcrumb)** | list, tuple,  | tuple,  |  | [optional] 
**node_type** | str,  | str,  |  | [optional] 
**highlight** | None, str,  | NoneClass, str,  |  | [optional] 
**user_id** | None, str, uuid.UUID,  | NoneClass, str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# breadcrumb

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

