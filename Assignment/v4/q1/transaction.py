from random import randint
from utils.validator import Validator
from utils.helper import Helper
from utils import message


class Transaction:
    transactions = []

    def add(self, customers):
        print(message.add_transaction_title)

        customer_id = Validator.validate_customer_id()

        if Helper.check_if_customer_exist(customer_id, customers):
            self.transactions.append({
                "transaction_id": randint(100000, 999999),
                "customer_id": customer_id,
                "transaction_date": Validator.validate_transaction_date(),
                "product_category": Validator.validate_product_category(),
                "sales_value": Validator.validate_sales_value()
            })

            print(f"{message.success_alert}- Transaction for Customer ID {customer_id} saved successfully.\n")

            exit_confirmation("Do you want to add another transaction? (yes/no): ", 'add')

        exit_confirmation("Do you want to search another transaction? (yes/no): ", 'add')

    def search(self):
        print(message.search_transaction_title)

        search_key = input("Enter either customer id, date, category or sales value: ").lower()

        search_result = [
            transaction for transaction in self.transactions
            if any(search_key in str(value) for value in transaction.values())
        ]

        if search_result:
            print(message.search_result)
            for transaction in search_result:
                print(f"Transaction ID   : {transaction['transaction_id']}")
                print(f"Customer ID      : {transaction['customer_id']}")
                print(f"Product Category : {transaction['product_category'].title()}")
                print(f"Transaction Date : {transaction['transaction_date']}")
                print(f"Sales Value      : ${transaction['sales_value']}")
                print("+-------------------------------------------+\n")

        else:
            print(f"{message.status_404}\n- Transaction records for search key '{search_key}' not found.\n")

        exit_confirmation("Do you want to search another transaction? (yes/no): ", 'search')

    def show_customer_transactions(self, customers):
        print(message.search_customer_transaction_title)

        customer_id = Validator.validate_customer_id()

        search_result = []

        customer_ids = set(customer["customer_id"] for customer in customers)

        if customer_id not in customer_ids:
            print(f"{message.status_404}\n- Customer with ID '{customer_id}' not found.\n")

        else:
            for transaction in self.transactions:
                if str(customer_id) in str(transaction["customer_id"]):
                    search_result.append(transaction)

            if len(search_result) > 0:
                print(message.search_result)
                for transaction in search_result:
                    print(f"Transaction ID   : {transaction['transaction_id']}")
                    print(f"Product Category : {transaction['product_category'].title()}")
                    print(f"Transaction Date : {transaction['transaction_date']}")
                    print(f"Sales Value      : ${transaction['sales_value']}")
                    print("+-------------------------------------------+\n")

            else:
                print(f"{message.status_404}\n- No transactions found for Customer ID {customer_id}.\n")

        exit_confirmation("Do you want to search another transaction? (yes/no): ", 'show_customer_transactions')

    def delete(self):
        print(message.delete_transaction_title)

        transaction_id = Validator.validate_transaction_id()

        transaction_to_delete = [
            transaction for transaction in self.transactions
            if transaction["transaction_id"] == transaction_id
        ]

        if transaction_to_delete:
            for transaction in transaction_to_delete:
                self.transactions.remove(transaction)
            print(f"{message.success_alert}- Transaction with ID '{transaction_id}' deleted successfully.\n")
        else:
            print(f"{message.status_404}\n- Transaction ID '{transaction_id}' not found.\n")

        exit_confirmation("Do you want to delete another transaction? (yes/no): ", 'delete')


def exit_confirmation(prompt, fn):
    from q1.q1_main import show_menu
    from q1.customer import Customer

    transaction_obj = Transaction()
    customer_obj = Customer()

    while True:
        choice = input(prompt).lower()

        if choice == 'yes':
            if fn == 'add':
                transaction_obj.add(customer_obj.customers)
            elif fn == 'search':
                transaction_obj.search()
            elif fn == 'show_customer_transactions':
                transaction_obj.show_customer_transactions(customer_obj.customers)
            else:
                transaction_obj.delete()

        elif choice == 'no':
            show_menu()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")
