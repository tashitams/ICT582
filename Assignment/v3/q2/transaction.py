import csv
import os
from random import randint


class Transaction:
    transactions = []

    def add_transaction(self, customer_id, date, category, value):
        transaction_id = str(randint(1, 10000))
        transaction = {
            'date': date,
            'transaction_id': transaction_id,
            'customer_id': customer_id,
            'category': category,
            'value': value
        }
        self.transactions.append(transaction)

        print(f"\nTransaction for Customer ID {customer_id} saved successfully.\n")

    def search_transactions(self, search_string):
        result = []
        for transaction in self.transactions:
            if (search_string in transaction['transaction_id'] or
                    search_string in transaction['date'] or
                    search_string in transaction['customer_id'] or
                    search_string in transaction['category'] or
                    search_string in transaction['value']):
                result.append(transaction)

        if result:
            print("+---------------------------------------+")
            print("|       Transaction search results      |")
            print("+---------------------------------------+")

            display_search_result(result)

        else:
            print(f"No transaction found for search term '{search_string}'.\n")

    def show_customer_transaction(self, customer_id):
        result = []
        for transaction in self.transactions:
            if customer_id in transaction['customer_id']:
                result.append(transaction)

        if result:
            print("+---------------------------------------+")
            print("|      Customer transaction results     |")
            print("+---------------------------------------+")

            display_search_result(result)

        else:
            print(f"No transaction found for customer id '{customer_id}'.\n")

    def delete_transaction(self, transaction_id):
        delete_flag = False
        for transaction in self.transactions:
            if transaction['transaction_id'] == transaction_id:
                self.transactions.remove(transaction)
                delete_flag = True
                break
        if delete_flag:
            print(f"Transaction for id {transaction_id} deleted successfully. \n")
        else:
            print(f"No transaction found for {transaction_id}. \n")

    def load_transaction_from_csv(self, customer_ids, csv_file):
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

                        transaction = {
                            'date': row['date'],
                            'transaction_id': transaction_id,
                            'customer_id': customer_id,
                            'category': row['category'],
                            'value': float(row['value'])
                        }
                        self.transactions.append(transaction)

        except FileNotFoundError:
            print(f"Sorry but '{csv_file}' was not found.")
        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Transaction records load successfully. \n")

    def save_transaction_to_csv(self, csv_file):
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
                        save_the_file(new_file_name, self.transactions)
                        break
                    case '2':
                        save_the_file(csv_file, self.transactions)
                        break
                    case '3':
                        print("Operation canceled.")
                        break
                    case _:
                        print("Invalid option selected. Try again!")

        else:
            save_the_file(csv_file, self.transactions)


def display_search_result(result):
    for transaction in result:
        print(f"Transaction ID  : {transaction['transaction_id']}")
        print(f"Customer ID     : {transaction['customer_id']}")
        print(f"Date            : {transaction['date']}")
        print(f"Category        : {transaction['category'].title()}")
        print(f"Sales Value     : {transaction['value']}")
        print("+=======================================+ \n")


def save_the_file(file_name, data):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
            column_names = ['date', 'transaction_id', 'customer_id', 'category', 'value']
            csv_writer = csv.DictWriter(file, fieldnames=column_names)

            csv_writer.writeheader()

            for row in data:
                csv_writer.writerow(row)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Transaction data saved to '{file_name}' successfully.")


def validate_csv_file():
    while True:
        csv_file = input("Enter a csv file path (required): ")

        if not csv_file:
            print("CSV file path is required!")
        elif not csv_file.endswith('.csv'):
            print("File path you provided doesn't end in '.csv'.")
        else:
            return csv_file
