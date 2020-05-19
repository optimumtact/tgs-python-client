# UserUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Cleartext password of the Tgstation.Server.Api.Models.User | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**id** | **int** | The ID of the Tgstation.Server.Api.Models.Internal.User | [optional] 
**enabled** | **bool** | If the Tgstation.Server.Api.Models.Internal.User is enabled since users cannot be deleted. System users cannot be disabled | [optional] 
**created_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.User was created | [optional] 
**system_identifier** | **str** | The SID/UID of the Tgstation.Server.Api.Models.Internal.User on Windows/POSIX respectively | [optional] 
**name** | **str** | The name of the Tgstation.Server.Api.Models.Internal.User | [optional] 
**administration_rights** | [**AdministrationRights**](AdministrationRights.md) |  | [optional] 
**instance_manager_rights** | [**InstanceManagerRights**](InstanceManagerRights.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

