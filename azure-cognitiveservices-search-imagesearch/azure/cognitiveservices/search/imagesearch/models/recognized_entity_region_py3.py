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

from .response_py3 import Response


class RecognizedEntityRegion(Response):
    """Defines a region of the image where an entity was found and a list of
    entities that might match it.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar region: A region of the image that contains an entity. The values of
     the rectangle are relative to the width and height of the original image
     and are in the range 0.0 through 1.0. For example, if the image is 300x200
     and the region's top, left corner is at point (10, 20) and the bottom,
     right corner is at point (290, 150), then the normalized rectangle is:
     Left = 0.0333333333333333, Top = 0.1, Right = 0.9666666666666667, Bottom =
     0.75. For people, the region represents the person's face.
    :vartype region:
     ~azure.cognitiveservices.search.imagesearch.models.NormalizedRectangle
    :ivar matching_entities: A list of entities that Bing believes match the
     entity found in the region. The entities are in descending order of
     confidence (see the matchConfidence field of RecognizedEntity).
    :vartype matching_entities:
     list[~azure.cognitiveservices.search.imagesearch.models.RecognizedEntity]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'region': {'readonly': True},
        'matching_entities': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'region': {'key': 'region', 'type': 'NormalizedRectangle'},
        'matching_entities': {'key': 'matchingEntities', 'type': '[RecognizedEntity]'},
    }

    def __init__(self, **kwargs) -> None:
        super(RecognizedEntityRegion, self).__init__(**kwargs)
        self.region = None
        self.matching_entities = None
        self._type = 'RecognizedEntityRegion'
