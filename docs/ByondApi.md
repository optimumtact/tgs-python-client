# swagger_client.ByondApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**byond_controller_list**](ByondApi.md#byond_controller_list) | **GET** /Byond/List | Lists installed Tgstation.Server.Api.Models.Byond versions.
[**byond_controller_read**](ByondApi.md#byond_controller_read) | **GET** /Byond | Gets the active Tgstation.Server.Api.Models.Byond version.
[**byond_controller_update**](ByondApi.md#byond_controller_update) | **POST** /Byond | Changes the active BYOND version to the one specified in a given model.

# **byond_controller_list**
> list[Byond] byond_controller_list(instance, api, user_agent)

Lists installed Tgstation.Server.Api.Models.Byond versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Lists installed Tgstation.Server.Api.Models.Byond versions.
    api_response = api_instance.byond_controller_list(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[Byond]**](Byond.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **byond_controller_read**
> Byond byond_controller_read(instance, api, user_agent)

Gets the active Tgstation.Server.Api.Models.Byond version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Gets the active Tgstation.Server.Api.Models.Byond version.
    api_response = api_instance.byond_controller_read(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Byond**](Byond.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **byond_controller_update**
> Byond byond_controller_update(instance, api, user_agent, body=body)

Changes the active BYOND version to the one specified in a given model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Byond() # Byond | The Tgstation.Server.Api.Models.Byond.Version to switch to. (optional)

try:
    # Changes the active BYOND version to the one specified in a given model.
    api_response = api_instance.byond_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Byond**](Byond.md)| The Tgstation.Server.Api.Models.Byond.Version to switch to. | [optional] 

### Return type

[**Byond**](Byond.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

