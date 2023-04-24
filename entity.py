"""Entity

Provides basic functionality of all entities.
"""
import logging

from marshmallow import Schema, fields, ValidationError


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
        labels (list): Labels
    """

    # URI of the class
    class_uri = None

    # URI
    uri = None

    # rdfs:labels
    labels = None
    """
    [ 
        {
            "lang": "de", 
            "label" : "Das ist das label"
        } 
    ]
    """

    def __init__(self,
                 class_uri: str = None,
                 uri: str = None,
                 labels: list = None,
                 **kwargs
                 ):
        """Initialize

        Args:
            class_uri (str, optional): URI of the entity class
            uri (str, optional): URI of the Entity
            labels (list, optional): Labels (rdfs:label)
        """
        if class_uri:
            assert type(class_uri) == str, "Invalid type. Expected a string."
            self.class_uri = class_uri

        if uri:
            assert type(uri) == str, "Invalid type. Expected a string."
            self.uri = uri

        if labels:
            # Validate contents of the label list before adding
            assert type(labels) == list, "Invalid type. Expected a list."
            label_schema = LabelSchema()
            valid_labels = True
            # TODO: Maybe add only valid labels instead of purging all if one is not correct
            for item in labels:
                if self.__validate_item(item, label_schema) is False:
                    valid_labels = False
                    logging.debug("Validation of item failed.")

            if valid_labels is True:
                self.labels = labels
                logging.debug("Added valid labels.")

            else:
                self.labels = None
                logging.warning("Validation of labels failed. Not adding labels")

    @staticmethod
    def __validate_item(item: dict, schema: Schema) -> bool:
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


class CRM_Entity(Entity):
    """ A Dummy entity; just for reference on how to use super()
    """

    class_uri = "http://www.cidoc-crm.org/cidoc-crm/" + "E1_CRM_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
