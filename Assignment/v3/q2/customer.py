import csv
import os
from random import randint
from transaction import Transaction


class Customer:
    customers = []

    def add_customer(self, name, postcode='', phone_number=''):
        customer_id = str(randint(1, 10000))
        customer = {
            'customer_id': customer_id,
            'name': name,
            'postcode': postcode,
            'phone_number': phone_number
        }
        self.customers.append(customer)

        print(f"\nCustomer record with ID {customer_id} saved successfully.\n")

    def search_customers(self, search_string):
        result = []
        for customer in self.customers:
            if (search_string in customer['customer_id'] or
                    search_string in customer['name'].lower() or
                    search_string in customer['postcode'] or
                    search_string in customer['phone_number']):
                result.append(customer)

        if result:
            print("+---------------------------------------+")
            print("|       Customer search results         |")
            print("+---------------------------------------+")

            for customer in result:
                print(f"Customer ID   : {customer['customer_id']}")
                print(f"Customer Name : {customer['name'].title()}")
                print(f"Postcode      : {customer['postcode']}")
                print(f"Phone Number  : {customer['phone_number']}")
                print("+=======================================+ \n")
        else:
            print(f"No customer found for search term '{search_string}'.\n")

    def delete_customer(self, customer_id):
        delete_flag = False
        for customer in self.customers:
            if customer_id == customer['customer_id']:
                self.customers.remove(customer)
                delete_customer_transactions(customer_id)
                delete_flag = True

        if delete_flag:
            print(f"Customer with id {customer_id} deleted successfully.\n")
        else:
            print(f"No customer for id {customer_id} found. \n")

    def load_customer_from_csv(self, csv_file):
        customer_ids = set(customer["customer_id"] for customer in self.customers)

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    customer_id = row['customer_id']
                    if customer_id not in customer_ids:
                        customer = {
                            'customer_id': customer_id,
                            'name': row['name'].lower(),
                            'postcode': row['postcode'],
                            'phone_number': row['phone_number']
                        }
                        self.customers.append(customer)
        except FileNotFoundError:
            print(f"Sorry but '{csv_file}' was not found. \n")
        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Customer records load successfully. \n")

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
                        save_the_file(new_file_name, self.customers)
                        break
                    case '2':
                        save_the_file(csv_file, self.customers)
                        break
                    case '3':
                        print("Operation canceled.")
                        break
                    case _:
                        print("Invalid option selected. Try again!")

        else:
            save_the_file(csv_file, self.customers)


def check_if_customer_transaction_exist(customer_id):
    customer_ids = [transaction['customer_id'] for transaction in Transaction.transactions]
    if customer_id in customer_ids:
        return True
    else:
        return False


def delete_customer_transactions(customer_id):
    if check_if_customer_transaction_exist(customer_id):
        for transaction in Transaction.transactions:
            if customer_id == transaction['customer_id']:
                Transaction.transactions.remove(transaction)


def validate_csv_file():
    while True:
        csv_file = input("Enter a csv file path (required): ")

        if not csv_file:
            print("CSV file path is required!")
        elif not csv_file.endswith('.csv'):
            print("File path you provided doesn't end in '.csv'. \n")
        else:
            return csv_file


def save_the_file(file_name, data):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
            column_names = ['customer_id', 'name', 'postcode', 'phone_number']
            csv_writer = csv.DictWriter(file, fieldnames=column_names)

            csv_writer.writeheader()

            for row in data:
                csv_writer.writerow(row)
    except Exception as e:
        print(f"Error: {e}")

    else:
        print(f"Customer data saved to '{file_name}' successfully. \n")
