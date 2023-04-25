import sqlite3
import json
from models import Order

ORDERS = [{"id": 1, "employeeId": 1, "productId": 1, "timestamp": 13042023}]


def get_all_orders():
    """This function gets the list of all order dictionaries"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT 
            o.id,
            o.employee_id,
            o.product_id,
            o.timestamp
        FROM "order" o
        """
        )

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(
                row["id"], row["employee_id"], row["product_id"], row["timestamp"]
            )
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
            a.employee_Id,
            a.product_Id,
            a.timestamp
        FROM "order" a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        requested_order = Order(data['id'], data['employee_Id'],
                                data['product_Id'], data['timestamp'])

        return requested_order


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
