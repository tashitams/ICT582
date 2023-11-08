import sys
from random import randint
import validator

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
                'category':  validator.validate_category("Enter product category (required): "),
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
            print(f"----- Customer ID {customer_id} -----")
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
