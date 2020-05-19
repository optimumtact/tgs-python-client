# swagger_client.DreamDaemonApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dream_daemon_controller_create**](DreamDaemonApi.md#dream_daemon_controller_create) | **PUT** /DreamDaemon | Launches the watchdog.
[**dream_daemon_controller_delete**](DreamDaemonApi.md#dream_daemon_controller_delete) | **DELETE** /DreamDaemon | Stops the Watchdog if it&#x27;s running.
[**dream_daemon_controller_read**](DreamDaemonApi.md#dream_daemon_controller_read) | **GET** /DreamDaemon | Get the watchdog status.
[**dream_daemon_controller_restart**](DreamDaemonApi.md#dream_daemon_controller_restart) | **PATCH** /DreamDaemon | Creates a Tgstation.Server.Api.Models.Job to restart the Watchdog. It will start if it wasn&#x27;t already running.
[**dream_daemon_controller_update**](DreamDaemonApi.md#dream_daemon_controller_update) | **POST** /DreamDaemon | Update watchdog settings to be applied at next server reboot.

# **dream_daemon_controller_create**
> Job dream_daemon_controller_create(instance, api, user_agent)

Launches the watchdog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Launches the watchdog.
    api_response = api_instance.dream_daemon_controller_create(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Job**](Job.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_delete**
> dream_daemon_controller_delete(instance, api, user_agent)

Stops the Watchdog if it's running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Stops the Watchdog if it's running.
    api_instance.dream_daemon_controller_delete(instance, api, user_agent)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_read**
> DreamDaemon dream_daemon_controller_read(instance, api, user_agent)

Get the watchdog status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get the watchdog status.
    api_response = api_instance.dream_daemon_controller_read(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**DreamDaemon**](DreamDaemon.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_restart**
> Job dream_daemon_controller_restart(instance, api, user_agent)

Creates a Tgstation.Server.Api.Models.Job to restart the Watchdog. It will start if it wasn't already running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Creates a Tgstation.Server.Api.Models.Job to restart the Watchdog. It will start if it wasn't already running.
    api_response = api_instance.dream_daemon_controller_restart(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Job**](Job.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_update**
> DreamDaemon dream_daemon_controller_update(instance, api, user_agent, body=body)

Update watchdog settings to be applied at next server reboot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.DreamDaemon() # DreamDaemon | The updated Tgstation.Server.Api.Models.DreamDaemon settings. (optional)

try:
    # Update watchdog settings to be applied at next server reboot.
    api_response = api_instance.dream_daemon_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**DreamDaemon**](DreamDaemon.md)| The updated Tgstation.Server.Api.Models.DreamDaemon settings. | [optional] 

### Return type

[**DreamDaemon**](DreamDaemon.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

