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

        Add triples to the self.graph either for each passed entity or for each URI provided in "uris".

        Args:
            *entities: Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = CRM.P1_is_identified_by
        prop_inverse = CRM.P1i_identifies

        if entities:
            for entity in entities:
                g = self.generate_property_to_entity_triples(entity, prop=prop, prop_inverse=prop_inverse)
                self.graph = self.graph + g

            return True

        elif uris:
            g = self.generate_property_to_uris_triples(uris=uris, prop=prop, prop_inverse=prop_inverse)
            self.graph = self.graph + g

            return True

        else:
            logging.warning("No data provided to generate triples from.")
            return False


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