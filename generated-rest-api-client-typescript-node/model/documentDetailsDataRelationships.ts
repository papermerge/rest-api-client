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
import { Reltoone } from './reltoone';

export class DocumentDetailsDataRelationships {
    'parent'?: Reltoone;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "parent",
            "baseName": "parent",
            "type": "Reltoone"
        }    ];

    static getAttributeTypeMap() {
        return DocumentDetailsDataRelationships.attributeTypeMap;
    }
}

