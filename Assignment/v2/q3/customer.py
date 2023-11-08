import csv
import os
from random import randint
import numpy as np


class Customer:
    customers = np.array([])

    def add_customer(self):
        customer_id = str(randint(100000, 999999))
        name = validate_name("Enter customer name (required): ")
        postcode = validate_postcode("Enter postcode (optional): ")
        phone_number = validate_phone_number("Enter phone_number (optional): ")

        customer_record = [customer_id, name, postcode, phone_number]

        if len(self.customers) == 0:
            self.customers = np.array([customer_record])
        else:
            self.customers = np.vstack((self.customers, customer_record))

        print(f"\nSuccess: Customer with id '{customer_id} saved successfully.")
        input("Press 'Enter' key to continue...")

    def search_customers(self):
        search_result = []
        search_term = input("Enter your search term: ")

        for customer in self.customers:
            customer_id, name, postcode, phone_number = map(str, customer)

            if (
                    search_term in customer_id or
                    search_term in name or
                    search_term in postcode or
                    search_term in phone_number
            ):
                search_result.append(customer)

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
            print(f"No customer found for search term '{search_term}'.\n")
        input("Press 'Enter' key to continue...")

    def delete_customer(self):
        from transaction import Transaction

        customer_id = validate_customer_id("Enter customer id to delete: ")

        customer_to_delete = np.where(self.customers[:, 0] == customer_id)

        if customer_to_delete[0].size > 0:
            np.delete(self.customers, customer_to_delete, axis=0)

            transaction_to_delete = np.where(Transaction.transactions[:, 1] == customer_id)

            if transaction_to_delete[0].size > 0:
                Transaction.transactions = Transaction.transactions[Transaction.transactions[:, 2] != customer_id]

            print(f"\nCustomer with ID {customer_id} and related transactions deleted successfully.")
        else:
            print(f"Customer with ID {customer_id} not found.")
        input("Press 'Enter' key to continue...")

    def import_customer_from_csv(self):
        csv_file = validate_csv_file("Enter CSV file name (required): ")

        if self.customers.size > 0:
            customer_ids = set(self.customers[:, 0])
        else:
            customer_ids = set()

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    customer_id, name, postcode, phone_number = row
                    if customer_id not in customer_ids:
                        customer_record = [customer_id, name, postcode, phone_number]

                        if self.customers.size == 0:
                            self.customers = np.array(customer_record)
                        else:
                            self.customers = np.vstack((self.customers, customer_record))
        except FileNotFoundError:
            print(f"- {csv_file} not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Customer records from CSV file imported successfully.")
        input("Press 'Enter' key to continue...")

    def export_customer_to_csv(self):
        if np.size(self.customers) == 0:
            print("Oops: No customer record to export.")
            print("Try adding some customer records first.\n")
            input("Press 'Enter' key to continue...")
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
            writer = csv.writer(file)
            writer.writerow(['customer_id', 'name', 'postcode', 'phone_number'])
            writer.writerows(customers)
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
    while True:
        name = input(prompt).lower()
        if not name:
            print("Warning: Customer name is required. \n")
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
