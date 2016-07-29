# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TopLevelDomainCollection(Model):
    """Collection of Top Level Domains.

    :param value: Collection of resources
    :type value: list of :class:`TopLevelDomain
     <azure.mgmt.web.models.TopLevelDomain>`
    :param next_link: Link to next page of resources
    :type next_link: str
    """ 

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TopLevelDomain]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, next_link=None):
        self.value = value
        self.next_link = next_link