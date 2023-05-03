"""CRM Dig (Version: 4.0 unstable)

Python module to provide CRMdig classes and their properties as Python classes and methods.

Author: Ingo Börner
"""


from rdflib import Namespace
from cidoc import E73InformationObject, E54Dimension, E11Modification, E65Creation, E16Measurement

# Base uri used for Class URIs
NAMESPACE = "http://www.ics.forth.gr/isl/CRMdig/"

DIG = Namespace(NAMESPACE)


class D1DigitalObject(E73InformationObject):
    """D1 Digital Object

    SubClassOf crm: E73 Information Object
    """

    class_uri = NAMESPACE + "D1_Digital_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l10i_was_input_of(self, *entities, uris: list = None) -> bool:
        """L10i was input of (had input): D7 Digital Machine Event

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L10i_was_input_of
        prop_inverse = DIG.L10_had_input

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def l11i_was_output_of(self, *entities, uris: list = None) -> bool:
        """L11i was output of (had output): D7 Digital Machine Event

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L10i_was_output_of
        prop_inverse = DIG.L11_had_output

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def l2i_was_source_for(self, *entities, uris: list = None) -> bool:
        """L2i was source for (used as source): D10 Software Execution

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L2i_was_source_for
        prop_inverse = DIG.L2_used_as_source

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class D7DigitalMachineEvent(E11Modification, E65Creation):
    """D7 Digital Machine Event

    SubClassOf crm: E11 Modification AND crm: E65 Creation

    L10 had input (was input of): D1 Digital Object
    L11 had output (was output of): D1 Digital Object
    L12 happened on device (was device for): D8 Digital Device [Not implemented]
    L18 has modified (was modified by): D13 Digital Information Carrier [Not implemented]
    L23 used software or firmware (was software or firmware used by): D14 Software
    """
    class_uri = NAMESPACE + "D7_Digital_Machine_Event"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l10_had_input(self, *entities, uris: list = None) -> bool:
        """L10 had input (was input of): D1 Digital Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L10_had_input
        prop_inverse = DIG.L10i_was_input_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def l11_had_output(self, *entities, uris: list = None) -> bool:
        """L11 had output (was output of): D1 Digital Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L11_had_output
        prop_inverse = DIG.L10i_was_output_of

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def l23_used_software_or_firmware(self, *entities, uris: list = None) -> bool:
        """L23 used software or firmware (was software or firmware used by): D14 Software

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L23_used_software_or_firmware
        prop_inverse = DIG.L23i_was_software_or_firmware_used_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class D9DataObject(D1DigitalObject, E54Dimension):
    """D9 Data Object

    SubClassOf D1 Digital Object AND crm: E54 Dimension
    """

    class_uri = NAMESPACE + "D9_Data_Object"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l20i_has_created(self, *entities, uris: list = None) -> bool:
        """L20i was created by (has created): D11 Digital Measurement Event

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L20i_was_created_by
        prop_inverse = DIG.L20_has_created

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class D10SoftwareExecution(D7DigitalMachineEvent):
    """D10 Software Execution

    SubClassOf D7 Digital Machine Event

    L2 used as source (was source for): D1 Digital Object
    L13 used parameters (parameters for): D1 Digital Object [Not implemented]
    L24 created logfile (was logfile created by): D1 Digital Object [Not implemented]
    """

    class_uri = NAMESPACE + "D10_Software_Execution"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l2_used_as_source(self, *entities, uris: list = None) -> bool:
        """L2 used as source (was source for): D1 Digital Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L2_used_as_source
        prop_inverse = DIG.L2i_was_source_for

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class D11DigitalMeasurementEvent(D7DigitalMachineEvent, E16Measurement):
    """D11 Digital Measurement Event

    SubClassOf D7 Digital Machine Event AND E16 Measurement

    L17 measured thing of type (was type of thing measured by): E55 Type
    L20 has created (was created by): D9 Data Object
    """
    class_uri = NAMESPACE + "D11_Digital_Measurement_Event"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l17_measured_thing_of_type(self, *entities, uris: list = None) -> bool:
        """L17 measured thing of type (was type of thing measured by): E55 Type

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L17_measured_thing_of_type
        prop_inverse = DIG.L17i_was_type_of_thing_measured_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

    def l20_has_created(self, *entities, uris: list = None) -> bool:
        """L20 has created (was created by): D9 Data Object

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L20_has_created
        prop_inverse = DIG.L20i_was_created_by

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)


class D14Software(D1DigitalObject):
    """D14 Software

    SubClassOf D1 Digital Object
    """
    class_uri = NAMESPACE + "D14_Software"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def l23i_was_software_or_firmware_used_by(self, *entities, uris: list = None) -> bool:
        """L23i was software or firmware used by (used software or firmware): D7 Digital Machine Event

        Args:
            *entities (optional): Any number of instances of an Entity class
            uris (list, optional): List of URIs of entities that identify this

        Returns:
             bool: True if added
        """
        prop = DIG.L23i_was_software_or_firmware_used_by
        prop_inverse = DIG.L23_used_software_or_firmware

        return self.add_triples(entities=list(entities), uris=uris, prop=prop, prop_inverse=prop_inverse)

