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

    P1 is identified by (identifies): E41 Appellation P2 has type (is type of): E55 Type
    P3 has note: E62 String
    (P3.1 has type: E55 Type) [Not implemented]
    P48 has preferred identifier (is preferred identifier of): E42 Identifier
    P137 exemplifies (is exemplified by): E55 Type
    (P137.1 in the taxonomic role: E55 Type) [Not implemented]
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


class Thing(CRM_Entity):
    """E70 Thing

    SubClassOf E77_Persistent_Item <- CRM Entity
    The class Persistent Item is not implemented (E77 does not have any specialized properties).

    P43 has dimension (is dimension of): E54 Dimension
    P101 had as general use (was use of): E55 Type
    P130 shows features of (features are also found on): E70 Thing
    (P130.1 kind of similarity: E55 Type) [Not implemented]
    """
    class_uri = cidoc_ns + "E70_Thing"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_dimension(self, *entities, uris: list = None) -> bool:
        """P43 has dimension (is dimension of): E54 Dimension

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P43_has_dimension
        prop_inverse = CRM.P43i_is_dimension_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def had_as_general_use(self, *entities, uris: list = None) -> bool:
        """P101 had as general use (was use of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P101_had_as_general_use
        prop_inverse = CRM.P101i_was_use_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def shows_features_of(self, *entities, uris: list = None) -> bool:
        """P130 shows features of (features are also found on): E70 Thing

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P130_shows_features_of
        prop_inverse = CRM.P130i_features_are_also_found_on

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Conceptual_Object(Thing):
    """E28 Conceptual Object

    SubClassOf E71 Human-Made Thing <- E70 Thing
    E71 is not implemented. Properties P102, P103 from E71 are implemented with this (E28).
    E28 does not have specialized properties.

    P102 has title (is title of): E35 Title [originally inherited from E71]
    (P102.1 has type: E55 Type) [Not implemented]
    P103 was intended for (was intention of): E55 Type [originally inherited from E71]
    """

    class_uri = cidoc_ns + "E28_Conceptual_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_title(self, *entities, uris: list = None) -> bool:
        """P102 has title (is title of): E35 Title [originally inherited from E71]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P102_has_title
        prop_inverse = CRM.P102i_is_title_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def was_intended_for(self, *entities, uris: list = None) -> bool:
        """P103 was intended for (was intention of): E55 Type [originally inherited from E71]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P103_was_intended_for
        prop_inverse = CRM.P103i_was_intention_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Propositional_Object(Conceptual_Object):
    """E89 Propositional Object

    SubClassOf E28 Conceptual Object

    P148 has component (is component of): E89 Propositional Object
    P67 refers to (is referred to by): E1 CRM Entity
    (P67.1 has type: E55 Type) [Not implemented]
    P129 is about (is subject of): E1 CRM Entity
    """

    class_uri = cidoc_ns + "E89_Propositional_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_component(self, *entities, uris: list = None) -> bool:
        """P148 has component (is component of): E89 Propositional Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P148_has_component
        prop_inverse = CRM.P148i_is_component_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def refers_to(self, *entities, uris: list = None) -> bool:
        """P67 refers to (is referred to by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P67_refers_to
        prop_inverse = CRM.P67i_is_referred_to_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def is_about(self, *entities, uris: list = None) -> bool:
        """P129 is about (is subject of): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P129_is_about
        prop_inverse = CRM.P129i_is_subject_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

class Symbolic_Object(Conceptual_Object):
    """E90 Symbolic Object

    SubClassOf E28 Conceptual Object AND E72 Legal Object (not implemented).
    The properties from E72 Legal Object are implemented here.

    P104 is subject to (applies to): E30 Right [inherited from E72 Legal Object]
    P105 right held by (has right on): E39 Actor [inherited from E72 Legal Object]

    P106 is composed of (forms part of): E90 Symbolic Object
    P190 has symbolic content: E62 String

    """

    class_uri = cidoc_ns + "E90_Symbolic_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_subject_to(self, *entities, uris: list = None) -> bool:
        """P104 is subject to (applies to): E30 Right [inherited from E72 Legal Object]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P104_is_subject_to
        prop_inverse = CRM.P104i_applies_to

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def right_held_by(self, *entities, uris: list = None) -> bool:
        """P105 right held by (has right on): E39 Actor [inherited from E72 Legal Object]

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P105_right_held_by
        prop_inverse = CRM.P105i_has_right_on

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def is_composed_of(self, *entities, uris: list = None) -> bool:
        """P106 is composed of (forms part of): E90 Symbolic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P106_is_composed_of
        prop_inverse = CRM.P106i_forms_part_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def has_symbolic_content(self, content: str, lang: str = None) -> bool:
        """P190 has symbolic content: E62 String

        Args:
            content (str): Textual content
            lang (str, optional): Language of the content. Added to the Literal.

        Returns:
             bool: True if added
        """
        prop = CRM.P190_has_symbolic_content

        if lang:
            self.graph.add((URIRef(self.uri), prop, Literal(content, lang=lang)))
        else:
            self.graph.add((URIRef(self.uri), prop, Literal(content)))

        return True


class Information_Object(Symbolic_Object, Propositional_Object):
    """E73 Information Object

    SubClassOf E90 Symbolic Object AND E89 Propositional Object

    P165 incorporates (is incorporated in): E90 Symbolic Object

    """

    class_uri = cidoc_ns + "E73_Information_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def incorporates(self, *entities, uris: list = None) -> bool:
        """P165 incorporates (is incorporated in): E90 Symbolic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P165_incorporates
        prop_inverse = CRM.P165i_is_incorporated_in

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Appellation(Symbolic_Object):
    """E41 Appellation

    subClassOf E90 Symbolic Object

    TODO: Implement
    """

    class_uri = cidoc_ns + "E41_Appellation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Identifier(Appellation):
    """E42 Identifier

    TODO: Implement
    """

    class_uri = cidoc_ns + "E42_Identifier"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Type(CRM_Entity):
    """E55 Type
    SubClassOf ??

    TODO: implement
    """

    class_uri = cidoc_ns + "E55_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Activity(CRM_Entity):
    """E7_Activity

    SubClassOf ??

    TODO: implement
    """

    class_uri = cidoc_ns + "E7_Activity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Dimension(CRM_Entity):
    """E54 Dimension

    SubClassOf E1 CRM Entity

    P90 has value: E60 Number
    P91 has unit (is unit of): E58 Measurement Unit

    TODO: implement
    """

    class_uri = cidoc_ns + "E54_Dimension"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)