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
"""

from rdflib import Namespace
from cidoc import E7Activity, E70Thing, E55Type
from crmdig import D1DigitalObject, D14Software

# Strange namespace, but it's in the RDF-XML of PEM (Downloaded this: http://parthenos.d4science.org/CRMext/CRMpe.rdfs)
NAMESPACE = "http://parthenos.d4science.org/CRMext/CRMpe.rdfs#"

PEM = Namespace(NAMESPACE)


class PE1Service(E7Activity):
    """PE1 Service

    SubClassOf crm: E7 Activity

    PP2 provided by: E39 Actor [Not implemented]
    PP42 has declarative time [Not implemented]
    PP45 has competency: PE36 Competency Type [Not implemented]
    PP51 has availability: PE39 Availability Type [Not implemented]
    """
    class_uri = NAMESPACE + "PE1_Service"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PE8EService(PE1Service):
    """PE8 E-Service

    SubClassOf PE1 Service

    PP28 has designated access point: PE29 [Not implemented]
    PP29 uses access protocol: D14 Software [Not implemented]
    PP47 has protocol type: PE37 Protocol Type [Not implemented]
    PP48 uses protocol parameter: PE38 [Not implemented]
    PP49 provides access point: PE29 [Not implemented]
    """

    class_uri = NAMESPACE + "PE8_E-Service"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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


