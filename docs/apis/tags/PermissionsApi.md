<a name="__pageTop"></a>
# papermerge-restapi-client.apis.tags.permissions_api.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_list**](#permissions_list) | **get** /api/permissions/ | 

# **permissions_list**
<a name="permissions_list"></a>
> [Permission] permissions_list()



Retrieves (almost) ALL permissions available in the system.  It is useful to be able to retrieve (almost) ALL permission resource objects available - for example when creating a new Role you need to know what permissions are available and then select couple of available permissions and associate them to the newly create Role.  Some permissions available will never be returned by this endpoint (hence \"almost all\"). For example permissions for internally used 'BaseTreeNode' model. User is not aware what is 'BaseTreeNode' and getting permission for that will only confuse him/her. Permissions used to grant access per node/object are not returned either.  In order to access this endpoint you need **view_permission** permission.  Don't confuse this endpoint with \"user permissions\", which is intended, as name suggests, to return only user specific permissions. In order to retrieve current user permissions use /api/users/me/ endpoint.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import permissions_api
from papermerge-restapi-client.model.permission import Permission
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
    api_instance = permissions_api.PermissionsApi(api_client)

    # example passing only optional values
    query_params = {
        'filter[search]': "filter[search]_example",
        'sort': "sort_example",
    }
    try:
        api_response = api_instance.permissions_list(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling PermissionsApi->permissions_list: %s\n" % e)
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
sort | SortSchema | | optional


# FilterSearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#permissions_list.ApiResponseFor200) | 

#### permissions_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Permission**]({{complexTypePrefix}}Permission.md) | [**Permission**]({{complexTypePrefix}}Permission.md) | [**Permission**]({{complexTypePrefix}}Permission.md) |  | 

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

