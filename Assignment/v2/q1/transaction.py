from datetime import datetime
from random import randint


class Transaction:
    transactions = []

    def add_transaction(self, customers):
        customer_id = validate_customer_id("Enter customer ID (required): ")

        # Find the customer with the given customer_id
        customer = next((
            customer for customer in customers
            if customer['customer_id'] == customer_id), None
        )

        if customer:
            transaction_id = str(randint(100000, 999999))
            date = validate_date("Enter transaction date in the format YYYY-MM-DD: ")
            category = validate_category("Enter product category (required): ")
            value = validate_value("Enter value (required): ")

            self.transactions.append({
                'date': date,
                'transaction_id': transaction_id,
                'customer_id': customer_id,
                'category': category,
                'value': value
            })
            print(f"\nSuccess: Transaction added successfully for customer id {customer_id}.")
        else:
            print(f"\nWarning: Customer with customer id {customer_id} does not exist.")
        input("Press 'Enter' key to continue...")

    def search_transactions(self):
        search_term = input("Enter your search term: ")

        search_result = [
            transaction for transaction in self.transactions if
            search_term == transaction['customer_id'] or
            search_term == transaction['date'] or
            search_term.lower() in transaction['category'] or
            search_term == transaction['value']
        ]

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
            print(f"\nNo transaction found for search term '{search_term}'.")

        input("Press 'Enter' key to continue...")

    def display_transactions_for_customer(self):
        customer_id = validate_customer_id("Enter customer ID (required): ")
        customer_transaction = []

        for transaction in self.transactions:
            if customer_id == transaction['customer_id']:
                customer_transaction.append(transaction)

        if customer_transaction:
            print(f"----- Transaction for Customer ID {customer_id} ----- \n")
            for transaction in customer_transaction:
                print(f"Transaction ID : {transaction['transaction_id']}")
                print(f"Transaction Date : {transaction['date']}")
                print(f"Product Category : {transaction['category'].title()}")
                print(f"Sales Value      : {transaction['value']}")
                print("------------------------------------------ \n")
        else:
            print(f"No transaction found for customer id '{customer_id}'.\n")

        input("Press 'Enter' key to continue...")

    def delete_transaction(self):
        transaction_deleted = False

        transaction_id = validate_transaction_id("Enter transaction id to delete: ")

        for transaction in self.transactions:
            if transaction_id == transaction['transaction_id']:
                self.transactions.remove(transaction)
                transaction_deleted = True
                break

        if transaction_deleted:
            print(f"\nSuccess: Transaction with id {transaction_id} deleted successfully.")
        else:
            print(f"\nInfo: No transaction for id {transaction_id} found.")
        input("Press 'Enter' key to continue...")


# validation methods
# ------------------
def validate_transaction_id(prompt):
    while True:
        transaction_id = input(prompt)

        if not transaction_id:
            print("Warning: Transaction id required. \n")

        if transaction_id:
            if not transaction_id.isdigit():
                print("Warning: Transaction id must be a number. \n")
            else:
                return transaction_id


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


def validate_date(prompt):
    while True:
        transaction_date = input(prompt)

        try:
            datetime.strptime(transaction_date, '%Y-%m-%d')
        except ValueError:
            print("Transaction date is invalid. Try again. \n")
        else:
            if datetime.strptime(transaction_date, '%Y-%m-%d') < datetime.today():
                return transaction_date
            print("Warning: Future date is not allowed. \n")


def validate_category(prompt):
    product_categories = [
        "food",
        "alcohol and beverage",
        "apparel",
        "furniture",
        "household appliances",
        "computer equipment"
    ]

    while True:
        product_category = input(prompt).lower()

        if not product_category:
            print(f"Warning: Category is required. \n")
        elif product_category not in product_categories:
            print("Warning: Choose a category from the available option. \n")
        else:
            return product_category


def validate_value(prompt):
    while True:
        try:
            sales_value = float(input(prompt))
        except ValueError:
            print(f"Warning: Invalid sales value. Only number allowed.")
        else:
            return str(sales_value)
