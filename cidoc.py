"""The implemented class hierarchy MUST not be confused with the CIDOC-CRM class hierarchy! There might be some classes
in between that have not been implemented.

"""
import logging
from rdflib import Graph, URIRef, Namespace
from entity import Entity

cidoc_ns = "http://www.cidoc-crm.org/cidoc-crm/"
CRM = Namespace(cidoc_ns)


class CRM_Entity(Entity):
    """ E1 CRM Entity
    """

    class_uri = cidoc_ns + "E1_CRM_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_identified_by(self, *entities, uris: list = None) -> bool:
        """P1 is identified by

        Args:
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """

        if uris:
            logging.debug("Will add P1 is identified by and inverse for each uri.")

            assert type(self.graph) == Graph, "Entity doesn't have a graph to add data to."

            for id_uri in uris:
                self.graph.add((URIRef(self.uri), CRM.P1_is_identified_by, URIRef(id_uri)))
                self.graph.add((URIRef(id_uri), CRM.P1i_identifies, URIRef(self.uri)))

        if entities:
            for entity in entities:
                id_uri = entity.uri
                self.graph.add((URIRef(self.uri), CRM.P1_is_identified_by, URIRef(id_uri)))
                self.graph.add((URIRef(id_uri), CRM.P1i_identifies, URIRef(self.uri)))

                # add the graph data
                self.graph = self.graph + entity.graph

        return True


class Appellation(CRM_Entity):
    """E41 Appellation
    """

    class_uri = cidoc_ns + "E41_Appellation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Type(CRM_Entity):
    """E55 Type"""

    class_uri = cidoc_ns + "E55_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)