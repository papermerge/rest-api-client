import localVarRequest from 'request';

export * from './archiveTypeEnum';
export * from './authToken';
export * from './customUserPreference';
export * from './datum';
export * from './documentDetails';
export * from './documentDetailsData';
export * from './documentDetailsDataAttributes';
export * from './documentDetailsDataRelationships';
export * from './documentVersion';
export * from './documentVersionOcrText';
export * from './documentsMerge';
export * from './errorSource';
export * from './failure';
export * from './folder';
export * from './folderData';
export * from './folderDataAttributes';
export * from './group';
export * from './groupData';
export * from './groupDataAttributes';
export * from './groupDataRelationships';
export * from './inboxCount';
export * from './includeVersionEnum';
export * from './jsonapi';
export * from './link';
export * from './linkOneOf';
export * from './linkage';
export * from './modelError';
export * from './node';
export * from './nodeData';
export * from './nodeDataAttributes';
export * from './nodeID';
export * from './nodeMove';
export * from './nodeTags';
export * from './nodeTypeEnum';
export * from './nodesDownload';
export * from './ocr';
export * from './onlymeta';
export * from './page';
export * from './pageData';
export * from './pageDataAttributes';
export * from './pageDataRelationships';
export * from './pageReorder';
export * from './pageRotate';
export * from './pageref';
export * from './pagesMoveToDocument';
export * from './pagesMoveToFolder';
export * from './pagesReorder';
export * from './pagesRotate';
export * from './paginatedCustomUserPreferenceList';
export * from './paginatedCustomUserPreferenceListLinks';
export * from './paginatedCustomUserPreferenceListMeta';
export * from './paginatedCustomUserPreferenceListMetaPagination';
export * from './paginatedDocumentDetailsList';
export * from './paginatedFolderList';
export * from './paginatedGroupList';
export * from './paginatedNodeList';
export * from './paginatedTagList';
export * from './paginatedTokenList';
export * from './paginatedUserList';
export * from './pagination';
export * from './password';
export * from './patchedCustomUserPreference';
export * from './patchedDocumentDetails';
export * from './patchedFolder';
export * from './patchedGroup';
export * from './patchedNode';
export * from './patchedNodeTags';
export * from './patchedTag';
export * from './patchedTagData';
export * from './patchedTagDataAttributes';
export * from './patchedUser';
export * from './patchedUserData';
export * from './patchedUserDataAttributes';
export * from './patchedUserDataRelationships';
export * from './permission';
export * from './relationshipLinks';
export * from './relationshipToOne';
export * from './reltomany';
export * from './reltoone';
export * from './resource';
export * from './resourceIdentifierObject';
export * from './searchResult';
export * from './tag';
export * from './token';
export * from './tokenData';
export * from './tokenDataAttributes';
export * from './user';
export * from './version';

import * as fs from 'fs';

export interface RequestDetailedFile {
    value: Buffer;
    options?: {
        filename?: string;
        contentType?: string;
    }
}

export type RequestFile = string | Buffer | fs.ReadStream | RequestDetailedFile;


import { ArchiveTypeEnum } from './archiveTypeEnum';
import { AuthToken } from './authToken';
import { CustomUserPreference } from './customUserPreference';
import { Datum } from './datum';
import { DocumentDetails } from './documentDetails';
import { DocumentDetailsData } from './documentDetailsData';
import { DocumentDetailsDataAttributes } from './documentDetailsDataAttributes';
import { DocumentDetailsDataRelationships } from './documentDetailsDataRelationships';
import { DocumentVersion } from './documentVersion';
import { DocumentVersionOcrText } from './documentVersionOcrText';
import { DocumentsMerge } from './documentsMerge';
import { ErrorSource } from './errorSource';
import { Failure } from './failure';
import { Folder } from './folder';
import { FolderData } from './folderData';
import { FolderDataAttributes } from './folderDataAttributes';
import { Group } from './group';
import { GroupData } from './groupData';
import { GroupDataAttributes } from './groupDataAttributes';
import { GroupDataRelationships } from './groupDataRelationships';
import { InboxCount } from './inboxCount';
import { IncludeVersionEnum } from './includeVersionEnum';
import { Jsonapi } from './jsonapi';
import { Link } from './link';
import { LinkOneOf } from './linkOneOf';
import { Linkage } from './linkage';
import { ModelError } from './modelError';
import { Node } from './node';
import { NodeData } from './nodeData';
import { NodeDataAttributes } from './nodeDataAttributes';
import { NodeID } from './nodeID';
import { NodeMove } from './nodeMove';
import { NodeTags } from './nodeTags';
import { NodeTypeEnum } from './nodeTypeEnum';
import { NodesDownload } from './nodesDownload';
import { Ocr } from './ocr';
import { Onlymeta } from './onlymeta';
import { Page } from './page';
import { PageData } from './pageData';
import { PageDataAttributes } from './pageDataAttributes';
import { PageDataRelationships } from './pageDataRelationships';
import { PageReorder } from './pageReorder';
import { PageRotate } from './pageRotate';
import { Pageref } from './pageref';
import { PagesMoveToDocument } from './pagesMoveToDocument';
import { PagesMoveToFolder } from './pagesMoveToFolder';
import { PagesReorder } from './pagesReorder';
import { PagesRotate } from './pagesRotate';
import { PaginatedCustomUserPreferenceList } from './paginatedCustomUserPreferenceList';
import { PaginatedCustomUserPreferenceListLinks } from './paginatedCustomUserPreferenceListLinks';
import { PaginatedCustomUserPreferenceListMeta } from './paginatedCustomUserPreferenceListMeta';
import { PaginatedCustomUserPreferenceListMetaPagination } from './paginatedCustomUserPreferenceListMetaPagination';
import { PaginatedDocumentDetailsList } from './paginatedDocumentDetailsList';
import { PaginatedFolderList } from './paginatedFolderList';
import { PaginatedGroupList } from './paginatedGroupList';
import { PaginatedNodeList } from './paginatedNodeList';
import { PaginatedTagList } from './paginatedTagList';
import { PaginatedTokenList } from './paginatedTokenList';
import { PaginatedUserList } from './paginatedUserList';
import { Pagination } from './pagination';
import { Password } from './password';
import { PatchedCustomUserPreference } from './patchedCustomUserPreference';
import { PatchedDocumentDetails } from './patchedDocumentDetails';
import { PatchedFolder } from './patchedFolder';
import { PatchedGroup } from './patchedGroup';
import { PatchedNode } from './patchedNode';
import { PatchedNodeTags } from './patchedNodeTags';
import { PatchedTag } from './patchedTag';
import { PatchedTagData } from './patchedTagData';
import { PatchedTagDataAttributes } from './patchedTagDataAttributes';
import { PatchedUser } from './patchedUser';
import { PatchedUserData } from './patchedUserData';
import { PatchedUserDataAttributes } from './patchedUserDataAttributes';
import { PatchedUserDataRelationships } from './patchedUserDataRelationships';
import { Permission } from './permission';
import { RelationshipLinks } from './relationshipLinks';
import { RelationshipToOne } from './relationshipToOne';
import { Reltomany } from './reltomany';
import { Reltoone } from './reltoone';
import { Resource } from './resource';
import { ResourceIdentifierObject } from './resourceIdentifierObject';
import { SearchResult } from './searchResult';
import { Tag } from './tag';
import { Token } from './token';
import { TokenData } from './tokenData';
import { TokenDataAttributes } from './tokenDataAttributes';
import { User } from './user';
import { Version } from './version';

/* tslint:disable:no-unused-variable */
let primitives = [
                    "string",
                    "boolean",
                    "double",
                    "integer",
                    "long",
                    "float",
                    "number",
                    "any"
                 ];

let enumsMap: {[index: string]: any} = {
        "ArchiveTypeEnum": ArchiveTypeEnum,
        "DocumentDetailsData.TypeEnum": DocumentDetailsData.TypeEnum,
        "DocumentDetailsDataAttributes.OcrStatusEnum": DocumentDetailsDataAttributes.OcrStatusEnum,
        "FolderData.TypeEnum": FolderData.TypeEnum,
        "GroupData.TypeEnum": GroupData.TypeEnum,
        "IncludeVersionEnum": IncludeVersionEnum,
        "NodeData.TypeEnum": NodeData.TypeEnum,
        "NodeTypeEnum": NodeTypeEnum,
        "PageData.TypeEnum": PageData.TypeEnum,
        "PatchedTagData.TypeEnum": PatchedTagData.TypeEnum,
        "PatchedUserData.TypeEnum": PatchedUserData.TypeEnum,
        "TokenData.TypeEnum": TokenData.TypeEnum,
}

let typeMap: {[index: string]: any} = {
    "AuthToken": AuthToken,
    "CustomUserPreference": CustomUserPreference,
    "Datum": Datum,
    "DocumentDetails": DocumentDetails,
    "DocumentDetailsData": DocumentDetailsData,
    "DocumentDetailsDataAttributes": DocumentDetailsDataAttributes,
    "DocumentDetailsDataRelationships": DocumentDetailsDataRelationships,
    "DocumentVersion": DocumentVersion,
    "DocumentVersionOcrText": DocumentVersionOcrText,
    "DocumentsMerge": DocumentsMerge,
    "ErrorSource": ErrorSource,
    "Failure": Failure,
    "Folder": Folder,
    "FolderData": FolderData,
    "FolderDataAttributes": FolderDataAttributes,
    "Group": Group,
    "GroupData": GroupData,
    "GroupDataAttributes": GroupDataAttributes,
    "GroupDataRelationships": GroupDataRelationships,
    "InboxCount": InboxCount,
    "Jsonapi": Jsonapi,
    "Link": Link,
    "LinkOneOf": LinkOneOf,
    "Linkage": Linkage,
    "ModelError": ModelError,
    "Node": Node,
    "NodeData": NodeData,
    "NodeDataAttributes": NodeDataAttributes,
    "NodeID": NodeID,
    "NodeMove": NodeMove,
    "NodeTags": NodeTags,
    "NodesDownload": NodesDownload,
    "Ocr": Ocr,
    "Onlymeta": Onlymeta,
    "Page": Page,
    "PageData": PageData,
    "PageDataAttributes": PageDataAttributes,
    "PageDataRelationships": PageDataRelationships,
    "PageReorder": PageReorder,
    "PageRotate": PageRotate,
    "Pageref": Pageref,
    "PagesMoveToDocument": PagesMoveToDocument,
    "PagesMoveToFolder": PagesMoveToFolder,
    "PagesReorder": PagesReorder,
    "PagesRotate": PagesRotate,
    "PaginatedCustomUserPreferenceList": PaginatedCustomUserPreferenceList,
    "PaginatedCustomUserPreferenceListLinks": PaginatedCustomUserPreferenceListLinks,
    "PaginatedCustomUserPreferenceListMeta": PaginatedCustomUserPreferenceListMeta,
    "PaginatedCustomUserPreferenceListMetaPagination": PaginatedCustomUserPreferenceListMetaPagination,
    "PaginatedDocumentDetailsList": PaginatedDocumentDetailsList,
    "PaginatedFolderList": PaginatedFolderList,
    "PaginatedGroupList": PaginatedGroupList,
    "PaginatedNodeList": PaginatedNodeList,
    "PaginatedTagList": PaginatedTagList,
    "PaginatedTokenList": PaginatedTokenList,
    "PaginatedUserList": PaginatedUserList,
    "Pagination": Pagination,
    "Password": Password,
    "PatchedCustomUserPreference": PatchedCustomUserPreference,
    "PatchedDocumentDetails": PatchedDocumentDetails,
    "PatchedFolder": PatchedFolder,
    "PatchedGroup": PatchedGroup,
    "PatchedNode": PatchedNode,
    "PatchedNodeTags": PatchedNodeTags,
    "PatchedTag": PatchedTag,
    "PatchedTagData": PatchedTagData,
    "PatchedTagDataAttributes": PatchedTagDataAttributes,
    "PatchedUser": PatchedUser,
    "PatchedUserData": PatchedUserData,
    "PatchedUserDataAttributes": PatchedUserDataAttributes,
    "PatchedUserDataRelationships": PatchedUserDataRelationships,
    "Permission": Permission,
    "RelationshipLinks": RelationshipLinks,
    "RelationshipToOne": RelationshipToOne,
    "Reltomany": Reltomany,
    "Reltoone": Reltoone,
    "Resource": Resource,
    "ResourceIdentifierObject": ResourceIdentifierObject,
    "SearchResult": SearchResult,
    "Tag": Tag,
    "Token": Token,
    "TokenData": TokenData,
    "TokenDataAttributes": TokenDataAttributes,
    "User": User,
    "Version": Version,
}

export class ObjectSerializer {
    public static findCorrectType(data: any, expectedType: string) {
        if (data == undefined) {
            return expectedType;
        } else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        } else if (expectedType === "Date") {
            return expectedType;
        } else {
            if (enumsMap[expectedType]) {
                return expectedType;
            }

            if (!typeMap[expectedType]) {
                return expectedType; // w/e we don't know the type
            }

            // Check the discriminator
            let discriminatorProperty = typeMap[expectedType].discriminator;
            if (discriminatorProperty == null) {
                return expectedType; // the type does not have a discriminator. use it.
            } else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if(typeMap[discriminatorType]){
                        return discriminatorType; // use the type given in the discriminator
                    } else {
                        return expectedType; // discriminator did not map to a type
                    }
                } else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }

    public static serialize(data: any, type: string) {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.serialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return data.toISOString();
        } else {
            if (enumsMap[type]) {
                return data;
            }
            if (!typeMap[type]) { // in case we dont know the type
                return data;
            }

            // Get the actual type of this object
            type = this.findCorrectType(data, type);

            // get the map for the correct type.
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            let instance: {[index: string]: any} = {};
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }

    public static deserialize(data: any, type: string) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index = 0; index < data.length; index++) {
                let datum = data[index];
                transformedData.push(ObjectSerializer.deserialize(datum, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return new Date(data);
        } else {
            if (enumsMap[type]) {// is Enum
                return data;
            }

            if (!typeMap[type]) { // dont know the type
                return data;
            }
            let instance = new typeMap[type]();
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            for (let index = 0; index < attributeTypes.length; index++) {
                let attributeType = attributeTypes[index];
                instance[attributeType.name] = ObjectSerializer.deserialize(data[attributeType.baseName], attributeType.type);
            }
            return instance;
        }
    }
}

export interface Authentication {
    /**
    * Apply authentication settings to header and query params.
    */
    applyToRequest(requestOptions: localVarRequest.Options): Promise<void> | void;
}

export class HttpBasicAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        requestOptions.auth = {
            username: this.username, password: this.password
        }
    }
}

export class HttpBearerAuth implements Authentication {
    public accessToken: string | (() => string) = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            const accessToken = typeof this.accessToken === 'function'
                            ? this.accessToken()
                            : this.accessToken;
            requestOptions.headers["Authorization"] = "Bearer " + accessToken;
        }
    }
}

export class ApiKeyAuth implements Authentication {
    public apiKey: string = '';

    constructor(private location: string, private paramName: string) {
    }

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (this.location == "query") {
            (<any>requestOptions.qs)[this.paramName] = this.apiKey;
        } else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        } else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}

export class OAuth implements Authentication {
    public accessToken: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}

export class VoidAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(_: localVarRequest.Options): void {
        // Do nothing
    }
}

export type Interceptor = (requestOptions: localVarRequest.Options) => (Promise<void> | void);
