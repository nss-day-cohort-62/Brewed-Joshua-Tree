import sqlite3
import json
from models import Order

ORDERS = [{"id": 1, "employeeId": 1, "productId": 1, "timestamp": 13042023}]


def get_all_orders():
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

        requested_requested_order = Order(data['id'], data['emplooyee_Id'],
                                data['product_Id'], data['timestamp'])

        return requested_order
