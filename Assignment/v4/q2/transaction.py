from random import randint
from utils import message
from utils.helper import Helper
from utils.validator import Validator
import csv
import os


class Transaction:
    transactions = []

    def add(self, customers):
        print(message.add_transaction_title)

        customer_id = Validator.validate_customer_id()

        if Helper.check_if_customer_exist(customer_id, customers):
            self.transactions.append({
                "date": Validator.validate_transaction_date(),
                "transaction_id": randint(100000, 999999),
                "customer_id": customer_id,
                "category": Validator.validate_product_category(),
                "value": Validator.validate_sales_value()
            })

            print(f"{message.success_alert}- Transaction for Customer ID {customer_id} saved successfully.\n")

        exit_confirmation("Do you want to add another transaction? (yes/no): ", 'add')

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
                print(f"Product Category : {transaction['category'].title()}")
                print(f"Transaction Date : {transaction['date']}")
                print(f"Sales Value      : ${transaction['value']}")
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
                    print(f"Product Category : {transaction['category'].title()}")
                    print(f"Transaction Date : {transaction['date']}")
                    print(f"Sales Value      : ${transaction['value']}")
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

    def load_from_csv(self, customers):
        print(message.load_transaction_title)

        customer_ids = set(customer["customer_id"] for customer in customers)

        transaction_ids = set(transaction["transaction_id"] for transaction in self.transactions)

        csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    customer_id = int(row['customer_id'])
                    transaction_id = int(row['transaction_id'])

                    if customer_id in customer_ids:
                        if transaction_id in transaction_ids:
                            transaction_id = randint(100000, 999999)

                        self.transactions.append({
                            'date': row['date'],
                            'transaction_id': transaction_id,
                            'customer_id': customer_id,
                            'category': row['category'],
                            'value': float(row['value'])
                        })

        except FileNotFoundError:
            print(f"- {csv_file} not found")
            exit_confirmation("Do you want to try again? (yes/no): ", 'load_csv')
        except Exception as e:
            print(f"Error: An error occurred: {e}")
        else:
            print(f"{message.success_alert}- Transaction records from CSV imported successfully.")
            input("- Press 'Enter' key to continue...")

    def save_to_csv(self):
        print(message.save_transaction_title)

        if not self.transactions:
            print(f"{message.error_title}\n- No transactions to export.")
            input("- Press 'Enter' key to continue...")

        else:
            csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

            if os.path.exists(csv_file):
                print(message.overwrite_title)

                while True:

                    choice = input("Please select your option: ")

                    if choice == '1':
                        new_csv_file_name = Validator.validate_csv_file("Enter new CSV file name (required): ")
                        write_csv_file(new_csv_file_name, self.transactions)
                        return
                    elif choice == '2':
                        write_csv_file(csv_file, self.transactions)
                        return
                    elif choice == '3':
                        print("- Operation canceled.\n")
                        input("- Press 'Enter' key to continue...")
                        return
                    else:
                        print(f"{message.error_title}\n-Invalid option selected. Try again!\n")
            else:
                write_csv_file(csv_file, self.transactions)

def write_csv_file(name, transactions):
    with open(name, 'w', newline='', encoding='utf-8-sig') as file:
        field_names = transactions[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=field_names)

        # Write the header row
        csv_writer.writeheader()

        for row in transactions:
            csv_writer.writerow(row)
    print(f"{message.success_alert}- Data has been written to '{name}'.")
    input("- Press 'Enter' key to continue...")

def exit_confirmation(prompt, fn):
    from q2.q2_main import show_menu
    from q2.customer import Customer

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
            elif fn == 'load_csv':
                return transaction_obj.load_from_csv(customer_obj.customers)
            else:
                transaction_obj.delete()

        elif choice == 'no':
            show_menu()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")



