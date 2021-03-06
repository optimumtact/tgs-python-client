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


class ChatBot(object):
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
        'channels': 'list[ChatChannel]',
        'id': 'int',
        'name': 'str',
        'enabled': 'bool',
        'reconnection_interval': 'int',
        'channel_limit': 'int',
        'provider': 'ChatProvider',
        'connection_string': 'str'
    }

    attribute_map = {
        'channels': 'channels',
        'id': 'id',
        'name': 'name',
        'enabled': 'enabled',
        'reconnection_interval': 'reconnectionInterval',
        'channel_limit': 'channelLimit',
        'provider': 'provider',
        'connection_string': 'connectionString'
    }

    def __init__(self, channels=None, id=None, name=None, enabled=None, reconnection_interval=None, channel_limit=None, provider=None, connection_string=None):  # noqa: E501
        """ChatBot - a model defined in Swagger"""  # noqa: E501
        self._channels = None
        self._id = None
        self._name = None
        self._enabled = None
        self._reconnection_interval = None
        self._channel_limit = None
        self._provider = None
        self._connection_string = None
        self.discriminator = None
        if channels is not None:
            self.channels = channels
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if reconnection_interval is not None:
            self.reconnection_interval = reconnection_interval
        if channel_limit is not None:
            self.channel_limit = channel_limit
        if provider is not None:
            self.provider = provider
        if connection_string is not None:
            self.connection_string = connection_string

    @property
    def channels(self):
        """Gets the channels of this ChatBot.  # noqa: E501

        Channels the Discord bot should listen/announce in  # noqa: E501

        :return: The channels of this ChatBot.  # noqa: E501
        :rtype: list[ChatChannel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ChatBot.

        Channels the Discord bot should listen/announce in  # noqa: E501

        :param channels: The channels of this ChatBot.  # noqa: E501
        :type: list[ChatChannel]
        """

        self._channels = channels

    @property
    def id(self):
        """Gets the id of this ChatBot.  # noqa: E501

        The settings id  # noqa: E501

        :return: The id of this ChatBot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChatBot.

        The settings id  # noqa: E501

        :param id: The id of this ChatBot.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ChatBot.  # noqa: E501

        The name of the connection  # noqa: E501

        :return: The name of this ChatBot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChatBot.

        The name of the connection  # noqa: E501

        :param name: The name of this ChatBot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this ChatBot.  # noqa: E501

        If the connection is enabled  # noqa: E501

        :return: The enabled of this ChatBot.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ChatBot.

        If the connection is enabled  # noqa: E501

        :param enabled: The enabled of this ChatBot.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def reconnection_interval(self):
        """Gets the reconnection_interval of this ChatBot.  # noqa: E501

        The time interval in minutes the chat bot attempts to reconnect if Tgstation.Server.Api.Models.Internal.ChatBot.Enabled and disconnected. Must not be zero.  # noqa: E501

        :return: The reconnection_interval of this ChatBot.  # noqa: E501
        :rtype: int
        """
        return self._reconnection_interval

    @reconnection_interval.setter
    def reconnection_interval(self, reconnection_interval):
        """Sets the reconnection_interval of this ChatBot.

        The time interval in minutes the chat bot attempts to reconnect if Tgstation.Server.Api.Models.Internal.ChatBot.Enabled and disconnected. Must not be zero.  # noqa: E501

        :param reconnection_interval: The reconnection_interval of this ChatBot.  # noqa: E501
        :type: int
        """

        self._reconnection_interval = reconnection_interval

    @property
    def channel_limit(self):
        """Gets the channel_limit of this ChatBot.  # noqa: E501

        The maximum number of Tgstation.Server.Api.Models.ChatChannels the Tgstation.Server.Api.Models.Internal.ChatBot may contain.  # noqa: E501

        :return: The channel_limit of this ChatBot.  # noqa: E501
        :rtype: int
        """
        return self._channel_limit

    @channel_limit.setter
    def channel_limit(self, channel_limit):
        """Sets the channel_limit of this ChatBot.

        The maximum number of Tgstation.Server.Api.Models.ChatChannels the Tgstation.Server.Api.Models.Internal.ChatBot may contain.  # noqa: E501

        :param channel_limit: The channel_limit of this ChatBot.  # noqa: E501
        :type: int
        """

        self._channel_limit = channel_limit

    @property
    def provider(self):
        """Gets the provider of this ChatBot.  # noqa: E501


        :return: The provider of this ChatBot.  # noqa: E501
        :rtype: ChatProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ChatBot.


        :param provider: The provider of this ChatBot.  # noqa: E501
        :type: ChatProvider
        """

        self._provider = provider

    @property
    def connection_string(self):
        """Gets the connection_string of this ChatBot.  # noqa: E501

        The information used to connect to the Tgstation.Server.Api.Models.Internal.ChatBot.Provider  # noqa: E501

        :return: The connection_string of this ChatBot.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this ChatBot.

        The information used to connect to the Tgstation.Server.Api.Models.Internal.ChatBot.Provider  # noqa: E501

        :param connection_string: The connection_string of this ChatBot.  # noqa: E501
        :type: str
        """

        self._connection_string = connection_string

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
        if issubclass(ChatBot, dict):
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
        if not isinstance(other, ChatBot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
