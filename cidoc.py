"""The implemented class hierarchy MUST not be confused with the CIDOC-CRM class hierarchy! There might be some classes
in between that have not been implemented.

"""
import logging
from rdflib import Namespace, URIRef, Literal
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
        """P1 is identified by (identifies): E41 Appellation

        Add triples "P1 is identified by" and inverse to the self.graph either for each passed entity
        or for each URI provided in "uris".

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
            bool: True if added

        """
        prop = CRM.P1_is_identified_by
        prop_inverse = CRM.P1i_identifies

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def has_type(self, *entities, uris: list = None) -> bool:
        """P2 has type (is type of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P2_has_type
        prop_inverse = CRM.P2i_is_type_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def has_note(self, content: str, lang: str = None) -> bool:
        """P3 has note: E62 String

        Args:
            content (str): Textual content of the note
            lang (str, optional): Language of the note. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = CRM.P3_has_note

        if lang:
            self.graph.add((URIRef(self.uri), prop, Literal(content, lang=lang)))
        else:
            self.graph.add((URIRef(self.uri), prop, Literal(content)))

        return True

    def has_preferred_identifier(self, *entities, uris: list = None) -> bool:
        """P48 has preferred identifier (is preferred identifier of): E42 Identifier

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P48_has_preferred_identifier
        prop_inverse = CRM.P48i_is_preferred_identifier_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def exemplifies(self, *entities, uris: list = None) -> bool:
        """P137 exemplifies( is exemplified by): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P137_exemplifies
        prop_inverse = CRM.P137i_is_exemplified_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Appellation(CRM_Entity):
    """E41 Appellation
    """

    class_uri = cidoc_ns + "E41_Appellation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Identifier(Appellation):
    """E42 Identifier
    """

    class_uri = cidoc_ns + "E42_Identifier"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Type(CRM_Entity):
    """E55 Type"""

    class_uri = cidoc_ns + "E55_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
