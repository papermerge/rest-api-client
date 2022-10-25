# papermerge_restapi_client.model.page_reorder.PageReorder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**old_number** | decimal.Decimal, int,  | decimal.Decimal,  | Page position within the document before  page&#x27;s order change.Position numbering starts with 1. | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**new_number** | decimal.Decimal, int,  | decimal.Decimal,  | Desired new page position within the document. Position numbering starts with 1. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

