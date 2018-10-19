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


class SoftareUpdateConfigurationRunTasks(Model):
    """Software update configuration run tasks model.

    :param pre_task: Pre task object
    :type pre_task:
     ~azure.mgmt.automation.models.SoftareUpdateConfigurationRunTaskProperties
    :param post_task: Post task object
    :type post_task:
     ~azure.mgmt.automation.models.SoftareUpdateConfigurationRunTaskProperties
    """

    _attribute_map = {
        'pre_task': {'key': 'preTask', 'type': 'SoftareUpdateConfigurationRunTaskProperties'},
        'post_task': {'key': 'postTask', 'type': 'SoftareUpdateConfigurationRunTaskProperties'},
    }

    def __init__(self, *, pre_task=None, post_task=None, **kwargs) -> None:
        super(SoftareUpdateConfigurationRunTasks, self).__init__(**kwargs)
        self.pre_task = pre_task
        self.post_task = post_task
