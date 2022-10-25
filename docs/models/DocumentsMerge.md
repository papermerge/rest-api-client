# papermerge_restapi_client.model.documents_merge.DocumentsMerge

A `Serializer` is a model-less serializer class with additional support for JSON:API spec features.  As in JSON:API specification a type is always required you need to make sure that you define `resource_name` in your `Meta` class when deriving from this class.  Included Mixins:  * A mixin class to enable sparse fieldsets is included * A mixin class to enable validation of included resources is included

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A &#x60;Serializer&#x60; is a model-less serializer class with additional support for JSON:API spec features.  As in JSON:API specification a type is always required you need to make sure that you define &#x60;resource_name&#x60; in your &#x60;Meta&#x60; class when deriving from this class.  Included Mixins:  * A mixin class to enable sparse fieldsets is included * A mixin class to enable validation of included resources is included | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dst** | str, uuid.UUID,  | str,  |  | value must be a uuid
**src** | str, uuid.UUID,  | str,  |  | value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

