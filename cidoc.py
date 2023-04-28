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


class Design_or_Procedure(Information_Object):
    """E29 Design or Procedure

    subClassOf E73 Information Object

    P68 foresees use of (use foreseen by): E57 Material [Not implemented]
    P69 has association with (is associated with): E29 Design or Procedure
    (P69.1 has type: E55 Type) [Not implemented]

    """
    class_uri = cidoc_ns + "E29_Design_or_Procedure"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_association_with(self, *entities, uris: list = None) -> bool:
        """P69 has association with (is associated with): E29 Design or Procedure

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P69_has_association_with
        prop_inverse = CRM.P69i_is_associated_with

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Linguistic_Object(Information_Object):
    """E33 Linguistic Object

    subClassOf E73 Information Object

    P72 has language (is language of): E56 Language
    P73 has translation (is translation of): E33 Linguistic Object
    """

    class_uri = cidoc_ns + "E33_Linguistic_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_language(self, *entities, uris: list = None) -> bool:
        """P72 has language (is language of): E56 Language

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P72_has_language
        prop_inverse = CRM.P72i_is_language_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def has_translation(self, *entities, uris: list = None) -> bool:
        """P73 has translation (is translation of): E33 Linguistic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P73_has_translation
        prop_inverse = CRM.P73i_is_translation_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Appellation(Symbolic_Object):
    """E41 Appellation

    subClassOf E90 Symbolic Object

    P139 has alternative form: E41 Appellation
    Implemented inverse: P1i_identifies: E1 CRM Entity
    """

    class_uri = cidoc_ns + "E41_Appellation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_alternative_form(self, *entities, uris: list = None) -> bool:
        """P139 has alternative form: E41 Appellation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P139_has_alternative_form
        prop_inverse = CRM.P139i_is_alternative_form_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def identifies(self, *entities, uris: list = None) -> bool:
        """P1i identifies (is identified by): E1 CRM Entity

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P1i_identifies
        prop_inverse = CRM.P1_is_identified_by

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Identifier(Appellation):
    """E42 Identifier

    No specialized properties.
    """

    class_uri = cidoc_ns + "E42_Identifier"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Title
#class Title()

class Type(Conceptual_Object):
    """E55 Type

    SubClassOf E28 Conceptual Object

    P127 has broader term (has narrower term): E55 Type
    P150 defines typical parts of (define typical wholes for): E55 Type

    Implemented inverse: P2i is type of: E1 CRM Entity
    """

    class_uri = cidoc_ns + "E55_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_broader_term(self, *entities, uris: list = None) -> bool:
        """P127 has broader term (has narrower term): E55 Type

        Implemented in both directions, see self.has_broader_term

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P127_has_broader_term
        prop_inverse = CRM.P127i_has_narrower_term

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def has_narrower_term(self, *entities, uris: list = None) -> bool:
        """P127i has narrower term (has broader term): E55 Type

        Implemented in both directions, see self.has_broader_term

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P127i_has_narrower_term
        prop_inverse = CRM.P127_has_broader_term

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def defines_typical_parts_of(self, *entities, uris: list = None) -> bool:
        """P150 defines typical parts of (defines typical wholes for): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P150_defines_typical_parts_of
        prop_inverse = CRM.P150i_defines_typical_wholes_for

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def defines_typical_wholes_for(self, *entities, uris: list = None) -> bool:
        """P150i defines typical wholes for (defines typical parts of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P150i_defines_typical_wholes_for
        prop_inverse = CRM.P150_defines_typical_parts_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def is_type_of(self, *entities, uris: list = None) -> bool:
        """P2i is type of (has type): E1 CRM Entity

        Implemented in both directions, see self.has_type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P2i_is_type_of
        prop_inverse = CRM.P2_has_type

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Measurement_Unit(Type):
    """E58 Measurement Unit

    subClassOf E55 Type

    No specialized properties.
    """

    class_uri = cidoc_ns + "E58_Measurement_Unit"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Temporal_Entity(CRM_Entity):
    """E2 Temporal Entity

    subClassOf E1 CRM Entity

    P4 has time-span (is time-span of): E52 Time-Span
    P173 starts before or with the end of (ends after or with the start of): E2 Temporal Entity [Not implemented]
    P174 starts before the end of (ends after the start of): E2 Temporal Entity [Not implemented]
    P175 starts before or with the start of (starts after or with the start of): E2 Temporal Entity [Not implemented]
    P176 starts before the start of (starts after the start of): E2 Temporal Entity [Not implemented]
    P182 ends before or with the start of (starts after or with the end of): E2 Temporal Entity [Not implemented]
    P183 ends before the start of (starts after the end of): E2 Temporal Entity [Not implemented]
    P184 ends before or with the end of (ends with or after the end of): E2 Temporal Entity [Not implemented]
    P185 ends before the end of (ends after the end of): E2 Temporal Entity [Not implemented]

    """
    class_uri = cidoc_ns + "E2_Temporal_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_timespan(self, *entities, uris: list = None) -> bool:
        """P4 has time-span (is time-span of): E52 Time-Span

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM["P4_has_time-span"]
        prop_inverse = CRM["P4i_is_time-span_of"]

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Period(Temporal_Entity):
    """E4 Period

    P7 took place at (witnessed): E53 Place
    P8 took place on or within (witnessed): E18 Physical Thing [Not implemented]
    P9 consists of (forms part of): E4 Period

    This is there because of the examples: Italian Renaissance (Macdonald, 1992), Sturm und Drang (Berkoff, 2013),
    Cubism (Cox, 2000), ...
    """

    class_uri = cidoc_ns + "E4_Period"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def took_place_at(self, *entities, uris: list = None) -> bool:
        """P7 took place at (witnessed): E53 Place

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P7_took_place_at
        prop_inverse = CRM.P7i_witnessed

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def consists_of(self, *entities, uris: list = None) -> bool:
        """P9 consists of (forms part of): E4 Period

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P9_consists_of
        prop_inverse = CRM.P9i_forms_part_of

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Event(Period):
    """E5 Event
    SubClassOf E4 Period

    P11 had participant (participated in): E39 Actor
    P12 occurred in the presence of (was present at): E77 Persistent Item
    """

    class_uri = cidoc_ns + "E5_Event"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def had_participant(self, *entities, uris: list = None) -> bool:
        """P11 had participant (participated in): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P11_had_participant
        prop_inverse = CRM.P11i_participated_in

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)

    def had_participant(self, *entities, uris: list = None) -> bool:
        """P12 occurred in the presence of (was present at): E77 Persistent Item

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = CRM.P12_occurred_in_the_presence_of
        prop_inverse = CRM.P12i_was_present_at

        return self.add_triples(entities, uris=uris, prop=prop, prop_inverse=prop_inverse)


class Activity(Event):
    """E7_Activity

    SubClassOf E5 Event

    P14 carried out by (performed): E39 Actor (P14.1 in the role of: E55 Type)
    P15 was influenced by (influenced): E1 CRM Entity P16 used specific object (was used for): E70 Thing
    (P16.1 mode of use: E55 Type) [Not implemented]
    P17 was motivated by (motivated): E1 CRM Entity
    P19 was intended use of (was made for): E71 Human-Made Thing
    (P19.1 mode of use: E55 Type) [Not implemented]
    P20 had specific purpose (was purpose of): E5 Event
    P21 had general purpose (was purpose of): E55 Type
    P32 used general technique (was technique of): E55 Type
    P33 used specific technique (was used by): E29 Design or Procedure
    P125 used object of type (was type of object used in): E55 Type

    TODO: implement
    """

    class_uri = cidoc_ns + "E7_Activity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Attribute_Assginment(Activity):
    """E13 Attribute Assginment

    TODO: implement
    """

    class_uri = cidoc_ns + "E13_Attribute_Assignment"

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


# E39 Actor !