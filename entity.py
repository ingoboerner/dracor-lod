"""Entity

Provides basic functionality of all entities.
"""
import logging
from marshmallow import Schema, fields, ValidationError
from sparql import DB


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
        database (DB): Triple Store connection
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
    # Database connection
    database = None

    # TODO: should have "mode"=create/fetch depending on pulled from triple store or created (default)
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
        if class_uri:
            assert type(class_uri) == str, "Invalid type. Expected a string."
            self.class_uri = class_uri

        if uri:
            assert type(uri) == str, "Invalid type. Expected a string."
            self.uri = uri

        if labels:
            self.load_labels(data=labels, mode=mode)

        if database:
            assert type(database) == DB, "Invalid type. Expected sparql.DB (database connection)."
            self.database=database

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
    def load_labels(self,
                    data: list = None,
                    mode: str = "create",
                    validation: bool = True) -> bool:
        """Load labels data.

        If the flag is set to create, it is expected, that there is a list of labels passed as "data".
        If "mode" is set to "fetch" data should be retrieved from the triple store using self.database.

        Args:
            data (list): Data of labels. Should confirm to schema LabelSchema.
            mode (str): create from labels data or fetch ("fetch") data from triple store. Defaults to "create".
            validation (bool): Validate with LabelSchema Defaults to True.

        Returns:
            bool: True if successful

        """
        if mode == "create":
            logging.debug("Trying to create labels from data.")

            if data:
                assert type(data) == list, "Invalid type. Expected a list."

                # should be cast into a list (was None?!)
                # Would be better to check for the type and then append, if it is already a list; this will overwrite
                self.labels = []

                if validation:
                    schema = LabelSchema()

                for item in data:
                    if validation:
                        if self.__item_is_valid(item, schema) is True:
                            self.labels.append(item)
                        else:
                            logging.debug("Validation of item failed.")
                            pass
                    else:
                        self.labels.append(item)

                # Operation was successful, if it appended a label
                if len(self.labels) > 0:
                    logging.debug(f"Successfully added {len(self.labels)} labels.")
                    return True
                else:
                    return False
            else:
                logging.warning("No data provided. Can not load labels.")
                return False

        else:
            raise Exception("Fetching data not implemented.")


class CRM_Entity(Entity):
    """ A Dummy entity; just for reference on how to use super()
    """

    class_uri = "http://www.cidoc-crm.org/cidoc-crm/" + "E1_CRM_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
