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


class SoftwareUpdateConfiguration(Model):
    """Software update configuration properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Resource name.
    :vartype name: str
    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource type
    :vartype type: str
    :param update_configuration: Required. update specific properties for the
     Software update configuration
    :type update_configuration:
     ~azure.mgmt.automation.models.UpdateConfiguration
    :param schedule_info: Required. Schedule information for the Software
     update configuration
    :type schedule_info: ~azure.mgmt.automation.models.ScheduleProperties
    :ivar provisioning_state: Provisioning state for the software update
     configuration, which only appears in the response.
    :vartype provisioning_state: str
    :param error: Details of provisioning error
    :type error: ~azure.mgmt.automation.models.ErrorResponse
    :ivar creation_time: Creation time of there source, which only appears in
     the response.
    :vartype creation_time: datetime
    :ivar created_by: CreatedBy property, which only appears in the response.
    :vartype created_by: str
    :ivar last_modified_time: Last time resource was modified, which only
     appears in the response.
    :vartype last_modified_time: datetime
    :ivar last_modified_by: LastModifiedBy property, which only appears in the
     response.
    :vartype last_modified_by: str
    :param tasks: Tasks information for the Software update configuration.
    :type tasks: ~azure.mgmt.automation.models.TasksProperties
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'update_configuration': {'required': True},
        'schedule_info': {'required': True},
        'provisioning_state': {'readonly': True},
        'creation_time': {'readonly': True},
        'created_by': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_modified_by': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'update_configuration': {'key': 'properties.updateConfiguration', 'type': 'UpdateConfiguration'},
        'schedule_info': {'key': 'properties.scheduleInfo', 'type': 'ScheduleProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'error': {'key': 'properties.error', 'type': 'ErrorResponse'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'created_by': {'key': 'properties.createdBy', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'tasks': {'key': 'properties.tasks', 'type': 'TasksProperties'},
    }

    def __init__(self, *, update_configuration, schedule_info, error=None, tasks=None, **kwargs) -> None:
        super(SoftwareUpdateConfiguration, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.update_configuration = update_configuration
        self.schedule_info = schedule_info
        self.provisioning_state = None
        self.error = error
        self.creation_time = None
        self.created_by = None
        self.last_modified_time = None
        self.last_modified_by = None
        self.tasks = tasks
