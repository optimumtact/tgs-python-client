# coding: utf-8

"""
    TGS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ConfigurationFile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path': 'str',
        'access_denied': 'bool',
        'is_directory': 'bool',
        'last_read_hash': 'str',
        'content': 'str'
    }

    attribute_map = {
        'path': 'path',
        'access_denied': 'accessDenied',
        'is_directory': 'isDirectory',
        'last_read_hash': 'lastReadHash',
        'content': 'content'
    }

    def __init__(self, path=None, access_denied=None, is_directory=None, last_read_hash=None, content=None):  # noqa: E501
        """ConfigurationFile - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._access_denied = None
        self._is_directory = None
        self._last_read_hash = None
        self._content = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if access_denied is not None:
            self.access_denied = access_denied
        if is_directory is not None:
            self.is_directory = is_directory
        if last_read_hash is not None:
            self.last_read_hash = last_read_hash
        if content is not None:
            self.content = content

    @property
    def path(self):
        """Gets the path of this ConfigurationFile.  # noqa: E501

        The path to the Tgstation.Server.Api.Models.ConfigurationFile file  # noqa: E501

        :return: The path of this ConfigurationFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ConfigurationFile.

        The path to the Tgstation.Server.Api.Models.ConfigurationFile file  # noqa: E501

        :param path: The path of this ConfigurationFile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def access_denied(self):
        """Gets the access_denied of this ConfigurationFile.  # noqa: E501

        If access to the Tgstation.Server.Api.Models.ConfigurationFile file was denied for the operation  # noqa: E501

        :return: The access_denied of this ConfigurationFile.  # noqa: E501
        :rtype: bool
        """
        return self._access_denied

    @access_denied.setter
    def access_denied(self, access_denied):
        """Sets the access_denied of this ConfigurationFile.

        If access to the Tgstation.Server.Api.Models.ConfigurationFile file was denied for the operation  # noqa: E501

        :param access_denied: The access_denied of this ConfigurationFile.  # noqa: E501
        :type: bool
        """

        self._access_denied = access_denied

    @property
    def is_directory(self):
        """Gets the is_directory of this ConfigurationFile.  # noqa: E501

        If Tgstation.Server.Api.Models.ConfigurationFile.Path represents a directory  # noqa: E501

        :return: The is_directory of this ConfigurationFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_directory

    @is_directory.setter
    def is_directory(self, is_directory):
        """Sets the is_directory of this ConfigurationFile.

        If Tgstation.Server.Api.Models.ConfigurationFile.Path represents a directory  # noqa: E501

        :param is_directory: The is_directory of this ConfigurationFile.  # noqa: E501
        :type: bool
        """

        self._is_directory = is_directory

    @property
    def last_read_hash(self):
        """Gets the last_read_hash of this ConfigurationFile.  # noqa: E501

        The MD5 hash of the file when last read by the user. If this doesn't match during update actions, the write will be denied with System.Net.HttpStatusCode.Conflict  # noqa: E501

        :return: The last_read_hash of this ConfigurationFile.  # noqa: E501
        :rtype: str
        """
        return self._last_read_hash

    @last_read_hash.setter
    def last_read_hash(self, last_read_hash):
        """Sets the last_read_hash of this ConfigurationFile.

        The MD5 hash of the file when last read by the user. If this doesn't match during update actions, the write will be denied with System.Net.HttpStatusCode.Conflict  # noqa: E501

        :param last_read_hash: The last_read_hash of this ConfigurationFile.  # noqa: E501
        :type: str
        """

        self._last_read_hash = last_read_hash

    @property
    def content(self):
        """Gets the content of this ConfigurationFile.  # noqa: E501

        The content of the Tgstation.Server.Api.Models.ConfigurationFile. Will be <see langword=\"null\" /> if Tgstation.Server.Api.Models.ConfigurationFile.AccessDenied is <see langword=\"true\" /> or during listing and write operations  # noqa: E501

        :return: The content of this ConfigurationFile.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ConfigurationFile.

        The content of the Tgstation.Server.Api.Models.ConfigurationFile. Will be <see langword=\"null\" /> if Tgstation.Server.Api.Models.ConfigurationFile.AccessDenied is <see langword=\"true\" /> or during listing and write operations  # noqa: E501

        :param content: The content of this ConfigurationFile.  # noqa: E501
        :type: str
        """

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConfigurationFile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
