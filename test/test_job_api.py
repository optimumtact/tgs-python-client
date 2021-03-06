# coding: utf-8

"""
    TGS API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.job_api import JobApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = api.job_api.JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_job_controller_delete(self):
        """Test case for job_controller_delete

        Cancel a running Tgstation.Server.Api.Models.Job.  # noqa: E501
        """
        pass

    def test_job_controller_get_id(self):
        """Test case for job_controller_get_id

        Get a specific Tgstation.Server.Api.Models.Job.  # noqa: E501
        """
        pass

    def test_job_controller_list(self):
        """Test case for job_controller_list

        List all Tgstation.Server.Api.Models.JobTgstation.Server.Api.Models.EntityIds for the instance in reverse creation order.  # noqa: E501
        """
        pass

    def test_job_controller_read(self):
        """Test case for job_controller_read

        Get active Tgstation.Server.Api.Models.Jobs for the instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
