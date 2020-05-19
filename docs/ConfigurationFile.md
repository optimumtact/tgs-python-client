# ConfigurationFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the Tgstation.Server.Api.Models.ConfigurationFile file | [optional] 
**access_denied** | **bool** | If access to the Tgstation.Server.Api.Models.ConfigurationFile file was denied for the operation | [optional] 
**is_directory** | **bool** | If Tgstation.Server.Api.Models.ConfigurationFile.Path represents a directory | [optional] 
**last_read_hash** | **str** | The MD5 hash of the file when last read by the user. If this doesn&#x27;t match during update actions, the write will be denied with System.Net.HttpStatusCode.Conflict | [optional] 
**content** | **str** | The content of the Tgstation.Server.Api.Models.ConfigurationFile. Will be &lt;see langword&#x3D;\&quot;null\&quot; /&gt; if Tgstation.Server.Api.Models.ConfigurationFile.AccessDenied is &lt;see langword&#x3D;\&quot;true\&quot; /&gt; or during listing and write operations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

