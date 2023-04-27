import sqlite3
from models import Product


PRODUCTS = [
    {"id": 1, "name": "Squeek Toy", "price": 20.00},
    {"id": 2, "name": "Holy Roller", "price": 30.00},
]


def get_products_by_name(name):

    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            p.id,
            p.name,
            p.price
        from Product p
        WHERE p.name = ?
        """, (name, ))

        products = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            product = Product(row['id'], row['name'], row['price'])

            products.append(product.__dict__)

    return products


def get_all_products():
    """
    Function that returns a list of products.
    """
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT 
            p.id,
            p.name,
            p.price
        FROM Product p
        """
        )

        products = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            product = Product(row["id"], row["name"], row["price"])
            products.append(product.__dict__)

    return products


def get_single_product(id):
    """Return single instance of product from SQL data"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM product p
        WHERE p.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        product = Product(data['id'], data['name'], data['price'])

    return product.__dict__


def create_product(new_product):
    """create product"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Product
            (name, price)
        VALUES
            (?, ?);
        """, (new_product['name'], new_product['price'], ))

        id = db_cursor.lastrowid

        new_product['id'] = id

    return new_product


def update_product(id, new_product):
    """Update product in SQL table"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Product
            SET
                
                name = ?,
                price = ?
        WHERE id = ?
        """, (new_product['name'], new_product['price'], new_product['id']))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

    # # Get the id value of the last product in the list
    # max_id = PRODUCTS[-1]["id"]

    # # Adds 1 to whatever that number is
    # new_id = max_id + 1

    # # Add an `id` property to product dictionary
    # product["id"] = new_id

    # # Adds the product dictionary to the list
    # PRODUCTS.append(product)

    # # Returns the dictionary with `id` property added
    # return product


def delete_product(id):
    """This is a function for deleting an product"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM product
        WHERE id = ?
        """, (id, ))
