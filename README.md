# Generated REST API clients for Papermerge

This project contains source code of automatically generated REST API clients for Papermerge.

All REST API clients are generated using [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator) based on [OpenAPI schema](https://github.com/papermerge/openapi-schema/blob/master/openapi-schema.yaml).

## Python Client

Command used:

```sh
openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/papermerge/openapi-schema/master/openapi-schema.yaml \
    -g python \
    -o generated-rest-api-client-python \
    --skip-validate-spec \
    --additional-properties packageName=papermerge_restapi_client,projectName=papermerge-restapi-client,packageVersion=1.0.1
```

Find mode details about [openapi-cli python generator here](https://openapi-generator.tech/docs/generators/python)


## TypeScript Client

Command used:

```sh
openapi-generator-cli generate \
     -i https://raw.githubusercontent.com/papermerge/openapi-schema/master/openapi-schema.yaml \
     -g typescript-node \
     -o generated-rest-api-client-typescript-node \
     --skip-validate-spec \
     --additional-properties npmName=papermerge-restapi-client
```