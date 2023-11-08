from random import randint
from utils import message
from utils.validator import Validator
import numpy as np
import csv
import os


class Customer:
    customers = np.array([])

    @classmethod
    def add(cls):
        print(message.add_customer_title)

        customer_id = str(randint(100000, 999999))
        name = Validator.validate_name()
        postcode = Validator.validate_postcode()
        phone_number = Validator.validate_phone_number()

        customer_record = [customer_id, name, postcode, phone_number]

        if len(cls.customers) == 0:
            cls.customers = np.array([customer_record])
        else:
            # Append the customer_record to the customers
            cls.customers = np.vstack((cls.customers, customer_record))

        print(f"{message.success_alert}Customer with ID {customer_id} saved successfully.\n")

        exit_confirmation("Do you want to add another customer? (yes/no): ", "add")

    @classmethod
    def search(cls):
        print(message.search_customer_title)

        search_results = []

        search_term = input("Enter either customer id, name, postcode or phone number: ").lower()

        for customer in cls.customers:
            for data in customer:
                if search_term in data:
                    search_results.append({
                        'customer_id': customer[0],
                        'name': customer[1],
                        'postcode': customer[2],
                        'phone_number': customer[3]
                    })

        if search_results:
            print(message.search_result)
            for customer in search_results:
                print("Customer ID   :", customer['customer_id'])
                print("Customer Name :", customer['name'])
                print("Postcode      :", customer['postcode'])
                print("Phone Number  :", customer['phone_number'])
                print("+-------------------------------------------+\n")

        else:
            print(f"{message.status_404}\n- Customer record for search key '{search_term}' not found.\n")

        exit_confirmation("Do you want to search another customer? (yes/no): ", 'search')

    @classmethod
    def delete(cls, transactions):
        from q3.transaction import Transaction

        print(message.delete_customer_title)

        customer_id = Validator.validate_customer_id()

        if str(customer_id) in cls.customers[:, 0]:
            cls.customers = cls.customers[cls.customers[:, 0] != str(customer_id)]

            if str(customer_id) in transactions[:, 1]:
                Transaction.transactions = transactions[transactions[:, 1] != str(customer_id)]
        else:
            print(f"{message.status_404}\n- Customer with ID '{customer_id}' not found.\n")

        exit_confirmation("Do you want to delete another customer? (yes/no): ", 'delete')

    @classmethod
    def load_from_csv(cls):
        print(message.load_customer_title)

        id_already_exist = []

        csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row if it exists
                for row in reader:
                    customer_id, name, postcode, phone_number = row
                    if customer_id not in [customer[0] for customer in cls.customers]:
                        customer_record = [customer_id, name, postcode, phone_number]
                        if len(cls.customers) == 0:
                            cls.customers = np.array([customer_record])
                        else:
                            cls.customers = np.vstack((cls.customers, customer_record))
                    else:
                        id_already_exist.append(customer_id)
        except FileNotFoundError:
            print(f"- {csv_file} not found")
            exit_confirmation("Do you want to try again? (yes/no): ", 'load_csv')
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print(f"{message.success_alert}- Customer records from CSV imported successfully.")
            if id_already_exist:
                print(f"- Except for following Customer ID {id_already_exist}.")
                print("- These customer id already exist.\n")

            input("- Press 'Enter' key to continue...")

    @classmethod
    def save_to_csv(cls):
        print(message.save_customer_title)

        if cls.customers.size > 0:
            csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

            if os.path.exists(csv_file):
                print(message.overwrite_title)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_csv_file_name = Validator.validate_csv_file("Enter new CSV file name (required): ")
                        write_csv_file(new_csv_file_name, cls.customers)
                        return
                    elif choice == '2':
                        write_csv_file(csv_file, cls.customers)
                        return
                    elif choice == '3':
                        print("- Operation canceled.\n")
                        input("- Press 'Enter' key to continue...")
                        return
                    else:
                        print(f"{message.error_title}\n- Invalid option selected. Try again!\n")
            else:
                write_csv_file(csv_file, cls.customers)

        else:
            print(f"{message.error_title}\n- No customers to export.")
            input("- Press 'Enter' key to continue...")


def write_csv_file(name, customers):
    with open(name, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['customer_id', 'name', 'postcode', 'phone_number'])
        writer.writerows(customers)

    print(f"{message.success_alert}- Data has been written to '{name}'.")
    input("- Press 'Enter' key to continue...")


def exit_confirmation(prompt, fn):
    from q3.q3_main import show_menu
    from q3.transaction import Transaction

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
