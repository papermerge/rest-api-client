export * from './authApi';
import { AuthApi } from './authApi';
export * from './documentVersionsApi';
import { DocumentVersionsApi } from './documentVersionsApi';
export * from './documentsApi';
import { DocumentsApi } from './documentsApi';
export * from './foldersApi';
import { FoldersApi } from './foldersApi';
export * from './groupsApi';
import { GroupsApi } from './groupsApi';
export * from './nodesApi';
import { NodesApi } from './nodesApi';
export * from './ocrApi';
import { OcrApi } from './ocrApi';
export * from './pagesApi';
import { PagesApi } from './pagesApi';
export * from './permissionsApi';
import { PermissionsApi } from './permissionsApi';
export * from './preferencesApi';
import { PreferencesApi } from './preferencesApi';
export * from './schemaApi';
import { SchemaApi } from './schemaApi';
export * from './searchApi';
import { SearchApi } from './searchApi';
export * from './tagsApi';
import { TagsApi } from './tagsApi';
export * from './tokensApi';
import { TokensApi } from './tokensApi';
export * from './usersApi';
import { UsersApi } from './usersApi';
export * from './versionApi';
import { VersionApi } from './versionApi';
import * as http from 'http';

export class HttpError extends Error {
    constructor (public response: http.IncomingMessage, public body: any, public statusCode?: number) {
        super('HTTP request failed');
        this.name = 'HttpError';
    }
}

export { RequestFile } from '../model/models';

export const APIS = [AuthApi, DocumentVersionsApi, DocumentsApi, FoldersApi, GroupsApi, NodesApi, OcrApi, PagesApi, PermissionsApi, PreferencesApi, SchemaApi, SearchApi, TagsApi, TokensApi, UsersApi, VersionApi];
