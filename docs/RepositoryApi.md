# swagger_client.RepositoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_controller_create**](RepositoryApi.md#repository_controller_create) | **PUT** /Repository | Begin cloning the repository if it doesn&#x27;t exist.
[**repository_controller_delete**](RepositoryApi.md#repository_controller_delete) | **DELETE** /Repository | Delete the Tgstation.Server.Api.Models.Repository.
[**repository_controller_read**](RepositoryApi.md#repository_controller_read) | **GET** /Repository | Get Tgstation.Server.Api.Models.Repository status.
[**repository_controller_update**](RepositoryApi.md#repository_controller_update) | **POST** /Repository | Perform updats to the Tgstation.Server.Api.Models.Repository.

# **repository_controller_create**
> Repository repository_controller_create(instance, api, user_agent, body=body)

Begin cloning the repository if it doesn't exist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Repository() # Repository | Initial Tgstation.Server.Api.Models.Repository settings. (optional)

try:
    # Begin cloning the repository if it doesn't exist.
    api_response = api_instance.repository_controller_create(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Repository**](Repository.md)| Initial Tgstation.Server.Api.Models.Repository settings. | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_delete**
> Repository repository_controller_delete(instance, api, user_agent)

Delete the Tgstation.Server.Api.Models.Repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Delete the Tgstation.Server.Api.Models.Repository.
    api_response = api_instance.repository_controller_delete(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_read**
> Repository repository_controller_read(instance, api, user_agent)

Get Tgstation.Server.Api.Models.Repository status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get Tgstation.Server.Api.Models.Repository status.
    api_response = api_instance.repository_controller_read(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_update**
> Repository repository_controller_update(instance, api, user_agent, body=body)

Perform updats to the Tgstation.Server.Api.Models.Repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Repository() # Repository | The updated Tgstation.Server.Api.Models.Repository. (optional)

try:
    # Perform updats to the Tgstation.Server.Api.Models.Repository.
    api_response = api_instance.repository_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Repository**](Repository.md)| The updated Tgstation.Server.Api.Models.Repository. | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

