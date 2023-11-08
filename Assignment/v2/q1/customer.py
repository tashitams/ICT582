import re
from random import randint


class Customer:
    customers = []

    def add_customer(self):
        customer_id = str(randint(100000, 999999))
        name = validate_name("Enter customer name (required): ")
        postcode = validate_postcode("Enter postcode (optional): ")
        phone_number = validate_phone_number("Enter phone_number (optional): ")

        self.customers.append({
            'customer_id': customer_id,
            'name': name,
            'postcode': postcode,
            'phone_number': phone_number
        })

        print(f"\nSuccess: Customer with id '{customer_id} saved successfully.")
        input("Press 'Enter' key to continue...")

    def search_customers(self):
        search_term = input("Enter your search term: ")

        search_result = [
            customer for customer in self.customers if
            search_term == customer['customer_id'] or
            search_term.lower() in customer['name'] or
            search_term == customer['postcode'] or
            search_term == customer['phone_number']
        ]

        if search_result:
            print("+---------------------------------------+")
            print("|       Customer search results         |")
            print("+---------------------------------------+")

            for customer in search_result:
                print(f"Customer ID   : {customer['customer_id']}")
                print(f"Customer Name : {customer['name'].title()}")
                print(f"Postcode      : {customer['postcode']}")
                print(f"Phone Number  : {customer['phone_number']}")
                print("+---------------------------------------+ \n")
        else:
            print(f"No customer found for search term '{search_term}'.\n")

        input("Press 'Enter' key to continue... \n")

    def delete_customer(self):
        from transaction import Transaction

        customer_deleted = False

        customer_id = validate_customer_id("Enter customer id to delete: ")

        for customer in self.customers:
            if customer_id == customer['customer_id']:
                self.customers.remove(customer)

                for transaction in Transaction.transactions:
                    if customer_id == transaction['customer_id']:
                        Transaction.transactions.remove(transaction)

                customer_deleted = True
                break

        if customer_deleted:
            print(f"Success: Customer with id {customer_id} deleted successfully.")
        else:
            print(f"Info: No customer for id {customer_id} found.")


# validation methods
# ------------------
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
                print("Warning: Postcode must be a number between 0000-9999. \n")
            elif len(postcode) != 4:
                print("Warning: Postcode must be 4 digits in length. \n")
            else:
                return postcode


def validate_phone_number(prompt):
    while True:
        phone_number = input(prompt)
        if not phone_number:
            return phone_number

        if not phone_number.isdigit():
            print("Warning: Phone number must be number. \n")
        elif not phone_number.startswith('04'):
            print("Warning: Phone number must start with 04. \n")
        else:
            return phone_number
