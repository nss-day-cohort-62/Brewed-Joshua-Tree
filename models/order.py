class Order:
    """A member of Brewed-Joshua-Tree.
    Stores all currently relevant data for our Order class in fields.
    """

    def __init__(self, id, employee_id, product_id, timestamp):
        self.id = id
        self.employee_id = employee_id
        self.product_id = product_id
        self.timestamp = timestamp
