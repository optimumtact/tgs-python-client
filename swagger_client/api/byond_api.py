# coding: utf-8

"""
    TGS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ByondApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def byond_controller_list(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Lists installed Tgstation.Server.Api.Models.Byond versions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_list(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :return: list[Byond]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.byond_controller_list_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.byond_controller_list_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
            return data

    def byond_controller_list_with_http_info(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Lists installed Tgstation.Server.Api.Models.Byond versions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_list_with_http_info(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :return: list[Byond]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance', 'api', 'user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method byond_controller_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `byond_controller_list`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `byond_controller_list`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `byond_controller_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in params:
            header_params['instance'] = params['instance']  # noqa: E501
        if 'api' in params:
            header_params['api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Byond/List', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Byond]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def byond_controller_read(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Gets the active Tgstation.Server.Api.Models.Byond version.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_read(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :return: Byond
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.byond_controller_read_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.byond_controller_read_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
            return data

    def byond_controller_read_with_http_info(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Gets the active Tgstation.Server.Api.Models.Byond version.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_read_with_http_info(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :return: Byond
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance', 'api', 'user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method byond_controller_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `byond_controller_read`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `byond_controller_read`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `byond_controller_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in params:
            header_params['instance'] = params['instance']  # noqa: E501
        if 'api' in params:
            header_params['api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Byond', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Byond',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def byond_controller_update(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Changes the active BYOND version to the one specified in a given model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_update(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Byond body: The Tgstation.Server.Api.Models.Byond.Version to switch to.
        :return: Byond
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.byond_controller_update_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.byond_controller_update_with_http_info(instance, api, user_agent, **kwargs)  # noqa: E501
            return data

    def byond_controller_update_with_http_info(self, instance, api, user_agent, **kwargs):  # noqa: E501
        """Changes the active BYOND version to the one specified in a given model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.byond_controller_update_with_http_info(instance, api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int instance: The instance ID being accessed (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Byond body: The Tgstation.Server.Api.Models.Byond.Version to switch to.
        :return: Byond
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance', 'api', 'user_agent', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method byond_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `byond_controller_update`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `byond_controller_update`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `byond_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance' in params:
            header_params['instance'] = params['instance']  # noqa: E501
        if 'api' in params:
            header_params['api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Byond', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Byond',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
