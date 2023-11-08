from random import randint
from utils import message
from utils.validator import Validator
import numpy as np

class Customer:
    customers = []

    def add(self):
        print(message.add_customer_title)

        customer_id = randint(100000, 999999)

        self.customers.append({
            "customer_id": customer_id,
            "name": Validator.validate_name(),
            "postcode": Validator.validate_postcode(),
            "phone_number": Validator.validate_phone_number()
        })

        print(f"{message.success_alert}Customer with ID {customer_id} saved successfully.\n")

        exit_confirmation("Do you want to add another customer? (yes/no): ", "add")

    def search(self):
        print(message.search_customer_title)

        search_key = input("Enter either customer id, name, postcode or phone number: ").lower()

        search_result = [
            customer for customer in self.customers
            if any(search_key in str(value) for value in customer.values())
        ]

        if search_result:
            print(message.search_result)
            for customer in search_result:
                print(f"Customer ID   : {customer['customer_id']}")
                print(f"Customer Name : {customer['name'].title()}")
                print(f"Postcode      : {customer['postcode']}")
                print(f"Phone Number  : {customer['phone_number']}")
                print("+-------------------------------------------+\n")

        else:
            print(f"{message.status_404}\n- Customer record for search key '{search_key}' not found.\n")

        exit_confirmation("Do you want to search another customer? (yes/no): ", 'search')

    def delete(self, transactions):
        from q1.transaction import Transaction

        print(message.delete_customer_title)

        customer_id = Validator.validate_customer_id()

        customer_ids = set(customer["customer_id"] for customer in self.customers)

        if customer_id not in customer_ids:
            print(f"{message.status_404}\n- Customer with ID '{customer_id}' not found.\n")

        else:
            for customer in self.customers:
                if customer['customer_id'] == customer_id:
                    self.customers.remove(customer)

            print(f"{message.success_alert}- Customer with ID '{customer_id}' deleted successfully.\n")

            transaction_customer_ids = set(transaction["customer_id"] for transaction in transactions)

            if customer_id in transaction_customer_ids:
                for transaction in Transaction.transactions:
                    if transaction['customer_id'] == customer_id:
                        Transaction.transactions.remove(transaction)

                print(f"{message.success_alert}- Transaction for Customer ID '{customer_id}' deleted successfully.\n")

        exit_confirmation("Do you want to delete another customer? (yes/no): ", 'delete')


def exit_confirmation(prompt, fn):
    from q1.q1_main import show_menu
    from q1.transaction import Transaction

    customer_obj = Customer()
    transaction_obj = Transaction()

    while True:
        choice = input(prompt).lower()

        if choice == 'yes':
            if fn == 'add':
                customer_obj.add()
            elif fn == 'search':
                customer_obj.search()
            else:
                customer_obj.delete(transaction_obj.transactions)

        elif choice == 'no':
            show_menu()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")
