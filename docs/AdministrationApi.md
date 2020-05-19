# swagger_client.AdministrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**administration_controller_delete**](AdministrationApi.md#administration_controller_delete) | **DELETE** /Administration | Attempts to restart the server.
[**administration_controller_read**](AdministrationApi.md#administration_controller_read) | **GET** /Administration | Get Tgstation.Server.Api.Models.Administration server information.
[**administration_controller_update**](AdministrationApi.md#administration_controller_update) | **POST** /Administration | Attempt to perform a server upgrade.

# **administration_controller_delete**
> administration_controller_delete(api, user_agent)

Attempts to restart the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Attempts to restart the server.
    api_instance.administration_controller_delete(api, user_agent)
except ApiException as e:
    print("Exception when calling AdministrationApi->administration_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **administration_controller_read**
> Administration administration_controller_read(api, user_agent)

Get Tgstation.Server.Api.Models.Administration server information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get Tgstation.Server.Api.Models.Administration server information.
    api_response = api_instance.administration_controller_read(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->administration_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Administration**](Administration.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **administration_controller_update**
> Administration administration_controller_update(api, user_agent, body=body)

Attempt to perform a server upgrade.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Administration() # Administration | The model containing the Tgstation.Server.Api.Models.Administration.NewVersion to update to. (optional)

try:
    # Attempt to perform a server upgrade.
    api_response = api_instance.administration_controller_update(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->administration_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Administration**](Administration.md)| The model containing the Tgstation.Server.Api.Models.Administration.NewVersion to update to. | [optional] 

### Return type

[**Administration**](Administration.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

