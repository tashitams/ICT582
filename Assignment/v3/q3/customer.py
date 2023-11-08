import csv
import os
from random import randint

import numpy as np


class Customer:
    # Create an empty NumPy structured array
    customers = np.array([])

    def add_customer(self, name, postcode='', phone_number=''):
        customer_id = str(randint(100000, 999999))

        customer = [customer_id, name, postcode, phone_number]

        if self.customers.size == 0:
            self.customers = np.array([customer])
        else:
            self.customers = np.vstack((self.customers, customer))

        print(f"\nCustomer record with ID '{customer_id}' saved successfully.\n")

    def search_customers(self, search_term):
        search_result = [
            customer for customer in self.customers
            if search_term in ' '.join(map(str, customer))
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
            print(f"No customer found for search term '{search_term}'.\n")

    def delete_customer(self, customer_id):
        from transaction import Transaction

        customer = np.where(self.customers[:, 0] == customer_id)

        if len(customer) > 0:
            self.customers = np.delete(self.customers, customer, axis=0)
            print(f"Customer with ID '{customer_id}' and related transactions deleted successfully. \n")

            transaction = np.where(Transaction.transactions[:, 2] == customer_id)

            if len(transaction) > 0:
                Transaction.transactions = np.delete(Transaction.transactions, transaction, axis=0)
                print(f"Customer with ID '{customer_id}' and related transactions deleted successfully. \n")
            else:
                print(f"Customer with ID '{customer_id}' deleted successfully.")
                print("No transactions found \n")
        else:
            print(f"Customer with ID '{customer_id}' not found. \n")

    def load_customer_from_csv(self, csv_file):

        if len(self.customers) > 0:
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
                        customer = [customer_id, name, postcode, phone_number]
                        if self.customers.size == 0:
                            self.customers = np.array([customer])
                        else:
                            self.customers = np.vstack((self.customers, customer))
        except FileNotFoundError:
            print(f"Sorry but '{csv_file}' was not found.")

        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Customer records from CSV file loaded successfully.")

    def save_customer_to_csv(self, csv_file):
        if os.path.isfile(csv_file):

            print("+---------- The file already exist ----------+")
            print("|                                            |")
            print("|  Press 1: Change the file name             |")
            print("|  Press 2: Overwrite the file               |")
            print("|  Press 3: Cancel the operation             |")
            print("+--------------------------------------------+")

            while True:
                option = input("Select your option: ")
                match option:
                    case '1':
                        new_file_name = validate_csv_file()
                        save_to_csv_file(new_file_name, self.customers)
                        break
                    case '2':
                        save_to_csv_file(csv_file, self.customers)
                        break
                    case '3':
                        print("Operation canceled.")
                        break
                    case _:
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
        print(f"Error: {e}")
    else:
        print(f"Customer data saved to '{name}' successfully. \n")


def validate_csv_file():
    while True:
        csv_file = input("Enter a csv file path (required): ")

        if not csv_file:
            print("CSV file path is required!")
        elif not csv_file.endswith('.csv'):
            print("File path you provided doesn't end in '.csv'. \n")
        else:
            return csv_file
