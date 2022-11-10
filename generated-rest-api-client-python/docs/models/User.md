# papermerge_restapi_client.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**UserTypeEnum**](UserTypeEnum.md) | [**UserTypeEnum**](UserTypeEnum.md) |  | 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[relationships](#relationships)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**username** | str,  | str,  | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | str,  | str,  |  | [optional] 
**last_name** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**is_active** | bool,  | BoolClass,  | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**is_staff** | bool,  | BoolClass,  | Designates whether the user can log into this admin site. | [optional] 
**is_superuser** | bool,  | BoolClass,  | Designates that this user has all permissions without explicitly assigning them. | [optional] 
**date_joined** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[user_permissions](#user_permissions)** | list, tuple,  | tuple,  |  | [optional] 
**[perm_codenames](#perm_codenames)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Permission**](Permission.md) | [**Permission**](Permission.md) | [**Permission**](Permission.md) |  | 

# perm_codenames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relationships

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inbox_folder** | [**Reltoone**](Reltoone.md) | [**Reltoone**](Reltoone.md) |  | [optional] 
**home_folder** | [**Reltoone**](Reltoone.md) | [**Reltoone**](Reltoone.md) |  | [optional] 
**groups** | [**Reltomany**](Reltomany.md) | [**Reltomany**](Reltomany.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

