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


# Working hard or hardly working?
# writing for demo

# showing pull request deets

# def get_all_employees():
#     """This function will return all employees"""
#     return EMPLOYEES


def get_single_employee(id):
    """This function will get a single employee by passing ID"""

    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.hourly_rate,
            e.email
        FROM employee e
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'],
                            data['hourly_rate'], data['email'])

        return employee.__dict__


def create_employee(new_employee):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, email, hourly_rate )
        VALUES
            ( ?, ?, ?);
        """, (new_employee['name'], new_employee['email'],
              new_employee['hourly_rate']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id

    return new_employee


def update_employee(id, new_employee):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE EMPLOYEE
            SET
                name = ?,
                email = ?,
                hourly_rate = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['email'], new_employee['hourly_rate'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_employee(id):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))


def get_employees_by_name(name):
    """This is a function that gets employees by name"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.hourly_rate,
            e.email
        FROM employee e
        WHERE e.name = ?
        """, (name, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['hourly_rate'], row['email'])
            employees.append(employee.__dict__)

    return employees
