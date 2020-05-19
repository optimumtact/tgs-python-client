# swagger_client.DreamMakerApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dream_maker_controller_create**](DreamMakerApi.md#dream_maker_controller_create) | **PUT** /DreamMaker | Begin deploying repository code.
[**dream_maker_controller_get_id**](DreamMakerApi.md#dream_maker_controller_get_id) | **GET** /DreamMaker/{id} | Get a Tgstation.Server.Api.Models.CompileJob specified by a given id.
[**dream_maker_controller_list**](DreamMakerApi.md#dream_maker_controller_list) | **GET** /DreamMaker/List | List all Tgstation.Server.Api.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.
[**dream_maker_controller_read**](DreamMakerApi.md#dream_maker_controller_read) | **GET** /DreamMaker | Read current Tgstation.Server.Api.Models.DreamMaker status.
[**dream_maker_controller_update**](DreamMakerApi.md#dream_maker_controller_update) | **POST** /DreamMaker | Update deployment settings.

# **dream_maker_controller_create**
> Job dream_maker_controller_create(instance, api, user_agent)

Begin deploying repository code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Begin deploying repository code.
    api_response = api_instance.dream_maker_controller_create(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_create: %s\n" % e)
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

# **dream_maker_controller_get_id**
> CompileJob dream_maker_controller_get_id(id, instance, api, user_agent)

Get a Tgstation.Server.Api.Models.CompileJob specified by a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id.
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get a Tgstation.Server.Api.Models.CompileJob specified by a given id.
    api_response = api_instance.dream_maker_controller_get_id(id, instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id. | 
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**CompileJob**](CompileJob.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_maker_controller_list**
> list[EntityId] dream_maker_controller_list(instance, api, user_agent)

List all Tgstation.Server.Api.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # List all Tgstation.Server.Api.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.
    api_response = api_instance.dream_maker_controller_list(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
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

# **dream_maker_controller_read**
> DreamMaker dream_maker_controller_read(instance, api, user_agent)

Read current Tgstation.Server.Api.Models.DreamMaker status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Read current Tgstation.Server.Api.Models.DreamMaker status.
    api_response = api_instance.dream_maker_controller_read(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**DreamMaker**](DreamMaker.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_maker_controller_update**
> DreamMaker dream_maker_controller_update(instance, api, user_agent, body=body)

Update deployment settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.DreamMaker() # DreamMaker | The updated Tgstation.Server.Api.Models.DreamMaker settings. (optional)

try:
    # Update deployment settings.
    api_response = api_instance.dream_maker_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**DreamMaker**](DreamMaker.md)| The updated Tgstation.Server.Api.Models.DreamMaker settings. | [optional] 

### Return type

[**DreamMaker**](DreamMaker.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

