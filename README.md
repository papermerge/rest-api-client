# Generated REST API clients for Papermerge

This project contains source code of automatically generated REST API clients for Papermerge.

REST API clients are generated based on [OpenAPI schema](https://github.com/papermerge/openapi-schema/blob/master/openapi-schema.yaml).

## Python Client

Command used:

``sh
openapi-generator-cli generate -i https://raw.githubusercontent.com/papermerge/openapi-schema/master/openapi-schema.yaml -g python -o generated-rest-api-client-python --skip-validate-spec --additional-properties packageName=papermerge_restapi_client,projectName=papermerge-restapi-client
``
