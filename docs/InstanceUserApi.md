# swagger_client.InstanceUserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_user_controller_create**](InstanceUserApi.md#instance_user_controller_create) | **PUT** /InstanceUser | Create am Tgstation.Server.Api.Models.InstanceUser.
[**instance_user_controller_delete**](InstanceUserApi.md#instance_user_controller_delete) | **DELETE** /InstanceUser/{id} | Delete an Tgstation.Server.Api.Models.InstanceUser.
[**instance_user_controller_get_id**](InstanceUserApi.md#instance_user_controller_get_id) | **GET** /InstanceUser/{id} | Gets a specific Tgstation.Server.Api.Models.InstanceUser.
[**instance_user_controller_list**](InstanceUserApi.md#instance_user_controller_list) | **GET** /InstanceUser/List | Lists Tgstation.Server.Api.Models.InstanceUsers for the instance.
[**instance_user_controller_read**](InstanceUserApi.md#instance_user_controller_read) | **GET** /InstanceUser | Read the active Tgstation.Server.Api.Models.InstanceUser.
[**instance_user_controller_update**](InstanceUserApi.md#instance_user_controller_update) | **POST** /InstanceUser | Update the permissions for an Tgstation.Server.Api.Models.InstanceUser.

# **instance_user_controller_create**
> InstanceUser instance_user_controller_create(instance, api, user_agent, body=body)

Create am Tgstation.Server.Api.Models.InstanceUser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.InstanceUser() # InstanceUser | The Tgstation.Server.Api.Models.InstanceUser to create. (optional)

try:
    # Create am Tgstation.Server.Api.Models.InstanceUser.
    api_response = api_instance.instance_user_controller_create(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**InstanceUser**](InstanceUser.md)| The Tgstation.Server.Api.Models.InstanceUser to create. | [optional] 

### Return type

[**InstanceUser**](InstanceUser.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_user_controller_delete**
> instance_user_controller_delete(id, instance, api, user_agent)

Delete an Tgstation.Server.Api.Models.InstanceUser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.InstanceUser.UserId to delete.
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Delete an Tgstation.Server.Api.Models.InstanceUser.
    api_instance.instance_user_controller_delete(id, instance, api, user_agent)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.InstanceUser.UserId to delete. | 
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

# **instance_user_controller_get_id**
> InstanceUser instance_user_controller_get_id(id, instance, api, user_agent)

Gets a specific Tgstation.Server.Api.Models.InstanceUser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.InstanceUser.UserId.
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Gets a specific Tgstation.Server.Api.Models.InstanceUser.
    api_response = api_instance.instance_user_controller_get_id(id, instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.InstanceUser.UserId. | 
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**InstanceUser**](InstanceUser.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_user_controller_list**
> list[InstanceUser] instance_user_controller_list(instance, api, user_agent)

Lists Tgstation.Server.Api.Models.InstanceUsers for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Lists Tgstation.Server.Api.Models.InstanceUsers for the instance.
    api_response = api_instance.instance_user_controller_list(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[InstanceUser]**](InstanceUser.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_user_controller_read**
> InstanceUser instance_user_controller_read(api, user_agent)

Read the active Tgstation.Server.Api.Models.InstanceUser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Read the active Tgstation.Server.Api.Models.InstanceUser.
    api_response = api_instance.instance_user_controller_read(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**InstanceUser**](InstanceUser.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_user_controller_update**
> InstanceUser instance_user_controller_update(instance, api, user_agent, body=body)

Update the permissions for an Tgstation.Server.Api.Models.InstanceUser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstanceUserApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.InstanceUser() # InstanceUser | The updated Tgstation.Server.Api.Models.InstanceUser. (optional)

try:
    # Update the permissions for an Tgstation.Server.Api.Models.InstanceUser.
    api_response = api_instance.instance_user_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceUserApi->instance_user_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**InstanceUser**](InstanceUser.md)| The updated Tgstation.Server.Api.Models.InstanceUser. | [optional] 

### Return type

[**InstanceUser**](InstanceUser.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

