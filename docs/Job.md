# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_by** | [**User**](User.md) |  | [optional] 
**cancelled_by** | [**User**](User.md) |  | [optional] 
**progress** | **int** | Optional progress between 0 and 100 inclusive | [optional] 
**description** | **str** | English description of the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**error_code** | [**ErrorCode**](ErrorCode.md) |  | [optional] 
**exception_details** | **str** | Details of any exceptions caught during the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**started_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.Job was started | [optional] 
**stopped_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.Job stopped | [optional] 
**cancelled** | **bool** | If the Tgstation.Server.Api.Models.Internal.Job was cancelled | [optional] 
**cancel_rights_type** | [**RightsType**](RightsType.md) |  | [optional] 
**cancel_right** | **int** | The N:Tgstation.Server.Api.Rights required to cancel the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

