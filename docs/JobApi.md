# swagger_client.JobApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_controller_delete**](JobApi.md#job_controller_delete) | **DELETE** /Job/{id} | Cancel a running Tgstation.Server.Api.Models.Job.
[**job_controller_get_id**](JobApi.md#job_controller_get_id) | **GET** /Job/{id} | Get a specific Tgstation.Server.Api.Models.Job.
[**job_controller_list**](JobApi.md#job_controller_list) | **GET** /Job/List | List all Tgstation.Server.Api.Models.JobTgstation.Server.Api.Models.EntityIds for the instance in reverse creation order.
[**job_controller_read**](JobApi.md#job_controller_read) | **GET** /Job | Get active Tgstation.Server.Api.Models.Jobs for the instance.

# **job_controller_delete**
> Job job_controller_delete(id, api, user_agent)

Cancel a running Tgstation.Server.Api.Models.Job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Job to cancel.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Cancel a running Tgstation.Server.Api.Models.Job.
    api_response = api_instance.job_controller_delete(id, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Job to cancel. | 
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

# **job_controller_get_id**
> Job job_controller_get_id(id, api, user_agent)

Get a specific Tgstation.Server.Api.Models.Job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Job to retrieve.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get a specific Tgstation.Server.Api.Models.Job.
    api_response = api_instance.job_controller_get_id(id, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Job to retrieve. | 
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

# **job_controller_list**
> list[EntityId] job_controller_list(api, user_agent)

List all Tgstation.Server.Api.Models.JobTgstation.Server.Api.Models.EntityIds for the instance in reverse creation order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # List all Tgstation.Server.Api.Models.JobTgstation.Server.Api.Models.EntityIds for the instance in reverse creation order.
    api_response = api_instance.job_controller_list(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[EntityId]**](EntityId.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_controller_read**
> list[Job] job_controller_read(api, user_agent)

Get active Tgstation.Server.Api.Models.Jobs for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get active Tgstation.Server.Api.Models.Jobs for the instance.
    api_response = api_instance.job_controller_read(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[Job]**](Job.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

