# papermerge-restapi-client.model.document_version.DocumentVersion

A `ModelSerializer` is just a regular `Serializer`, except that:  * A set of default fields are automatically populated. * A set of default validators are automatically populated. * Default `.create()` and `.update()` implementations are provided.  The process of automatically determining a set of serializer fields based on the model fields is reasonably complex, but you almost certainly don't need to dig into the implementation.  If the `ModelSerializer` class *doesn't* generate the set of fields that you need you should either declare the extra/differing fields explicitly on the serializer class, or simply use a `Serializer` class.   Included Mixins:  * A mixin class to enable sparse fieldsets is included * A mixin class to enable validation of included resources is included

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A &#x60;ModelSerializer&#x60; is just a regular &#x60;Serializer&#x60;, except that:  * A set of default fields are automatically populated. * A set of default validators are automatically populated. * Default &#x60;.create()&#x60; and &#x60;.update()&#x60; implementations are provided.  The process of automatically determining a set of serializer fields based on the model fields is reasonably complex, but you almost certainly don&#x27;t need to dig into the implementation.  If the &#x60;ModelSerializer&#x60; class *doesn&#x27;t* generate the set of fields that you need you should either declare the extra/differing fields explicitly on the serializer class, or simply use a &#x60;Serializer&#x60; class.   Included Mixins:  * A mixin class to enable sparse fieldsets is included * A mixin class to enable validation of included resources is included | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[pages](#pages)** | list, tuple,  | tuple,  |  | 
**document** | str, uuid.UUID,  | str,  |  | value must be a uuid
**download_url** | str,  | str,  |  | 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**lang** | str,  | str,  |  | [optional] 
**file_name** | None, str,  | NoneClass, str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | Size of file_orig attached. Size is in Bytes | [optional] 
**page_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**short_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

