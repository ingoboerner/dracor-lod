"""Ontologies module

Stuff that is connected to handling ontologies.
The functionality has been implemented to the DraCor class. I moved it.
"""
import logging

try:
    from cidoc import NAMESPACE as CIDOCNAMESPACE
except ImportError:
    CIDOCNAMESPACE = "http://www.cidoc-crm.org/cidoc-crm/"

try:
    from lrmoo import LRMNAMESPACE
except ImportError:
    LRMNAMESPACE = "http://www.cidoc-crm.org/cidoc-crm/lrmoo/"

try:
    from crmdig import NAMESPACE as DIGNAMESPACE
except ImportError:
    DIGNAMESPACE = "http://www.ics.forth.gr/isl/CRMdig/"

try:
    from pem import NAMESPACE as PEMNAMESPACE
except ImportError:
    PEMNAMESPACE = "http://parthenos.d4science.org/CRMext/CRMpe.rdfs#"

try:
    from crmcls import NAMESPACE as CLSCORNAMESPACE
except ImportError:
    CLSCORNAMESPACE = "https://clscor.io/ontologies/CRMcls/"


class Ontologies:
    """Ontologies
    """

    __data = [
        {
            "prefix": "rdfs",
            "uri": "http://www.w3.org/2000/01/rdf-schema#"
        },
        {
            "prefix": "owl",
            "uri": "http://www.w3.org/2002/07/owl#"
        },
        {
            "prefix": "xsd",
            "uri": "http://www.w3.org/2001/XMLSchema#"
        },
        {
            "prefix": "crm",
            "uri": CIDOCNAMESPACE,
            "version": "v7.1.2"
        },
        {
            "prefix": "cls",
            "uri": CLSCORNAMESPACE
        },
        {
            "prefix": "lrm",
            "uri": LRMNAMESPACE,
            "version": "v0.9"
        },
        {
            "prefix": "pem",
            "uri": PEMNAMESPACE
        },
        {
            "prefix": "dig",
            "uri": DIGNAMESPACE
        }
    ]

    def __init__(self):
        pass

    def get_prefix_uri(self, prefix: str) -> str:
        """Get the uri for a prefix form self.__data

        Args:
            prefix (str): Prefix to get URI for

        Returns:
            str: URI
        """
        assert self.__data

        try:
            uri = list(filter(lambda item: prefix in item["prefix"], self.__data))[0]["uri"]
        except IndexError:
            logging.warning(f"Prefix '{prefix}' is not defined.")
            uri = None

        return uri

    def get_prefixes_uris(self) -> list:
        """Get prefix and corresponding URI

        Returns:
            list: List containing dictionaries with "prefix", "uri"
        """
        prefix_uris = list()
        for item in self.__data:
            prefix_uris.append(dict(prefix=item["prefix"], uri=item["uri"]))
        return prefix_uris


