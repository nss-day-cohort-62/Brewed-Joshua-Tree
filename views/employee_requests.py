from models import Employee
import sqlite3
import json

EMPLOYEES = [
    {
        "id": 1,
        "name": "Dale Gribble",
        "email": "governmentbad@texas.gov",
        "hourly_rate": 18,
    }
]


# going to write new get_all_employees
def get_all_employees():
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT 
            e.id,
            e.name,
            e.hourly_rate,
            e.email
        FROM employee e
        """
        )

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(
                row["id"], row["name"], row["hourly_rate"], row["email"]
            )
            employees.append(employee.__dict__)

    return employees


# writing for demo

# def get_all_employees():
#     """This function will return all employees"""
#     return EMPLOYEES


def get_single_employee(id):
    """This function will get a single employee by passing ID"""
    requested_employee = None

    for employee in EMPLOYEES:
        # need to sort thru employees with "if"
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
