# DreamDaemon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_compile_job** | [**CompileJob**](CompileJob.md) |  | [optional] 
**staged_compile_job** | [**CompileJob**](CompileJob.md) |  | [optional] 
**running** | **bool** | The current status of Tgstation.Server.Api.Models.DreamDaemon | [optional] 
**current_security** | [**DreamDaemonSecurity**](DreamDaemonSecurity.md) |  | [optional] 
**current_port** | **int** | The port the running Tgstation.Server.Api.Models.DreamDaemon instance is set to | [optional] 
**current_allow_webclient** | **bool** | The webclient status the running Tgstation.Server.Api.Models.DreamDaemon instance is set to | [optional] 
**soft_restart** | **bool** | If the server is undergoing a soft reset. This may be automatically set by changes to other fields | [optional] 
**soft_shutdown** | **bool** | If the server is undergoing a soft shutdown | [optional] 
**auto_start** | **bool** | If Tgstation.Server.Api.Models.DreamDaemon starts when it&#x27;s Tgstation.Server.Api.Models.Instance starts | [optional] 
**allow_web_client** | **bool** | If the BYOND web client can be used to connect to the game server | [optional] 
**security_level** | [**DreamDaemonSecurity**](DreamDaemonSecurity.md) |  | [optional] 
**primary_port** | **int** | The first port Tgstation.Server.Api.Models.DreamDaemon uses. This should be the publically advertised port | [optional] 
**secondary_port** | **int** | The second port Tgstation.Server.Api.Models.DreamDaemon uses | [optional] 
**startup_timeout** | **int** | The DreamDaemon startup timeout in seconds | [optional] 
**heartbeat_seconds** | **int** | The number of seconds between each watchdog heartbeat. 0 disables. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

