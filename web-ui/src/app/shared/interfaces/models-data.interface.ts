import { PermissionEnum } from 'src/app/core/configs/permissions';

export interface ModelModel {
  aliases: Record<string, unknown>;
  description: string;
  name: string;
  tags: Record<string, unknown>;
}


export interface ModelPermissionsModel {
  models: ModelPermissionModel[];
}

export interface ModelPermissionModel {
  name: string;
  permission: PermissionEnum;
}

export interface ModelUserListModel {
  permission: PermissionEnum;
  username: string;
}
