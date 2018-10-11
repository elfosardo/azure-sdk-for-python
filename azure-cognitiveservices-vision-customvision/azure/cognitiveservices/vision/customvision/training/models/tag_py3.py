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


class Tag(Model):
    """Represents a Tag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the Tag ID
    :vartype id: str
    :param name: Gets or sets the name of the tag
    :type name: str
    :param description: Gets or sets the description of the tag
    :type description: str
    :param type: Gets or sets the type of the tag. Possible values include:
     'Regular', 'Negative'
    :type type: str or
     ~azure.cognitiveservices.vision.customvision.training.models.TagType
    :ivar image_count: Gets the number of images with this tag
    :vartype image_count: int
    """

    _validation = {
        'id': {'readonly': True},
        'image_count': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'image_count': {'key': 'imageCount', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, description: str=None, type=None, **kwargs) -> None:
        super(Tag, self).__init__(**kwargs)
        self.id = None
        self.name = name
        self.description = description
        self.type = type
        self.image_count = None
