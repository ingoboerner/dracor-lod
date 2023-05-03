"""CRMcls Ontology Draft

(almost) aligned to https://gitlab.clsinfra.io/cls-infra/wp5wp6/mkm-cidoc/-/blob/vera/model/CLSCorDataModel.ttl
"""

from rdflib import Namespace
from cidoc import E73InformationObject, E55Type, E7Activity, E29DesignOrProcedure, E83TypeCreation, E90SymbolicObject
from lrmoo import F3Manifestation
from crmdig import D1DigitalObject

CLSCORNAMESPACE = "https://clscor.io/ontologies/CRMcls/"

CLS = Namespace(CLSCORNAMESPACE)


class X1Corpus(D1DigitalObject, F3Manifestation):
    """X1 Corpus

    SubClassOf crmdig: D1 Digital Object AND lrm: F3 Manifestation
    """

    class_uri = CLSCORNAMESPACE + "X1_Corpus"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X2CorpusDocument(D1DigitalObject, F3Manifestation):
    """X2 Document

    SubClassOf crmdig: D1 Digital Object AND lrm: F3 Manifestation
    """

    class_uri = CLSCORNAMESPACE + "X2_Corpus_Document"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X3Feature(E73InformationObject, E55Type):
    """X3 Feature

    SubClassOf crm: E73 Information Object AND crm: E55 Type
    """

    class_uri = CLSCORNAMESPACE + "X3_Feature"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X4Project(E7Activity):
    """X4 Project

    SubClassOf crm: E7 Activity
    """
    class_uri = CLSCORNAMESPACE + "X4_Project"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X5ResearchActivity(E7Activity):
    """X5 Research Activity

    SubClassOf crm: E7 Activity
    """
    class_uri = CLSCORNAMESPACE + "X5_Research_Activity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X6Method(E29DesignOrProcedure):
    """X6 Method

    SubClassOf crm: E29 Design or Procedure
    """
    class_uri = CLSCORNAMESPACE + "X6_Method"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X7Format:
    """X7 Format

    owl:equivalentClass pem:PE43_Encoding_Type .

    TODO: this does not inherit from anything
    """
    class_uri = CLSCORNAMESPACE + "X7_Format"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X8Schema:
    """X8 Schema

    owl:equivalentClass pem:PE38_Schema .

    TODO: this does not inherit from anything
    """
    class_uri = CLSCORNAMESPACE + "X8_Schema"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X9CorpusDescription(E83TypeCreation):
    """X9 Corpus Description

    subClassOf E83 Type Creation
    """
    class_uri = CLSCORNAMESPACE + "X9_Corpus_Description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X10EncodingPattern(E90SymbolicObject):
    """X10 Encoding Pattern

    SubClassOf crm: E90 Symbolic Object
    """
    class_uri = CLSCORNAMESPACE + "X10_Encoding_Pattern"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X11PrototypicalDocument(E55Type):
    """X11 Prototypical Corpus Document

    SubClassOf crm: E55 Type
    """

    class_uri = CLSCORNAMESPACE + "X11_Prototypical_Document"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



