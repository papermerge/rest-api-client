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
import { DocumentDetailsDataRelationships } from './documentDetailsDataRelationships';
import { NodeDataAttributes } from './nodeDataAttributes';

export class NodeData {
    'type': NodeData.TypeEnum;
    'id'?: string;
    'attributes'?: NodeDataAttributes;
    'relationships'?: DocumentDetailsDataRelationships;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "type",
            "type": "NodeData.TypeEnum"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "attributes",
            "baseName": "attributes",
            "type": "NodeDataAttributes"
        },
        {
            "name": "relationships",
            "baseName": "relationships",
            "type": "DocumentDetailsDataRelationships"
        }    ];

    static getAttributeTypeMap() {
        return NodeData.attributeTypeMap;
    }
}

export namespace NodeData {
    export enum TypeEnum {
        Documents = <any> 'documents',
        Folders = <any> 'folders'
    }
}
