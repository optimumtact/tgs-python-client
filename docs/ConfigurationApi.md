# swagger_client.ConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_controller_create**](ConfigurationApi.md#configuration_controller_create) | **PUT** /Config | Create a configuration directory.
[**configuration_controller_delete**](ConfigurationApi.md#configuration_controller_delete) | **DELETE** /Config | Deletes an empty directory
[**configuration_controller_directory**](ConfigurationApi.md#configuration_controller_directory) | **GET** /Config/List/{directoryPath} | Get the contents of a directory at a directoryPath
[**configuration_controller_file**](ConfigurationApi.md#configuration_controller_file) | **GET** /Config/File/{filePath} | Get the contents of a file at a filePath
[**configuration_controller_list**](ConfigurationApi.md#configuration_controller_list) | **GET** /Config/List | Get the contents of the root configuration directory.
[**configuration_controller_update**](ConfigurationApi.md#configuration_controller_update) | **POST** /Config | Write to a configuration file.

# **configuration_controller_create**
> ConfigurationFile configuration_controller_create(instance, api, user_agent, body=body)

Create a configuration directory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.ConfigurationFile() # ConfigurationFile | The Tgstation.Server.Api.Models.ConfigurationFile representing the directory. (optional)

try:
    # Create a configuration directory.
    api_response = api_instance.configuration_controller_create(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**ConfigurationFile**](ConfigurationFile.md)| The Tgstation.Server.Api.Models.ConfigurationFile representing the directory. | [optional] 

### Return type

[**ConfigurationFile**](ConfigurationFile.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_delete**
> configuration_controller_delete(instance, api, user_agent, body=body)

Deletes an empty directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.ConfigurationFile() # ConfigurationFile | A Tgstation.Server.Api.Models.ConfigurationFile representing the path to the directory to delete (optional)

try:
    # Deletes an empty directory
    api_instance.configuration_controller_delete(instance, api, user_agent, body=body)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**ConfigurationFile**](ConfigurationFile.md)| A Tgstation.Server.Api.Models.ConfigurationFile representing the path to the directory to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_directory**
> list[ConfigurationFile] configuration_controller_directory(directory_path, instance, api, user_agent)

Get the contents of a directory at a directoryPath

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
directory_path = 'directory_path_example' # str | The path of the directory to get
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get the contents of a directory at a directoryPath
    api_response = api_instance.configuration_controller_directory(directory_path, instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| The path of the directory to get | 
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[ConfigurationFile]**](ConfigurationFile.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_file**
> ConfigurationFile configuration_controller_file(file_path, instance, api, user_agent)

Get the contents of a file at a filePath

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
file_path = 'file_path_example' # str | The path of the file to get
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get the contents of a file at a filePath
    api_response = api_instance.configuration_controller_file(file_path, instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| The path of the file to get | 
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**ConfigurationFile**](ConfigurationFile.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_list**
> list[ConfigurationFile] configuration_controller_list(instance, api, user_agent)

Get the contents of the root configuration directory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Get the contents of the root configuration directory.
    api_response = api_instance.configuration_controller_list(instance, api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**list[ConfigurationFile]**](ConfigurationFile.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_update**
> ConfigurationFile configuration_controller_update(instance, api, user_agent, body=body)

Write to a configuration file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
instance = 56 # int | The instance ID being accessed
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.ConfigurationFile() # ConfigurationFile | The Tgstation.Server.Api.Models.ConfigurationFile representing the file. (optional)

try:
    # Write to a configuration file.
    api_response = api_instance.configuration_controller_update(instance, api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **int**| The instance ID being accessed | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**ConfigurationFile**](ConfigurationFile.md)| The Tgstation.Server.Api.Models.ConfigurationFile representing the file. | [optional] 

### Return type

[**ConfigurationFile**](ConfigurationFile.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

