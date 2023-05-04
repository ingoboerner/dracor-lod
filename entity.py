"""Entity

Provides basic functionality of all entities.
"""
import logging
from marshmallow import Schema, fields, ValidationError
from sparql import DB
from rdflib import Graph, Literal, URIRef, RDF, RDFS
from ontologies import Ontologies

ONTOLOGIES = Ontologies()
PREFIXES = ONTOLOGIES.get_prefixes_uris()


class LabelSchema(Schema):
    """Schema for the source data to generate rdfs:label"""
    lang = fields.Str()
    label = fields.Str()


class Entity:
    """Entity

    General class of an Entity

    Attributes:
        class_uri: URI of the Entity Class
        uri (str): URI of the Entity
        database (DB): Triple Store connection
        graph (Graph): Entity as rdflib.Graph
    """

    # URI of the class
    class_uri = None

    # URI
    uri = None

    # Database connection
    database = None

    # Graph
    graph = None

    def __init__(self,
                 class_uri: str = None,
                 uri: str = None,
                 labels: list = None,
                 mode: str = "create",
                 database: DB = None,
                 **kwargs
                 ):
        """Initialize

        Args:
            class_uri (str, optional): URI of the entity class
            uri (str, optional): URI of the Entity
            labels (list, optional): Labels (rdfs:label)
            mode (str): Create new data ("create") or fetch ("fetch") existing data from a triple store
            database (DB): Triple Store Connection
        """

        # Create the graph
        self.graph = self.__initialize_graph()

        if uri:
            assert type(uri) == str, "Invalid type. Expected a string."
            self.uri = uri

        if class_uri:
            assert type(class_uri) == str, "Invalid type. Expected a string."
            self.class_uri = class_uri
            self.graph = self.graph + self.instance_of_class()

        elif self.class_uri:
            # this was set on the class level; should also add it to the graph
            self.graph = self.graph + self.instance_of_class()

        if labels:
            """
                [ 
                    {
                        "lang": "de", 
                        "label" : "Das ist das label"
                    } 
                ]
            """
            self.add_labels(data=labels, mode=mode)

        if database:
            assert type(database) == DB, "Invalid type. Expected sparql.DB (database connection)."
            self.database = database

    @staticmethod
    def __item_is_valid(item: dict, schema: Schema) -> bool:
        """Helper function to validate labels

        Args:
            item (dict): Item to validate
            schema (Schema): Schema used to validate

        Returns:
            bool: True if valid
        """
        try:
            schema.load(item)
            return True
        except ValidationError:
            logging.debug("Validation failed.")
            return False

    @staticmethod
    def __initialize_graph() -> Graph:
        """Return a bare rdflib.graph with prefixes

        Returns:
            bool: True if successful
        """

        g = Graph()

        # add the namespaces
        for item in PREFIXES:
            g.namespace_manager.bind(item["prefix"], URIRef(item["uri"]))

        return g

    def add_labels(self, data: list = None, mode: str = "create") -> bool:
        """Add rdfs: labels to the graph.

        If the flag is set to create, it is expected, that there is a list of labels passed as "data".
        mode="fetch" is not implemented.

        Args:
            data (list): Data of labels. Should confirm to schema LabelSchema.
            mode (str): create from labels data or fetch ("fetch"). Defaults to "create".

        Returns:
            bool: True if successful

        """
        if mode == "create":
            self.graph = self.graph + self.__generate_rdfs_labels(labels=data)
            return True

        else:
            raise Exception("Fetching data not implemented.")

    def __generate_rdfs_labels(self,
                               domain_uri: str = None,
                               labels: list = None,
                               lang_to_literals: bool = False,
                               validation: bool = True) -> Graph:
        """Generate rdfs:labels

        Args:
            domain_uri (str): URI of the domain. Defaults to self.uri
            labels (list): label data
            lang_to_literals (bool): Explicitly add language to literals. Defaults to False.

        Returns:
            Graph: rdflib.Graph containing the labels

        """
        if labels:
            assert type(labels) == list, "Invalid type. Expected a list."

            if validation:
                schema = LabelSchema()
                for item in labels:
                    if self.__item_is_valid(item, schema) is False:
                        labels.pop(item)
                        logging.debug("Validation of item failed. Removed.")

            if len(labels) > 0:

                g = Graph()

                if domain_uri:
                    domain = URIRef(domain_uri)
                else:
                    if self.uri:
                        domain = URIRef(self.uri)
                    else:
                        logging.warning("No URI of this entity is set. Will not add labels.")
                        return Graph()

                if len(labels) > 1 and lang_to_literals is False:
                    logging.warning("Set not to explicitly add language, but provided multiple labels.")

                for item in labels:
                    if lang_to_literals is False:
                        g.add((domain, RDFS.label, Literal(item["label"])))
                    else:
                        g.add(domain, RDFS.label, Literal(item["label"], lang=item["lang"]))

                return g

            else:
                logging.warning("No label data validated. Can not create labels.")
                return Graph()

        else:
            logging.warning("No label data provided. Can not create labels.")
            return Graph()

    def instance_of_class(self, domain_uri: str = None, class_uri: str = None) -> Graph:
        """Create a graph containing the statement domain_uri a class_uri

        domain_uri a class_uri

        Args:
            domain_uri (str): URI of the domain. Defaults to self.uri
            class_uri (str): URI of the class Defaults to self.class_uri

        Returns:
            Graph: rdflib Graph
        """
        if domain_uri:
            domain_e = URIRef(domain_uri)
        else:
            # assert self.uri, "No URI for instance is set."
            if self.uri:
                domain_e = URIRef(self.uri)
            else:
                logging.warning("No URI of this entity is set. Will not add rdf:type statement.")
                return Graph()

        if class_uri:
            range_e = URIRef(class_uri)
        else:
            if self.class_uri:
                range_e = URIRef(self.class_uri)
            else:
                logging.warning("Class URI is not set globally and no URI for range is set.")
                return Graph()

        g = Graph()
        g.add((domain_e, RDF.type, range_e))

        return g

    def generate_property_to_uris_triples(self,
                                            domain_uri: str = None,
                                            prop: URIRef = None,
                                            prop_inverse: URIRef = None,
                                            uris: list = None) -> Graph:
        """Add triples to graph: self.uri prop uri.

        Args:
            domain_uri (str): Domain. Defaults to self.uri.
            prop (URIRef, optional): Property. Expected rdflib.term.URIRef, e.g. CRM.P1_is_identified_by
            prop_inverse (URIRef, optional): Inverse Property. Expected rdflib.term.URIRef, e.g. CRM.P1i_identifies
            uris (list): list of URIs that will be the range of the triples.

        Returns:
            Graph: Triples in a graph
        """
        if prop:
            assert type(prop) == URIRef, "Invalid type. Expected property prop as URIRef."

        if prop_inverse:
            assert type(prop_inverse) == URIRef, "Invalid type. Expected property prop_inverse as URIRef."

        if domain_uri:
            domain_e = URIRef(domain_uri)
        else:
            # Default will be self.uri, which means: this entity
            if self.uri:
                domain_e = URIRef(self.uri)
            else:
                logging.warning("No self.uri set. Will not create anything.")
                return Graph()

        if uris:
            assert type(uris) == list, "Invalid type. Expected a list of uris."

            # results graph
            g = Graph()

            for id_uri in uris:
                if prop:
                    g.add((domain_e, prop, URIRef(id_uri)))

                if prop_inverse:
                    g.add((URIRef(id_uri), prop_inverse, domain_e))

            return g

        else:
            logging.warning("No uris set. Will not create anything.")
            return Graph()

    def generate_property_to_entity_triples(self,
                                            entity,
                                            domain_uri: str = None,
                                            prop: URIRef = None,
                                            prop_inverse: URIRef = None,
                                            range_class_constraint = None,
                                            ) -> Graph:
        """Add triples to graph: self.uri prop entity.uri.

        Args:
            entity: Instance of an entity class
            domain_uri (str): URI of the domain.
            prop (URIRef): Property. Expected rdflib.term.URIRef, e.g. CRM.P1_is_identified_by
            prop_inverse (URIRef, optional): Inverse Property. Expected rdflib.term.URIRef, e.g. CRM.P1i_identifies
            range_class_constraint (optional): Expected class as range or a subclass thereof

        Returns:
            Graph: Triples in a graph

        Raises:
            ValidationError: Wrong Class or subclass provided as range.
        """
        if prop:
            assert type(prop) == URIRef, "Invalid type. Expected property prop as URIRef."

        if prop_inverse:
            assert type(prop_inverse) == URIRef, "Invalid type. Expected property prop_inverse as URIRef."

        if domain_uri:
            domain_e = URIRef(domain_uri)
        else:
            # Default will be self.uri, which means: this entity
            if self.uri:
                domain_e = URIRef(self.uri)
            else:
                logging.warning("No self.uri set. Will not create anything.")
                return Graph()

        if entity:
            if range_class_constraint:
                if issubclass(type(entity), range_class_constraint) is False:
                    logging.warning(f"An instance of class '{type(entity).__name__}' is not allowed as range of"
                                    f" '{str(prop)}'. Must be an instance of '{range_class_constraint.__name__}'"
                                    f" or a subclass thereof.")
                    raise ValidationError("Wrong class of range")

            # results graph
            g = Graph()

            if entity.uri:

                if prop:
                    g.add((domain_e, prop, URIRef(entity.uri)))
                    g = g + entity.graph

                if prop_inverse:
                    g.add((URIRef(entity.uri), prop_inverse, domain_e))
                    g = g + entity.graph

            return g

        else:
            logging.warning("No entities provided. Will not create anything.")
            return Graph()

    def add_triples(self,
                    entities: list = None,
                    uris: list = None,
                    prop: URIRef = None,
                    prop_inverse: URIRef = None,
                    range_class_constraint=None
                    ) -> bool:
        """Add triples to self.graph.

        Domain will be self.uri. Pass either a list of entites (Entity) or a list of uris.

        Args:
            entities (list, optional): list of entites added as range of the triples
            uris (list, optional): list of uris added as range of the triples
            prop (URIRef, optional): Property
            prop_inverse (URIRef, optional) : Inverse Propery
            range_class_constraint (optional): Expected class as range or a subclass thereof

        Returns:
            bool: True if successful

        """
        if entities:
            for entity in entities:

                try:
                    g = self.generate_property_to_entity_triples(entity,
                                                                 prop=prop,
                                                                 prop_inverse=prop_inverse,
                                                                 range_class_constraint=range_class_constraint)
                    self.graph = self.graph + g

                except ValidationError:
                    # Wrong class or subclass was provided as range. Catch the ValidationError
                    return False

            return True

        elif uris:
            g = self.generate_property_to_uris_triples(uris=uris, prop=prop, prop_inverse=prop_inverse)
            self.graph = self.graph + g

            return True

        else:
            logging.warning("No data provided to generate triples from.")
            return False

    def dump(self) -> Graph:
        """Return the graph

        Returns:
            Graph: Instance as Graph

        """
        return self.graph

    def serialize(self, format: str = "ttl"):
        """Serialize the graph

        Args:
            format (str): Format of the serialization. Defaults to "ttl". Other values: e.g. "xml"
        """
        return self.graph.serialize(format=format)


