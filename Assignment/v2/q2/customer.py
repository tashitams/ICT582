import csv
import os
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

    def import_customer_from_csv(self):
        csv_file = validate_csv_file("Enter CSV file name (required): ")
        customer_ids = set(customer["customer_id"] for customer in self.customers)
        id_already_exists = []
        customer_already_exist = False

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['customer_id'] not in customer_ids:
                        self.customers.append({
                            "customer_id": row['customer_id'],
                            "name": row['name'].lower(),
                            "postcode": row['postcode'],
                            "phone_number": row['phone_number']
                        })
                    else:
                        id_already_exists.append(row['customer_id'])
                        customer_already_exist = True

        except FileNotFoundError:
            print(f"Info: {csv_file} not found")
        except Exception as e:
            print(f"Error: An error occurred: {e}")
        else:
            if customer_already_exist:
                print(f"Error: Import failed, record already exist for following customer id {id_already_exists}")
            else:
                print("Success: Customer records from CSV imported successfully.")

        input("Press 'Enter' key to continue...")

    def export_customer_to_csv(self):
        if not self.customers:
            print("Info: No customer records to export.")

        else:
            csv_file = validate_csv_file("Enter CSV file name (required): ")

            if os.path.isfile(csv_file):
                print(f"\nWARNING: {csv_file} already exist.")
                print("Press 1: Change the file name")
                print("Press 2: Overwrite the file")
                print("Press 3: Cancel the operation \n")

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_file_name = validate_csv_file("Enter new CSV file name (required): ")
                        export(new_file_name, self.customers)
                        return

                    elif choice == '2':
                        export(csv_file, self.customers)
                        return

                    elif choice == '3':
                        print("Operation canceled. \n")
                        input("Press 'Enter' key to continue...")
                        break

                    else:
                        print("Invalid option selected. Try again! \n")

            else:
                export(csv_file, self.customers)

def export(name, customers):
    try:
        with open(name, 'w', newline='', encoding='utf-8-sig') as file:
            field_names = customers[0].keys()
            csv_writer = csv.DictWriter(file, fieldnames=field_names)

            # Write the header row
            csv_writer.writeheader()

            for row in customers:
                csv_writer.writerow(row)
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

    else:
        print(f"Customer data has been exported to '{name}' successfully.")

    input("Press 'Enter' key to continue...")


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

def validate_csv_file(prompt):
    while True:
        file_path = input(prompt)

        if not file_path:
            print("CSV file name is required! \n")
        elif not file_path.endswith('.csv'):
            print("Invalid file format. Please provide a CSV file. \n")
        else:
            return file_path
