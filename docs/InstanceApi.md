# swagger_client.InstanceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_controller_create**](InstanceApi.md#instance_controller_create) | **PUT** /Instance | Create or attach an Tgstation.Server.Api.Models.Instance.
[**instance_controller_delete**](InstanceApi.md#instance_controller_delete) | **DELETE** /Instance/{id} | Detach an Tgstation.Server.Api.Models.Instance with the given id.
[**instance_controller_get_id**](InstanceApi.md#instance_controller_get_id) | **GET** /Instance/{id} | Get a specific Tgstation.Server.Api.Models.Instance.
[**instance_controller_list**](InstanceApi.md#instance_controller_list) | **GET** /Instance/List | List Tgstation.Server.Api.Models.Instances.
[**instance_controller_update**](InstanceApi.md#instance_controller_update) | **POST** /Instance | Modify an Tgstation.Server.Api.Models.Instance&#x27;s settings.

# **instance_controller_create**
> Instance instance_controller_create(api, user_agent, body=body)

Create or attach an Tgstation.Server.Api.Models.Instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Instance() # Instance | The Tgstation.Server.Api.Models.Instance settings. (optional)

try:
    # Create or attach an Tgstation.Server.Api.Models.Instance.
    api_response = api_instance.instance_controller_create(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->instance_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Instance**](Instance.md)| The Tgstation.Server.Api.Models.Instance settings. | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_delete**
> instance_controller_delete(id, api, user_agent)

Detach an Tgstation.Server.Api.Models.Instance with the given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.Instance.Id to detach.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Detach an Tgstation.Server.Api.Models.Instance with the given id.
    api_instance.instance_controller_delete(id, api, user_agent)
except ApiException as e:
    print("Exception when calling InstanceApi->instance_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.Instance.Id to detach. | 
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

# **instance_controller_get_id**
> Instance instance_controller_get_id(id, api, user_agent)

Get a specific Tgstation.Server.Api.Models.Instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.Instance.Id to retrieve.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get a specific Tgstation.Server.Api.Models.Instance.
    api_response = api_instance.instance_controller_get_id(id, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->instance_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.Instance.Id to retrieve. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_list**
> list[Instance] instance_controller_list(api, user_agent)

List Tgstation.Server.Api.Models.Instances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # List Tgstation.Server.Api.Models.Instances.
    api_response = api_instance.instance_controller_list(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->instance_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[Instance]**](Instance.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_controller_update**
> Instance instance_controller_update(api, user_agent, body=body)

Modify an Tgstation.Server.Api.Models.Instance's settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Instance() # Instance | The updated Tgstation.Server.Api.Models.Instance settings. (optional)

try:
    # Modify an Tgstation.Server.Api.Models.Instance's settings.
    api_response = api_instance.instance_controller_update(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceApi->instance_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Instance**](Instance.md)| The updated Tgstation.Server.Api.Models.Instance settings. | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

