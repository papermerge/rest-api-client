<a name="__pageTop"></a>
# papermerge_restapi_client.apis.tags.auth_api.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_create**](#auth_login_create) | **post** /api/auth/login/ | 
[**auth_logout_create**](#auth_logout_create) | **post** /api/auth/logout/ | 
[**auth_logoutall_create**](#auth_logoutall_create) | **post** /api/auth/logoutall/ | 

# **auth_login_create**
<a name="auth_login_create"></a>
> AuthToken auth_login_create(auth_token)



Authenticates user with given username and password. Response will contain token to be used as part of ``Authorization`` header in subsequent requests whenever authorization is required.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge_restapi_client
from papermerge_restapi_client.apis.tags import auth_api
from papermerge_restapi_client.model.auth_token import AuthToken
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
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = AuthToken(
        username="username_example",
        password="password_example",
        token="token_example",
    )
    try:
        api_response = api_instance.auth_login_create(
            body=body,
        )
        pprint(api_response)
    except papermerge_restapi_client.ApiException as e:
        print("Exception when calling AuthApi->auth_login_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthToken**](../../models/AuthToken.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_login_create.ApiResponseFor200) | 

#### auth_login_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthToken**](../../models/AuthToken.md) |  | 


### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_logout_create**
<a name="auth_logout_create"></a>
> auth_logout_create()



Logs the user out of current session.  On a successful request, the token used to authenticate is deleted from the system and can no longer be used for authentication.  Request body must be empty.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge_restapi_client
from papermerge_restapi_client.apis.tags import auth_api
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
    api_instance = auth_api.AuthApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "json",
    }
    try:
        api_response = api_instance.auth_logout_create(
            query_params=query_params,
        )
    except papermerge_restapi_client.ApiException as e:
        print("Exception when calling AuthApi->auth_logout_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
200 | [ApiResponseFor200](#auth_logout_create.ApiResponseFor200) | No response body

#### auth_logout_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_logoutall_create**
<a name="auth_logoutall_create"></a>
> auth_logoutall_create()



Logs the user out of all sessions i.e. deletes all auth tokens for the user.  On a successful request, the token used to authenticate, and all other tokens registered to the same user account, are deleted from the system and can no longer be used for authentication.  Request body must be empty.

### Example

* Api Key Authentication (Token Authentication):
```python
import papermerge_restapi_client
from papermerge_restapi_client.apis.tags import auth_api
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
    api_instance = auth_api.AuthApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "json",
    }
    try:
        api_response = api_instance.auth_logoutall_create(
            query_params=query_params,
        )
    except papermerge_restapi_client.ApiException as e:
        print("Exception when calling AuthApi->auth_logoutall_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
200 | [ApiResponseFor200](#auth_logoutall_create.ApiResponseFor200) | No response body

#### auth_logoutall_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[Token Authentication](../../../README.md#Token Authentication)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

