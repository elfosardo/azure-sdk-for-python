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


class TaskProperties(Model):
    """task properties of the software update configuration.

    :param parameters: Gets or sets the parameters of the task.
    :type parameters: dict[str, str]
    :param source: Gets or sets the name of the runbook.
    :type source: str
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TaskProperties, self).__init__(**kwargs)
        self.parameters = kwargs.get('parameters', None)
        self.source = kwargs.get('source', None)
