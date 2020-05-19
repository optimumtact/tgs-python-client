# swagger_client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_controller_create**](UserApi.md#user_controller_create) | **PUT** /User | Create a Tgstation.Server.Api.Models.User.
[**user_controller_get_id**](UserApi.md#user_controller_get_id) | **GET** /User/{id} | Get a specific Tgstation.Server.Api.Models.User.
[**user_controller_list**](UserApi.md#user_controller_list) | **GET** /User/List | List all Tgstation.Server.Api.Models.Users in the server.
[**user_controller_read**](UserApi.md#user_controller_read) | **GET** /User | Get information about the current Tgstation.Server.Api.Models.User.
[**user_controller_update**](UserApi.md#user_controller_update) | **POST** /User | Update a Tgstation.Server.Api.Models.User.

# **user_controller_create**
> User user_controller_create(api, user_agent, body=body)

Create a Tgstation.Server.Api.Models.User.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.UserUpdate() # UserUpdate | The Tgstation.Server.Api.Models.User to create. (optional)

try:
    # Create a Tgstation.Server.Api.Models.User.
    api_response = api_instance.user_controller_create(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**UserUpdate**](UserUpdate.md)| The Tgstation.Server.Api.Models.User to create. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_controller_get_id**
> User user_controller_get_id(id, api, user_agent)

Get a specific Tgstation.Server.Api.Models.User.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.Internal.User.Id to retrieve.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get a specific Tgstation.Server.Api.Models.User.
    api_response = api_instance.user_controller_get_id(id, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.Internal.User.Id to retrieve. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**User**](User.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_controller_list**
> list[User] user_controller_list(api, user_agent)

List all Tgstation.Server.Api.Models.Users in the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # List all Tgstation.Server.Api.Models.Users in the server.
    api_response = api_instance.user_controller_list(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[User]**](User.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_controller_read**
> User user_controller_read(api, user_agent)

Get information about the current Tgstation.Server.Api.Models.User.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get information about the current Tgstation.Server.Api.Models.User.
    api_response = api_instance.user_controller_read(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**User**](User.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_controller_update**
> User user_controller_update(api, user_agent, body=body)

Update a Tgstation.Server.Api.Models.User.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.UserUpdate() # UserUpdate | The Tgstation.Server.Api.Models.User to update. (optional)

try:
    # Update a Tgstation.Server.Api.Models.User.
    api_response = api_instance.user_controller_update(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**UserUpdate**](UserUpdate.md)| The Tgstation.Server.Api.Models.User to update. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

