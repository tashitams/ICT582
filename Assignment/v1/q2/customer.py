import csv
import os
import sys
import validator
from random import randint

file_exist_warning = """
+----------------- WARNING -----------------+
|          The file already exist.          |
|                                           |
|  Press 1: Change the file name            |
|  Press 2: Overwrite the file              |
|  Press 3: Cancel the operation            |
+-------------------------------------------+

+------------ Select an option  ------------+
"""

class Customer:
    customers = []

    def add(self):
        print("+---------------------------------------+")
        print("|              Add customer             |")
        print("+---------------------------------------+")

        customer_id = str(randint(100000, 999999))

        self.customers.append({
            'customer_id': customer_id,
            'name': validator.validate_name("Enter customer name (required): "),
            'postcode': validator.validate_postcode("Enter postcode (optional): "),
            'phone_number': validator.validate_phone_number("Enter phone_number (optional): ")
        })

        print(f"Customer with id '{customer_id} saved successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def search(self):
        print("+---------------------------------------+")
        print("|           Search customers            |")
        print("+---------------------------------------+")

        search_term = input("Search using customer's id, name, postcode or phone number: ")

        search_result = []

        for customer in self.customers:
            if (search_term == customer['customer_id'] or
                    search_term.lower() in customer['name'].lower() or
                    search_term == customer['postcode'] or
                    search_term == customer['phone_number']):
                search_result.append(customer)

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

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def delete(self):
        print("+---------------------------------------+")
        print("|            Delete customer            |")
        print("+---------------------------------------+")
        delete_flag = False

        customer_id = validator.validate_customer_id("Enter customer id to delete: ")

        for customer in self.customers:
            if customer_id == customer['customer_id']:
                self.customers.remove(customer)
                remove_customer_transaction(customer_id)
                delete_flag = True
                break

        if delete_flag:
            print(f"Customer with id {customer_id} deleted successfully.")
        else:
            print(f"No customer for id {customer_id} found.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def load_customer_from_csv(self):
        print("+---------------------------------------+")
        print("|      Load customer from CSV file      |")
        print("+---------------------------------------+")

        csv_file = validator.validate_csv_file("Enter csv file path (required): ")

        customer_ids = set(customer["customer_id"] for customer in self.customers)

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    customer_id = row['customer_id']
                    if customer_id not in customer_ids:
                        self.customers.append({
                            "customer_id": customer_id,
                            "name": row['name'].lower(),
                            "postcode": row['postcode'],
                            "phone_number": row['phone_number']
                        })
        except FileNotFoundError:
            print(f"{csv_file} not found")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Customer records from CSV file loaded successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def save_customer_to_csv(self):
        print("+---------------------------------------+")
        print("|       Save customer to CSV file       |")
        print("+---------------------------------------+")

        if not self.customers:
            print("There is no customer records to export.")

        else:
            csv_file = validator.validate_csv_file("Enter csv file path (required): ")

            if os.path.isfile(csv_file):

                print(file_exist_warning)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_file_name = validator.validate_csv_file("Enter new csv file path (required): ")
                        save_to_csv_file(new_file_name, self.customers)
                        break

                    elif choice == '2':
                        save_to_csv_file(csv_file, self.customers)
                        break

                    elif choice == '3':
                        print("Operation canceled.")
                        input("Press 'Enter' key to continue...")
                        break

                    else:
                        print("Invalid option selected. Try again!")

            else:
                save_to_csv_file(csv_file, self.customers)

def remove_customer_transaction(customer_id):
    from transaction import Transaction

    Transaction.transactions = [
        transaction for transaction in Transaction.transactions
        if transaction['customer_id'] != customer_id
    ]

def save_to_csv_file(name, customers):
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
        print(f"Customer data has been exported to '{name}'.")

    print("Press 'Enter' key to continue...")
    sys.stdin.read(1)
