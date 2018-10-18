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

from .resource import Resource


class IpFilterRule(Resource):
    """Single item in a List or Get IpFilterRules operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param ip_mask: IP Mask
    :type ip_mask: str
    :param action: The IP Filter Action. Possible values include: 'Accept',
     'Reject'
    :type action: str or ~azure.mgmt.servicebus.models.IPAction
    :param filter_name: IP Filter name
    :type filter_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'ip_mask': {'key': 'properties.ipMask', 'type': 'str'},
        'action': {'key': 'properties.action', 'type': 'str'},
        'filter_name': {'key': 'properties.filterName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IpFilterRule, self).__init__(**kwargs)
        self.ip_mask = kwargs.get('ip_mask', None)
        self.action = kwargs.get('action', None)
        self.filter_name = kwargs.get('filter_name', None)