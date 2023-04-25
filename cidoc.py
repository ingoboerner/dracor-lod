from entity import Entity

cidoc_ns = "http://www.cidoc-crm.org/cidoc-crm/"
class CRM_Entity(Entity):
    """ A Dummy entity; just for reference on how to use super()
    """

    class_uri = cidoc_ns + "E1_CRM_Entity"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
