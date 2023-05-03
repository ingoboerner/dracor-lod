"""LRMoo (Draft Version 0.9)

Python module to provide LRMoo classes and their properties as Python classes and methods.

Author: Ingo Börner
"""

from rdflib import Namespace
from cidoc import E89PropositionalObject, E73InformationObject, E24PhysicalHumanMadeThing, E65Creation, E12Production, \
    E7Activity

# Base uri used for Class URIs
NAMESPACE = "http://www.cidoc-crm.org/cidoc-crm/lrmoo/"

LRM = Namespace(NAMESPACE)


class F1Work(E89PropositionalObject):
    """F1 Work

    SubClassOf crm:E89 Propositional Object

    R1 is logical successor of (has successor): F1 Work
    R2 is derivative of (has derivative): F1 Work
    (R2.1 has type: E55 Type) [Not implemented]
    R3 is realised in (realises): F2 Expression
    R10 has member (is member of): F1 Work
    R67 has part (forms part of): F1 Work
    R68 is inspired by (is inspiration for): F1 Work
    R73 takes representative attribute from (bears representative attribute for): F2 Expression
    R74 uses expression of (has expression used in): F1 Work
    """

    class_uri = NAMESPACE + "F1_Work"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r1_is_logical_successor_of(self, *entities, uris: list = None) -> bool:
        """R1 is logical successor of (has successor): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R1_is_logical_successor_of
        prop_inverse = LRM.R1i_has_successor

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r1i_has_successor(self, *entities, uris: list = None) -> bool:
        """R1i has successor (is logical successor of): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R1i_has_successor
        prop_inverse = LRM.R1_is_logical_successor_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r2_is_derivative_of(self, *entities, uris: list = None) -> bool:
        """R2 is derivative of (has derivative): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R2_is_derivative_of
        prop_inverse = LRM.R2i_has_derivative

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r2i_has_derivative(self, *entities, uris: list = None) -> bool:
        """R2i has derivative (is derivative of): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R2i_has_derivative
        prop_inverse = LRM.R2_is_derivative_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r3_is_realised_in(self, *entities, uris: list = None) -> bool:
        """R3 is realised in (realises): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R3_is_realised_in
        prop_inverse = LRM.R3i_realises

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r10_has_member(self, *entities, uris: list = None) -> bool:
        """R10 has member (is member of): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R10_has_member
        prop_inverse = LRM.R10i_is_member_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r10i_is_member_of(self, *entities, uris: list = None) -> bool:
        """R10i is member of (has member): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R10i_is_member_of
        prop_inverse = LRM.R10_has_member

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r67_has_part(self, *entities, uris: list = None) -> bool:
        """R67 has part (forms part of): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R67_has_part
        prop_inverse = LRM.R67i_forms_part_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r67i_forms_part_of(self, *entities, uris: list = None) -> bool:
        """R67i forms part of (has part): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R67i_forms_part_of
        prop_inverse = LRM.R67_has_part

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r68_is_inspired_by(self, *entities, uris: list = None) -> bool:
        """R68 is inspired by (is inspiration for): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R68_is_inspired_by
        prop_inverse = LRM.R68i_is_inspiration_for

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r68i_is_inspiration_for(self, *entities, uris: list = None) -> bool:
        """R68i is inspiration for (is inspired by): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R68i_is_inspiration_for
        prop_inverse = LRM.R68_is_inspired_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r73_takes_representative_attribute_from(self, *entities, uris: list = None) -> bool:
        """R73 takes representative attribute from (bears representative attribute for): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R73_takes_representative_attribute_from
        prop_inverse = LRM.R73i_bears_representative_attribute_for

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r74_uses_expression_of(self, *entities, uris: list = None) -> bool:
        """R74 uses expression of (has expression used in): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R74_uses_expression_of
        prop_inverse = LRM.R74i_has_expression_used_in

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r74i_has_expression_used_in(self, *entities, uris: list = None) -> bool:
        """R74i has expression used in (uses expression of): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R74i_has_expression_used_in
        prop_inverse = LRM.R74_uses_expression_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r16i_was_created_by(self, *entities, uris: list = None) -> bool:
        """R16i created (was created by): F27 Work Creation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R16i_was_created_by
        prop_inverse = LRM.R16_created

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r19i_was_realised_through(self, *entities, uris: list = None) -> bool:
        """R19i was realised through (created a realisation of): F28 Expression Creation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R19i_was_realised_through
        prop_inverse = LRM.R19_created_a_realisation_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F2Expression(E73InformationObject):
    """F2 Expression

    SubClassOf crm:E73 Information Object

    R5 has component (is component of): F2 Expression
    R15 has fragment (is fragment of): E90 Symbolic Object
    R75 incorporates (is incorporated in): F2 Expression
    R76 is derivative of (has derivative): F2 Expression
    (R76.1 has type: E55 Type) [Not implemented]
    """

    class_uri = NAMESPACE + "F2_Expression"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r5_has_component(self, *entities, uris: list = None) -> bool:
        """R5 has component (is component of): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R5_has_component
        prop_inverse = LRM.R5i_is_component_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r5i_is_component_of(self, *entities, uris: list = None) -> bool:
        """R5i is component of (has component): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R5i_is_component_of
        prop_inverse = LRM.R5_has_component

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r15_has_fragment(self, *entities, uris: list = None) -> bool:
        """R15 has fragment (is fragment of): E90 Symbolic Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R15_has_fragment
        prop_inverse = LRM.R15i_is_fragment_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r75_incorporates(self, *entities, uris: list = None) -> bool:
        """R75 incorporates (is incorporated in): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R75_incorporates
        prop_inverse = LRM.R75i_is_incorporated_in

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r75i_is_incorporated_in(self, *entities, uris: list = None) -> bool:
        """R75i is incorporated in (incorporates): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R75i_is_incorporated_in
        prop_inverse = LRM.R75_incorporates

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r76_is_derivative_of(self, *entities, uris: list = None) -> bool:
        """R76 is derivative of (has derivative): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R76_is_derivative_of
        prop_inverse = LRM.R76i_has_derivative

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r76i_has_derivative(self, *entities, uris: list = None) -> bool:
        """R76i has derivative (is derivative of): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R76i_has_derivative
        prop_inverse = LRM.R76_is_derivative_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r3i_realises(self, *entities, uris: list = None) -> bool:
        """R3i realises (is realised in): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R3i_realises
        prop_inverse = LRM.R3_is_realised_in

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r73i_bears_representative_attribute_for(self, *entities, uris: list = None) -> bool:
        """R73i bears representative attribute for (takes representative attribute from): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R73i_bears_representative_attribute_for
        prop_inverse = LRM.R73_takes_representative_attribute_from

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r4i_is_embodied_in(self, *entities, uris: list = None) -> bool:
        """R4i is embodied in (embodies): F3 Manifestation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R4i_is_embodied_in
        prop_inverse = LRM.R4_embodies

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r17i_was_created_by(self, *entities, uris: list = None) -> bool:
        """R17i was created by (created): F28 Expression Creation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R17i_was_created_by
        prop_inverse = LRM.R17_created

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F3Manifestation(F2Expression):
    """F3 Manifestation

    SubClassOf F2 Expression

    R4 embodies (is embodied in): F2 Expression
    R69 has physical form (is physical form of): E55 Type
    R70 has dimension (is dimension of): E54 Dimension
    R71 has part (is part of): F3 Manifestation
    """

    class_uri = NAMESPACE + "F3_Manifestation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r4_embodies(self, *entities, uris: list = None) -> bool:
        """R4 embodies (is embodied in): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R4_embodies
        prop_inverse = LRM.R4i_is_embodied_in

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r69_has_physical_form(self, *entities, uris: list = None) -> bool:
        """R69 has physical form (is physical form of): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R69_has_physical_form
        prop_inverse = LRM.R69i_is_physical_form_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r70_has_dimension(self, *entities, uris: list = None) -> bool:
        """R70 has dimension (is dimension of): E54 Dimension

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R70_has_dimension
        prop_inverse = LRM.R70i_is_dimension_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r71_has_part(self, *entities, uris: list = None) -> bool:
        """R71 has part (is part of): F3 Manifestation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R71_has_part
        prop_inverse = LRM.R71i_is_part_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r71i_is_part_of(self, *entities, uris: list = None) -> bool:
        """R71i is part of (has part): F3 Manifestation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R71i_is_part_of
        prop_inverse = LRM.R71_has_part

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r7i_is_materialization_of(self, *entities, uris: list = None) -> bool:
        """R7i is materialized in (is materialization of): F5 Item

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R7i_is_materialized_in
        prop_inverse = LRM.R7_is_materialization_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r24i_was_created_through(self, *entities, uris: list = None) -> bool:
        """R24i was created through (created): F30 Manifestation Creation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R24i_was_created_through
        prop_inverse = LRM.R24_created

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F5Item(E24PhysicalHumanMadeThing):
    """F5 Item

    SubClassOf crm: E24 Physical Human-Made Thing

    R7 is materialization of (is materialized in): F3 Manifestation
    """

    class_uri = NAMESPACE + "F5_Item"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r7_is_materialization_of(self, *entities, uris: list = None) -> bool:
        """R7 is materialization of (is materialized in): F3 Manifestation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R7_is_materialization_of
        prop_inverse = LRM.R7i_is_materialized_in

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F27WorkCreation(E65Creation):
    """F27 Work Creation

    SubClassOf crm: E65 Creation

    R16 created (was created by): F1 Work

    """

    class_uri = NAMESPACE + "F27_Work_Creation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r16_created(self, *entities, uris: list = None) -> bool:
        """R16 created (was created by): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R16_created
        prop_inverse = LRM.R16i_was_created_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F28ExpressionCreation(E65Creation, E12Production):
    """F28 Expression Creation

    SubClassOf crm: E65 Creation AND crm: E12 Production

    R17 created (was created by): F2 Expression
    R19 created a realisation of (was realised through): F1 Work
    """

    class_uri = NAMESPACE + "F28_Expression_Creation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r17_created(self, *entities, uris: list = None) -> bool:
        """R17 created (was created by): F2 Expression

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R17_created
        prop_inverse = LRM.R17i_was_created_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def r19_created_a_realisation_of(self, *entities, uris: list = None) -> bool:
        """R19 created a realisation of (was realised through): F1 Work

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R19_created_a_realisation_of
        prop_inverse = LRM.R19i_was_realised_through

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F30ManifestationCreation(F28ExpressionCreation):
    """F30 Manifestation Creation

    SubClassOf F28 Expression Creation

    R24 created (was created through): F3 Manifestation
    """

    class_uri = NAMESPACE + "F30_Manifestation_Creation"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r24_created(self, *entities, uris: list = None) -> bool:
        """R24 created (was created through): F3 Manifestation

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R24_created
        prop_inverse = LRM.R24i_was_created_through

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class F31Performance(E7Activity):
    """F31 Performance

    SubClassOf E7 Activity

    R66 included performed version of (had a performed version through): E89 Propositional Object
    """
    class_uri = NAMESPACE + "F31_Performance"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def r66_included_performed_version_of(self, *entities, uris: list = None) -> bool:
        """R66 included performed version of (had a performed version through): E89 Propositional Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = LRM.R66_included_performed_version_of
        prop_inverse = LRM.R66i_had_a_performed_version_through

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

