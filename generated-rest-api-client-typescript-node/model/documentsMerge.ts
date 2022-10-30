/**
 * Papermerge REST API
 * Document management system designed for digital archives
 *
 * The version of the OpenAPI document: 2.1.0b12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* A `Serializer` is a model-less serializer class with additional support for JSON:API spec features.  As in JSON:API specification a type is always required you need to make sure that you define `resource_name` in your `Meta` class when deriving from this class.  Included Mixins:  * A mixin class to enable sparse fieldsets is included * A mixin class to enable validation of included resources is included
*/
export class DocumentsMerge {
    'src': string;
    'dst': string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "src",
            "baseName": "src",
            "type": "string"
        },
        {
            "name": "dst",
            "baseName": "dst",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DocumentsMerge.attributeTypeMap;
    }
}

