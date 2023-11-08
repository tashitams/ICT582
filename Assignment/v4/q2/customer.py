from random import randint
from utils import message
from utils.validator import Validator
import csv
import os


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

    def load_from_csv(self):
        print(message.load_customer_title)

        customer_ids = set(customer["customer_id"] for customer in self.customers)

        id_already_exist = []

        csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    customer_id = int(row['customer_id'])
                    if customer_id not in customer_ids:
                        self.customers.append({
                            "customer_id": customer_id,
                            "name": row['name'],
                            "postcode": row['postcode'],
                            "phone_number": row['phone_number']
                        })
                    else:
                        id_already_exist.append(customer_id)
        except FileNotFoundError:
            print(f"- {csv_file} not found")
            exit_confirmation("Do you want to try again? (yes/no): ", 'load_csv')
        except Exception as e:
            print(f"Error: An error occurred: {e}")
        else:
            print(f"{message.success_alert}- Customer records from CSV imported successfully.")
            if id_already_exist:
                print(f"- Except for following Customer ID {id_already_exist}.")
                print("- These customer id already exist.\n")

            input("- Press 'Enter' key to continue...")

    def save_to_csv(self):
        print(message.save_customer_title)

        if not self.customers:
            print(f"{message.error_title}\n- No customers to export.")
            input("- Press 'Enter' key to continue...")

        else:
            csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

            if os.path.exists(csv_file):
                print(message.overwrite_title)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_csv_file_name = Validator.validate_csv_file("Enter new CSV file name (required): ")
                        write_csv_file(new_csv_file_name, self.customers)
                        return
                    elif choice == '2':
                        write_csv_file(csv_file, self.customers)
                        return
                    elif choice == '3':
                        print("- Operation canceled.\n")
                        input("- Press 'Enter' key to continue...")
                        return
                    else:
                        print(f"{message.error_title}\n- Invalid option selected. Try again!\n")
            else:
                write_csv_file(csv_file, self.customers)


def write_csv_file(name, customers):
    with open(name, 'w', newline='', encoding='utf-8-sig') as file:
        field_names = customers[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=field_names)

        # Write the header row
        csv_writer.writeheader()

        for row in customers:
            csv_writer.writerow(row)
    print(f"{message.success_alert}- Data has been written to '{name}'.")
    input("- Press 'Enter' key to continue...")

def exit_confirmation(prompt, fn):
    from q2.q2_main import show_menu
    from q2.transaction import Transaction

    customer_obj = Customer()
    transaction_obj = Transaction()

    while True:
        choice = input(prompt).lower()

        if choice == 'yes':
            if fn == 'add':
                customer_obj.add()
            elif fn == 'search':
                customer_obj.search()
            elif fn == 'load_csv':
                return customer_obj.load_from_csv()
            else:
                customer_obj.delete(transaction_obj.transactions)

        elif choice == 'no':
            show_menu()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")
