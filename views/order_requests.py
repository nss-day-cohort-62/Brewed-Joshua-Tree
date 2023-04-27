import sqlite3
import json
from models import Order, Employee, Product

ORDERS = [{"id": 1, "employeeId": 1, "productId": 1, "timestamp": 13042023}]


def get_all_orders():
    """This function gets the list of all order dictionaries"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            o.id,
            o.employee_id,
            o.product_id,
            e.name employee_name,
            e.hourly_rate,
            e.email,
            p.name,
            p.price,
            o.timestamp
        FROM "order" o
        INNER JOIN Employee e
            ON e.id = o.employee_id
        INNER JOIN Product p
            ON p.id = o.product_id
        """
                          )

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(
                row["id"], row["employee_id"], row["product_id"], row["timestamp"]
            )

            employee = Employee(
                row["employee_id"], row["employee_name"], row["hourly_rate"], row["email"]
            )

            product = Product(
                row["product_id"], row["name"], row["price"]
            )

            order.employee = employee.__dict__
            order.product = product.__dict__

            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    """This function gets a single order based off ID"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
            a.id,
            a.employee_id,
            a.product_id,
            a.timestamp,
            e.name employee_name,
            e.hourly_rate,
            e.email,
            p.name product_name,
            p.price
        FROM "order" a
        JOIN Employee e
            ON e.id = a.employee_id
        JOIN Product p
            ON p.id = a.product_id
        """)

        orders = []

        data = db_cursor.fetchone()

        requested_order = Order(data['id'], data['employee_id'],
                                data['product_id'], data['timestamp'])
        employee = Employee(data['employee_id'], data['employee_name'],
                            data['hourly_rate'], data['email'])
        product = Product(data['product_id'],
                          data['product_name'], data['price'])

        requested_order.employee = employee.__dict__
        requested_order.product = product.__dict__

        orders.append(requested_order.__dict__)

        return orders


def create_order(new_order):
    """create order"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO "Order"
            (employee_Id, product_Id, timestamp)
        VALUES
            (?, ?, ?);
        """, (new_order['employee_id'], new_order['product_id'], new_order['timestamp']))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order


def update_order(id, new_order):
    """Update orders into SQL DB"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE `Order`
            SET
                employee_id = ?,
                product_id = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order['employee_id'], new_order['product_id'], new_order['timestamp'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_order(id):
    """Deletes orders from SQL database"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM 'Order'
        WHERE id = ?
        """, (id, ))
