ORDERS = [{"id": 1, "employeeId": 1, "productId": 1, "timestamp": 13042023}]


def get_all_orders():
    """this gets orders"""
    return ORDERS


def get_single_order(id):
    """This function gets a single order based off ID"""
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order
