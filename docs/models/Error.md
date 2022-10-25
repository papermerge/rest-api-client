# papermerge-restapi-client.model.error.Error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**links** | [**Links**](Links.md) | [**Links**](Links.md) |  | [optional] 
**code** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**detail** | str,  | str,  |  | [optional] 
**[source](#source)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 

# source

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pointer** | str,  | str,  | A [JSON Pointer](https://tools.ietf.org/html/rfc6901) to the associated entity in the request document [e.g. &#x60;/data&#x60; for a primary data object, or &#x60;/data/attributes/title&#x60; for a specific attribute. | [optional] 
**parameter** | str,  | str,  | A string indicating which query parameter caused the error. | [optional] 
**meta** | [**Meta**](Meta.md) | [**Meta**](Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

