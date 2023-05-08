"""Parthenos Entities Model (PEM)

(https://cidoc-crm.org/sites/default/files/Parthenos%20Entities%20Model%20Description%20v%203.1.pdf)
(see also: https://cidoc-crm.org/Resources/parthenos-entities-research-infrastructure-model)

Tentative CLScor DM will re-use:

- PE8_E-Service
- PE19_Persistent_Digital_Object
- PE23_Volatile_Software
- PE37_Protocol_Type
- PE38_Schema
- PE43_Encoding_Type (coequal with Feature, Format, Language, etc.)


CIDOC E51 Contact Point is deprecated; in PE29 Access Point superclass was changed to E41 Appellation (see also CIDOC Version 7.1.2)
"""

from rdflib import Namespace
from cidoc import E7Activity, E70Thing, E55Type, E39Actor, E41Appellation
from crmdig import D1DigitalObject, D14Software

# Strange namespace, but it's in the RDF-XML of PEM (Downloaded this: http://parthenos.d4science.org/CRMext/CRMpe.rdfs)
NAMESPACE = "http://parthenos.d4science.org/CRMext/CRMpe.rdfs#"

PEM = Namespace(NAMESPACE)


class PE1Service(E7Activity):
    """PE1 Service

    SubClassOf crm: E7 Activity

    PP2 provided by: E39 Actor
    PP42 has declarative time [Not implemented]
    PP45 has competency: PE36 Competency Type
    PP51 has availability: PE39 Availability Type
    """
    class_uri = NAMESPACE + "PE1_Service"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pp2_provided_by(self, *entities, uris: list = None) -> bool:
        """PP2 provided by (provides): E39 Actor

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = PEM.PP2_provided_by
        prop_inverse = PEM.PP2i_provides

        range_class_constraint = E39Actor

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    # PP42 has declarative time [Not implemented]

    def pp45_has_competency(self, *entities, uris: list = None) -> bool:
        """PP45 has competency (is competency of): PE36 Competency Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = PEM.PP45_has_competency
        prop_inverse = PEM.PP45i_is_competency_of

        range_class_constraint = PE36CompetencyType

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    def pp51_has_availability(self, *entities, uris: list = None) -> bool:
        """PP51 has availability (is availability of): PE39 Availability Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = PEM.PP51_has_availability
        prop_inverse = PEM.PP51i_is_availability_of

        range_class_constraint = PE39AvailabilityType

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)


class PE8EService(PE1Service):
    """PE8 E-Service

    SubClassOf PE1 Service

    PP28 has designated access point (is designated access point of): PE29 Access Point
    PP29 uses access protocol: D14 Software [Not implemented]
    PP47 has protocol type: PE37 Protocol Type [Not implemented]
    PP48 uses protocol parameter: PE38 [Not implemented]
    PP49 provides access point: PE29 [Not implemented]
    """

    class_uri = NAMESPACE + "PE8_E-Service"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pp28_has_designated_access_point(self, *entities, uris: list = None) -> bool:
        """PP28 has designated access point (is designated access point of): PE29 Access Point

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = PEM.PP28_has_designated_access_point
        prop_inverse = PEM.PP28i_is_designated_access_point_of

        range_class_constraint = PE29AccessPoint

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)

    # PP29 uses access protocol: D14 Software [Not implemented]
    # PP47 has protocol type: PE37 Protocol Type [Not implemented]
    # PP48 uses protocol parameter: PE38 [Not implemented]

    def pp49_provides_access_point(self, *entities, uris: list = None) -> bool:
        """PP49 provides access point (is access point provided by): PE29 Access Point

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = PEM.PP49_provides_access_point
        prop_inverse = PEM.PP49i_is_access_point_provided_by

        range_class_constraint = PE29AccessPoint

        return self.add_triples(entities=list(entities),
                                uris=uris,
                                prop=prop,
                                prop_inverse=prop_inverse,
                                range_class_constraint=range_class_constraint)


class PE19PersistentDigitalObject(D1DigitalObject):
    """PE19 Persistent Digital Object

    SubClassOf crmdig: D1 Digital Object

    PP16 has persistent digital object part: PE19 Persistent Digital Object [Not implemented]
    """

    class_uri = NAMESPACE + "PE19_Persistent_Digital_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE32CuratedThing(E70Thing):
    """PE32 Curated Thing

    SubClassOf crm: E70 Thing
    """

    class_uri = NAMESPACE + "PE32_Curated_Thing"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE20VolatileDigitalObject(D1DigitalObject, E70Thing):
    """PE20 Volatile Digital Object

    SubClassOf PE32 Curated Thing AND D1 Digital Object
    """

    class_uri = NAMESPACE + "PE20_Volatile_Digital_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE23VolatileSoftware(D14Software, PE20VolatileDigitalObject):
    """PE23 Volatile Software

    SubClassOf crmdig: D14 Software AND PE20 Volatile Digital Object
    """

    class_uri = NAMESPACE + "PE23_Volatile_Software"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE37ProtocolType(E55Type):
    """PE37 Protocol Type
    SubClassOf crm: E55 Type
    """

    class_uri = NAMESPACE + "PE37_Protocol_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE38Schema(D14Software):
    """PE38 Schema

    SubClassOf crmdig: D14 Software
    """
    class_uri = NAMESPACE + "PE38_Schema"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE43EncodingType(E55Type):
    """PE43 Encoding Type

    SubClassOf crm: E55 Type
    """
    class_uri = NAMESPACE + "PE43_Encoding_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE36CompetencyType(E55Type):
    """PE36 Competency Type

    SubClassOf crm: E55 Type
    """
    class_uri = NAMESPACE + "PE36_Competency_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE39AvailabilityType(E55Type):
    """PE39 Availability Type

    SubClassOf crm: E55 Type
    """
    class_uri = NAMESPACE + "PE39_Availability_Type"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE29AccessPoint(E41Appellation):
    """PE29 Access Point

    SubClassOf crm: E51 Contact Point [deprecated];
    changed this to E41 Appellation (see CIDOC Version 7.1.2)
    """
    class_uri = NAMESPACE + "PE29_Access_Point"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


