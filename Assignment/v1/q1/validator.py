#######################
#  Validation methods #
#######################

import re
from datetime import datetime


def validate_customer_id(prompt):
    while True:
        customer_id = input(prompt)

        if not customer_id:
            print("Warning: Customer id required. \n")

        if customer_id:
            if not customer_id.isdigit():
                print("Warning: Customer id must be a number. \n")
            else:
                return customer_id


def validate_name(prompt):
    name_pattern = r'^[a-zA-Z\s-]+$'

    while True:
        name = input(prompt).lower()
        if not name:
            print("Warning: Customer name is required. \n")
        elif not re.match(name_pattern, name):
            print("Warning: Invalid customer name entered. \n")
        else:
            return name


def validate_postcode(prompt):
    while True:
        postcode = input(prompt)
        if not postcode:
            return postcode

        if postcode:
            if not postcode.isdigit():
                print("INFO: Postcode must be a number between 0000-9999. \n")
            elif len(postcode) != 4:
                print("INFO: Postcode must be 4 digits in length. \n")
            else:
                return postcode


def validate_phone_number(prompt):
    while True:
        phone_number = input(prompt)
        if not phone_number:
            return phone_number

        if not phone_number.isdigit():
            print("INFO: Phone number must be number. \n")
        elif not phone_number.startswith('04'):
            print("INFO: Phone number must start with 04. \n")
        else:
            return phone_number

def validate_transaction_id(prompt):
    while True:
        transaction_id = input(prompt)

        if not transaction_id:
            print("INFO: Transaction id required. \n")

        if transaction_id:
            if not transaction_id.isdigit():
                print("INFO: Transaction id must be a number. \n")
            else:
                return transaction_id


def validate_date(prompt):
    while True:
        transaction_date = input(prompt)

        try:
            datetime.strptime(transaction_date, '%Y-%m-%d')
        except ValueError:
            print("Transaction date is invalid. Try again. \n")
        else:
            if datetime.strptime(transaction_date, '%Y-%m-%d') < datetime.today():
                return transaction_date
            print("INFO: Date in future not allowed. \n")


def validate_category(prompt):
    categories = [
        "food",
        "alcohol and beverage",
        "apparel",
        "furniture",
        "household appliances",
        "computer equipment"
    ]

    while True:
        category = input(prompt).lower()

        if not category:
            print("INFO: Category is required. \n")
        elif category not in categories:
            print("INFO: Choose a category from the available option. \n")
        else:
            return category


def validate_value(prompt):
    while True:
        try:
            sales_value = float(input(prompt))
        except ValueError:
            print("INFO: Invalid sales value. Only number allowed.")
        else:
            return str(sales_value)