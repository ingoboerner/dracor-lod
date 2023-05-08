"""Marshmallow Schemas of DraCor API response objects

Used current production version (v0.89.0).

"""
from marshmallow import Schema, fields


class InfoSchema(Schema):
    """Response object of the /info endpoint"""
    name = fields.Str()
    status = fields.Str()
    version = fields.Str()
    existdb = fields.Str()


"""
{

    "title": "German Drama Corpus",
    "repository": "https://github.com/dracor-org/gerdracor",
    "uri": "https://dracor.org/api/corpora/ger",
    "description": "Edited by Frank Fischer and Peer Trilcke. Features 501 German-language plays from the 1730s to the 1940s.",
    "licence": "CC0",
    "licenceUrl": "https://creativecommons.org/share-your-work/public-domain/cc0/",
    "metrics": {
      "characters": 10001,
      "female": 1308,
      "male": 3953,
      "plays": 471,
      "sp": 327696,
      "stage": 139169,
      "text": 471,
      "updated": "2019-01-12T00:55:59.145+01:00",
      "wordcount": {
        "sp": 7909927,
        "stage": 880356,
        "text": 8275863
      }
    }
  }
"""


class CorpusInCorporaSchema(Schema):
    """Single corpus object in the response of the /corpora endpoint"""
    # C1 corpus_name:
    name = fields.Str
    # C2 corpus_uri:
    uri = fields.Url
    # ...

