import csv
import os
import sys
from random import randint
import validator

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


class Transaction:
    transactions = []

    def add(self, customers):
        print("+---------------------------------------+")
        print("|           Add transactions            |")
        print("+---------------------------------------+")

        customer_id = validator.validate_customer_id("Enter customer ID (required): ")

        customer = next((
            customer for customer in customers
            if customer['customer_id'] == customer_id), None
        )

        if customer:
            self.transactions.append({
                'transaction_id': str(randint(100000, 999999)),
                'customer_id': customer_id,
                'date': validator.validate_date("Enter transaction date (YYYY-MM-DD): "),
                'category': validator.validate_category("Enter product category (required): "),
                'value': validator.validate_value("Enter value (required): ")
            })
            print(f"Transaction added successfully for customer id {customer_id}.")
        else:
            print(f"Customer with customer id {customer_id} does not exist.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def search(self):
        print("+---------------------------------------+")
        print("|         Search transactions           |")
        print("+---------------------------------------+")

        search_key = input("Enter customer id, date, category or value: ")

        search_result = []

        for transaction in self.transactions:
            if (search_key == transaction['customer_id'] or
                    search_key == transaction['date'] or
                    search_key.lower() in transaction['category'] or
                    search_key == transaction['value']):
                search_result.append(transaction)

        if search_result:
            print("+---------------------------------------+")
            print("|      Transaction search results       |")
            print("+---------------------------------------+")
            for transaction in search_result:
                print(f"Transaction ID   : {transaction['transaction_id']}")
                print(f"Customer ID      : {transaction['customer_id']}")
                print(f"Transaction Date : {transaction['date']}")
                print(f"Product Category : {transaction['category'].title()}")
                print(f"Sales Value      : {transaction['value']}")
                print("------------------------------------------ \n")
        else:
            print(f"No transaction found for search term '{search_key}'.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def display_transactions_for_customer(self):
        print("+---------------------------------------+")
        print("|     Display customer transactions     |")
        print("+---------------------------------------+")

        customer_id = validator.validate_customer_id("Enter customer ID (required): ")
        customer_transaction = []

        for transaction in self.transactions:
            if customer_id == transaction['customer_id']:
                customer_transaction.append(transaction)

        if customer_transaction:
            print("+---------------------------------------+")
            print(f"|           Customer ID {customer_id}         |")
            print("+---------------------------------------+")
            for transaction in customer_transaction:
                print(f"Transaction ID : {transaction['transaction_id']}")
                print(f"Transaction Date : {transaction['date']}")
                print(f"Product Category : {transaction['category'].title()}")
                print(f"Sales Value      : {transaction['value']}")
                print("------------------------------------------ \n")

        else:
            print(f"No transaction found for customer id '{customer_id}'.\n")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def delete(self):
        print("+---------------------------------------+")
        print("|          Delete transaction           |")
        print("+---------------------------------------+")

        delete_flag = False

        transaction_id = validator.validate_transaction_id("Enter transaction id to delete: ")

        for transaction in self.transactions:
            if transaction_id == transaction['transaction_id']:
                self.transactions.remove(transaction)
                delete_flag = True
                break

        if delete_flag:
            print(f"Transaction with id {transaction_id} deleted successfully.")
        else:
            print(f"No transaction for id {transaction_id} found.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def load_transaction_from_csv(self, customers):
        print("+---------------------------------------+")
        print("|    Load transaction from CSV file     |")
        print("+---------------------------------------+")

        csv_file = validator.validate_csv_file("Enter csv file path (required): ")

        customer_ids = set(customer["customer_id"] for customer in customers)

        transaction_ids = set(transaction["transaction_id"] for transaction in self.transactions)

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    customer_id = row['customer_id']
                    transaction_id = row['transaction_id']

                    if customer_id in customer_ids:
                        if transaction_id in transaction_ids:
                            transaction_id = str(randint(100000, 999999))

                        self.transactions.append({
                            'date': row['date'],
                            'transaction_id': transaction_id,
                            'customer_id': customer_id,
                            'category': row['category'],
                            'value': float(row['value'])
                        })
        except FileNotFoundError:
            print(f"{csv_file} not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Transaction records from CSV file loaded successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def save_transaction_to_csv(self):
        print("+---------------------------------------+")
        print("|     Save transaction to CSV file      |")
        print("+---------------------------------------+")

        if not self.transactions:
            print("There is no transaction records to export.")

        else:
            csv_file = validator.validate_csv_file("Enter CSV file path (required): ")

            if os.path.isfile(csv_file):

                print(file_exist_warning)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_file_name = validator.validate_csv_file("Enter new csv file path (required): ")
                        save_to_csv_file(new_file_name, self.transactions)
                        break

                    elif choice == '2':
                        save_to_csv_file(csv_file, self.transactions)
                        break

                    elif choice == '3':
                        print("Operation canceled.")
                        input("Press 'Enter' key to continue...")
                        break

                    else:
                        print("Invalid option selected. Try again!")

            else:
                save_to_csv_file(csv_file, self.transactions)


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