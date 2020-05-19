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


class Byond(object):
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
        'version': 'str',
        'install_job': 'Job'
    }

    attribute_map = {
        'version': 'version',
        'install_job': 'installJob'
    }

    def __init__(self, version=None, install_job=None):  # noqa: E501
        """Byond - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._install_job = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if install_job is not None:
            self.install_job = install_job

    @property
    def version(self):
        """Gets the version of this Byond.  # noqa: E501

        The System.Version of the Tgstation.Server.Api.Models.Byond installation used for new compiles. Will be <see langword=\"null\" /> if the user does not have permission to view it or there is no BYOND version installed. Only considers the System.Version.Major and System.Version.Minor numbers.  # noqa: E501

        :return: The version of this Byond.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Byond.

        The System.Version of the Tgstation.Server.Api.Models.Byond installation used for new compiles. Will be <see langword=\"null\" /> if the user does not have permission to view it or there is no BYOND version installed. Only considers the System.Version.Major and System.Version.Minor numbers.  # noqa: E501

        :param version: The version of this Byond.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def install_job(self):
        """Gets the install_job of this Byond.  # noqa: E501


        :return: The install_job of this Byond.  # noqa: E501
        :rtype: Job
        """
        return self._install_job

    @install_job.setter
    def install_job(self, install_job):
        """Sets the install_job of this Byond.


        :param install_job: The install_job of this Byond.  # noqa: E501
        :type: Job
        """

        self._install_job = install_job

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
        if issubclass(Byond, dict):
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
        if not isinstance(other, Byond):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other