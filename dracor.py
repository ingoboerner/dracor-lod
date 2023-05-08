"""General Stuff regarding DraCor goes here

"""
import logging
from marshmallow import Schema, fields, ValidationError

from crmcls import X1Corpus


class DraCor:
    """DraCor base class. Don't really know what to do with it at the moment.
    ()
    """
    def __init__(self):
        pass


"""
    {
    "licence": "CC0",
    "licenceUrl": "https://creativecommons.org/share-your-work/public-domain/cc0/",
    "description": "Edited by Frank Fischer and Peer Trilcke. Features more than 600 German-language plays ...",
    "title": "German Drama Corpus",
    "repository": "https://github.com/dracor-org/gerdracor",
    "name": "ger",
    "acronym": "GerDraCor"
    }
"""


class LicenceSchema(Schema):
    """Schema for the licence data"""
    # see D7.1, Feature C7 corpus_licence
    url = fields.Str()
    # see D7.1., Feature C8 corpus_licence_url
    label = fields.Str()


class DraCorCorpus(X1Corpus):
    """DraCor Corpus

    Attributes:
        id (str): ID; in the API this is the parameter "corpusname", e.g. ger
    """
    # Base URI
    __uri_base = "https://dracor.org/entity/"

    # ID of the corpus; will be key "name" in the response of /corpus/{corpusname}
    id = None

    def __init__(self,
                 id: str = None,
                 title: str = None,
                 licence: dict = None,
                 description: str = None,
                 repository_url: str = None):
        """

        Args:
            id (str): ID of the corpus [Feature C1 corpus_name]
            title (str, optional): Title of the corpus [Feature C3 corpus_title]
            licence (dict, optional): Licence information, should validate against LicenceSchema [Features C7, C8]
            description (str, optional): Description of the corpus [Feature C5 corpus_description]
            repository_url (str, optional): URL of the (GitHub) repository [Feature C6]
        """
        pass


