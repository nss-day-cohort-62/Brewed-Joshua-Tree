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
    """This function will return all employees"""
    return EMPLOYEES


def get_single_employee(id):
    """This function will get a single employee by passing ID"""
    requested_employee = None

    for employee in EMPLOYEES:
        # need to sort thru employees with "if"
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
