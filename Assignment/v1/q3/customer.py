import csv
import os
import sys
import numpy as np
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
    customers = np.empty((0, 4))

    def add(self):
        print("+---------------------------------------+")
        print("|              Add customer             |")
        print("+---------------------------------------+")

        customer_id = str(randint(100000, 999999))
        name = validator.validate_name("Enter customer name (required): ")
        postcode = validator.validate_postcode("Enter postcode (optional): ")
        phone_number = validator.validate_phone_number("Enter phone_number (optional): ")

        customer_record = np.array([customer_id, name, postcode, phone_number])

        self.customers = np.append(self.customers, [customer_record], axis=0)

        print(f"\nCustomer with id '{customer_id} saved successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def search(self):
        print("+---------------------------------------+")
        print("|           Search customers            |")
        print("+---------------------------------------+")

        search_term = input("Search using customer's id, name, postcode or phone number: ")

        search_result = [
            customer for customer in self.customers
            if any(search_term in str(value) for value in customer)
        ]

        if search_result:
            print("+---------------------------------------+")
            print("|       Customer search results         |")
            print("+---------------------------------------+")
            for customer in search_result:
                print("Customer ID  :", customer[0])
                print("Name         :", customer[1].title())
                print("Postcode     :", customer[2])
                print("Phone Number :", customer[3])
                print("+---------------------------------------+ \n")
        else:
            print(f"\nNo customer found for search term '{search_term}'.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def delete(self):
        print("+---------------------------------------+")
        print("|            Delete customer            |")
        print("+---------------------------------------+")

        from transaction import Transaction

        # Get the customer ID to delete
        customer_id = validator.validate_customer_id("Enter customer id to delete: ")

        # Find the customer to delete
        customer = np.where(self.customers[:, 0] == customer_id)

        if customer[0].size > 0:
            # Delete the customer
            np.delete(self.customers, customer, axis=0)

            # Find and delete related transactions for the given customer id
            transaction = np.where(Transaction.transactions[:, 1] == customer_id)

            if transaction[0].size > 0:
                Transaction.transactions = Transaction.transactions[Transaction.transactions[:, 2] != customer_id]

            print(f"\nCustomer with ID {customer_id} and related transactions deleted successfully.")
        else:
            print(f"\nCustomer with ID {customer_id} not found.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def load_customer_from_csv(self):
        print("+---------------------------------------+")
        print("|      Load customer from CSV file      |")
        print("+---------------------------------------+")

        csv_file = validator.validate_csv_file("Enter CSV file path (required): ")

        customer_ids = set(self.customers[:, 0])

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    customer_id, name, postcode, phone_number = row
                    if customer_id not in customer_ids:
                        customer_record = np.array([customer_id, name, postcode, phone_number])
                        self.customers = np.append(self.customers, [customer_record], axis=0)
        except FileNotFoundError:
            print(f"INFO: {csv_file} not found")

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

        if np.size(self.customers) == 0:
            print("There is no customer records to save.")

        else:
            csv_file = validator.validate_csv_file("Enter CSV file path (required): ")

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

def save_to_csv_file(name, customers):
    try:
        with open(name, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['customer_id', 'name', 'postcode', 'phone_number'])
            writer.writerows(customers)
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
    else:
        print(f"Customer data has been exported to '{name}'.")

    print("Press 'Enter' key to continue...")
    sys.stdin.read(1)


