<a name="__pageTop"></a>
# papermerge-restapi-client.apis.tags.tokens_api.TokensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_create**](#tokens_create) | **post** /api/tokens/ | 
[**tokens_destroy**](#tokens_destroy) | **delete** /api/tokens/{digest}/ | 
[**tokens_list**](#tokens_list) | **get** /api/tokens/ | 
[**tokens_retrieve**](#tokens_retrieve) | **get** /api/tokens/{digest}/ | 

# **tokens_create**
<a name="tokens_create"></a>
> Token tokens_create()



Each user can have multiple authentication tokens. The reason to have multiple tokens per user is that he (or she) may consume REST API from multiple clients (or devices) using one single user account. User may then use a separate authentication token per each device or client.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import tokens_api
from papermerge-restapi-client.model.token import Token
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
    api_instance = tokens_api.TokensApi(api_client)

    # example passing only optional values
    body = Token(
        data=dict(
            type="tokens",
            id="id_example",
            attributes=dict(
                token="token_example",
                digest="digest_example",
                created="1970-01-01T00:00:00.00Z",
                expiry="1970-01-01T00:00:00.00Z",
            ),
        ),
    )
    try:
        api_response = api_instance.tokens_create(
            body=body,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling TokensApi->tokens_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndApijson, SchemaForRequestBodyApplicationJson, SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/vnd.api+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.api+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#tokens_create.ApiResponseFor201) | 

#### tokens_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tokens_destroy**
<a name="tokens_destroy"></a>
> tokens_destroy(digest)



Each user can have multiple authentication tokens. The reason to have multiple tokens per user is that he (or she) may consume REST API from multiple clients (or devices) using one single user account. User may then use a separate authentication token per each device or client.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import tokens_api
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
    api_instance = tokens_api.TokensApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'digest': "digest_example",
    }
    try:
        api_response = api_instance.tokens_destroy(
            path_params=path_params,
        )
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling TokensApi->tokens_destroy: %s\n" % e)
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
digest | DigestSchema | | 

# DigestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#tokens_destroy.ApiResponseFor204) | No response body

#### tokens_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tokens_list**
<a name="tokens_list"></a>
> PaginatedTokenList tokens_list()



Each user can have multiple authentication tokens. The reason to have multiple tokens per user is that he (or she) may consume REST API from multiple clients (or devices) using one single user account. User may then use a separate authentication token per each device or client.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import tokens_api
from papermerge-restapi-client.model.paginated_token_list import PaginatedTokenList
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
    api_instance = tokens_api.TokensApi(api_client)

    # example passing only optional values
    query_params = {
        'filter[search]': "filter[search]_example",
        'page[number]': 1,
        'page[size]': 1,
        'sort': "sort_example",
    }
    try:
        api_response = api_instance.tokens_list(
            query_params=query_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling TokensApi->tokens_list: %s\n" % e)
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
200 | [ApiResponseFor200](#tokens_list.ApiResponseFor200) | 

#### tokens_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedTokenList**](../../models/PaginatedTokenList.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tokens_retrieve**
<a name="tokens_retrieve"></a>
> Token tokens_retrieve(digest)



Each user can have multiple authentication tokens. The reason to have multiple tokens per user is that he (or she) may consume REST API from multiple clients (or devices) using one single user account. User may then use a separate authentication token per each device or client.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge-restapi-client
from papermerge-restapi-client.apis.tags import tokens_api
from papermerge-restapi-client.model.token import Token
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
    api_instance = tokens_api.TokensApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'digest': "digest_example",
    }
    try:
        api_response = api_instance.tokens_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except papermerge-restapi-client.ApiException as e:
        print("Exception when calling TokensApi->tokens_retrieve: %s\n" % e)
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
digest | DigestSchema | | 

# DigestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tokens_retrieve.ApiResponseFor200) | 

#### tokens_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndApijson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndApijson
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

