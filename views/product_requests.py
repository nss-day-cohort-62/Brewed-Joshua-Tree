PRODUCTS = [
    {"id": 1, "name": "Squeek Toy", "price": 20.00},
    {"id": 2, "name": "Holy Roller", "price": 30.00},
]


def get_all_products():
    """
    Function that returns a list of products.
    """
    return PRODUCTS


def get_single_product(id):
    """Return single instance of product"""
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product


def create_product(product):
    """create product"""

    # Get the id value of the last product in the list
    max_id = PRODUCTS[-1]["id"]

    # Adds 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to product dictionary
    product["id"] = new_id

    # Adds the product dictionary to the list
    PRODUCTS.append(product)

    # Returns the dictionary with `id` property added
    return product
def create_productALL(product):
    """create product"""

    # Get the id value of the last product in the list
    max_id = PRODUCTS[-1]["id"]

    # Adds 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to product dictionary
    product["id"] = new_id

    # Adds the product dictionary to the list
    PRODUCTS.append(product)

    # Returns the dictionary with `id` property added
    return PRODUCTS
