"""General Stuff regarding DraCor goes here, e.g. defined prefixes

"""
import logging


class DraCor:
    """DraCor

    Attributes:
          ontologies (list): Ontologies used
    """
    ontologies = [
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
            "uri": "http://www.cidoc-crm.org/cidoc-crm/",
            "version": "v7.1.2"
        },
        {
            "prefix": "cls",
            "uri": "http://clscor.io/ontology/"
        },
        {
            "prefix": "lrm",
            "uri": "http://www.cidoc-crm.org/cidoc-crm/lrmoo/",
            "version": "v0.9"
        }
    ]

    def __init__(self):
        pass

    def get_prefix_uri(self, prefix: str) -> str:
        """Get the uri for a prefix form self.ontologies

        Args:
            prefix (str): Prefix to get URI for

        Returns:
            str: URI
        """
        assert self.ontologies

        try:
            uri = list(filter(lambda item: prefix in item["prefix"], self.ontologies))[0]["uri"]
        except IndexError:
            logging.warning(f"Prefix '{prefix}' is not defined.")
            uri = None

        return uri
