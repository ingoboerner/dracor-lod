"""CRMcls Unstable Ontology Draft

(almost) aligned to https://gitlab.clsinfra.io/cls-infra/wp5wp6/mkm-cidoc/-/blob/vera/model/CLSCorDataModel.ttl, 
left out the properties because they have yet to be consolidated.
"""

from rdflib import Namespace
from cidoc import E73InformationObject, E55Type, E7Activity, E29DesignOrProcedure, E83TypeCreation, E90SymbolicObject
from lrmoo import F3Manifestation
from crmdig import D1DigitalObject, D14Software
from pem import PE43EncodingType

NAMESPACE = "https://clscor.io/ontologies/CRMcls/"

CLS = Namespace(NAMESPACE)


class X1Corpus(D1DigitalObject, F3Manifestation):
    """X1 Corpus

    SubClassOf crmdig: D1 Digital Object AND lrm: F3 Manifestation
    """

    class_uri = NAMESPACE + "X1_Corpus"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X2CorpusDocument(D1DigitalObject, F3Manifestation):
    """X2 Document

    SubClassOf crmdig: D1 Digital Object AND lrm: F3 Manifestation
    """

    class_uri = NAMESPACE + "X2_Corpus_Document"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X3Feature(E73InformationObject, E55Type):
    """X3 Feature

    SubClassOf crm: E73 Information Object AND crm: E55 Type
    """

    class_uri = NAMESPACE + "X3_Feature"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X4Project(E7Activity):
    """X4 Project

    SubClassOf crm: E7 Activity
    """
    class_uri = NAMESPACE + "X4_Project"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X5ResearchActivity(E7Activity):
    """X5 Research Activity

    SubClassOf crm: E7 Activity
    """
    class_uri = NAMESPACE + "X5_Research_Activity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X6Method(E29DesignOrProcedure):
    """X6 Method

    SubClassOf crm: E29 Design or Procedure
    """
    class_uri = NAMESPACE + "X6_Method"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X7Format(PE43EncodingType):
    """X7 Format

    owl:equivalentClass pem:PE43_Encoding_Type (= SubClassOf crm: E55 Type) .

    TODO: this does not inherit from anything. PE43 is a subclass of crm: E55 Type; I inherit here directly (cf. X8!)
    """
    class_uri = NAMESPACE + "X7_Format"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X8Schema(D14Software):
    """X8 Schema

    owl:equivalentClass pem:PE38_Schema (=SubClassOf dig: D14 Software) .

    TODO: check inheritance; because equivalent, I also inherit from D14; but maybe inherit directly from pem: PE38
    """
    class_uri = NAMESPACE + "X8_Schema"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X9CorpusDescription(E83TypeCreation):
    """X9 Corpus Description

    subClassOf E83 Type Creation
    """
    class_uri = NAMESPACE + "X9_Corpus_Description"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X10EncodingPattern(E90SymbolicObject):
    """X10 Encoding Pattern

    SubClassOf crm: E90 Symbolic Object
    """
    class_uri = NAMESPACE + "X10_Encoding_Pattern"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class X11PrototypicalDocument(E55Type):
    """X11 Prototypical Corpus Document

    SubClassOf crm: E55 Type
    """

    class_uri = NAMESPACE + "X11_Prototypical_Document"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


"""
crmcls:Z9_has_subcorpus a rdf:Property ;
    rdfs:label "hat als Subkorpus"@de,
        "has subcorpus"@en ;
    rdfs:comment "associates a corpus with its subcorpus"@en ;
    rdfs:domain crmcls:X1_Corpus ;
    rdfs:range crmcls:X1_Corpus ;
    rdfs:subPropertyOf crm:P148_has_component .

crmcls:Z9i_is_subcorpus_of a rdf:Property ;
    rdfs:label "ist Subkorpus von"@de,
        "is subcorpus of"@en ;
    rdfs:comment "associates subcorpus with its super corpus"@en ;
    rdfs:domain crmcls:X1_Corpus ;
    rdfs:range crmcls:X1_Corpus ;
    rdfs:subPropertyOf crm:P148i_is_component_of .

"""
