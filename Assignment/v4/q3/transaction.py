from random import randint
from matplotlib import pyplot as plt
from utils import message
from utils.validator import Validator
import csv
import os
import numpy as np


class Transaction:
    transactions = np.array([])

    # Map month numbers to month names
    month_names = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    @classmethod
    def add(cls, customers):
        print(message.add_transaction_title)

        if len(customers) > 0:
            customer_id = Validator.validate_customer_id()

            if str(customer_id) in customers[:, 0]:
                date = Validator.validate_transaction_date()
                transaction_id = str(randint(100000, 999999))
                customer_id = str(customer_id)
                category = Validator.validate_product_category()
                value = Validator.validate_sales_value()

                transaction_record = [date, transaction_id, customer_id, category, value]

                if len(cls.transactions) == 0:
                    cls.transactions = np.array([transaction_record])
                else:
                    cls.transactions = np.vstack((cls.transactions, transaction_record))

                print(f"{message.success_alert}- Transaction for Customer ID {customer_id} saved successfully.\n")

            else:
                print(f"Customer ID {customer_id} doesn't exist.")

            exit_confirmation("Do you want to add another transaction? (yes/no): ", 'add')

        else:
            print(f"{message.status_404}\n- No customers found.")
            input("- Press 'Enter' key to continue...")

    @classmethod
    def search(cls):
        print(message.search_transaction_title)

        search_term = input("Enter either customer id, date, category or sales value: ").lower()

        search_results = []

        for transaction in cls.transactions:
            for data in transaction:
                if search_term in data:
                    search_results.append({
                        'transaction_id': transaction[1],
                        'customer_id': transaction[2],
                        'date': transaction[0],
                        'category': transaction[3],
                        'value': transaction[4]
                    })

        if search_results:
            print(message.search_result)
            for transaction in search_results:
                print(f"Transaction ID   : {transaction['transaction_id']}")
                print(f"Customer ID      : {transaction['customer_id']}")
                print(f"Product Category : {transaction['category'].title()}")
                print(f"Transaction Date : {transaction['date']}")
                print(f"Sales Value      : ${transaction['value']}")
                print("+-------------------------------------------+\n")

        else:
            print(f"{message.status_404}\n- Transaction records for search key '{search_term}' not found.\n")

        exit_confirmation("Do you want to search another transaction? (yes/no): ", 'search')

    @classmethod
    def show_customer_transactions(cls, customers):
        print(message.search_customer_transaction_title)

        customer_id = Validator.validate_customer_id()

        if str(customer_id) in customers[:, 0]:
            customer_transactions = cls.transactions[cls.transactions[:, 2] == customer_id]

            if customer_transactions.size > 0:
                print(message.search_result)
                for transaction in customer_transactions:
                    print(f"Transaction ID   : {transaction[1]}")
                    print(f"Transaction Date : {transaction[0]}")
                    print(f"Product Category : {transaction[3].title()}")
                    print(f"Sales Value      : ${transaction[4]}")
                    print("+-------------------------------------------+\n")
            else:
                print(f"{message.status_404}\n- No transactions found for Customer ID {customer_id}.\n")
        else:
            print(f"{message.status_404}\n- Customer ID {customer_id} doesn't exist.\n")

        exit_confirmation("Do you want to search another transaction? (yes/no): ", 'show_customer_transactions')

    @classmethod
    def delete(cls):
        print(message.delete_transaction_title)

        transaction_id = Validator.validate_transaction_id()

        if str(transaction_id) in cls.transactions[:, 0]:
            cls.transactions = cls.transactions[cls.transactions[:, 0] != str(transaction_id)]
            print(f"{message.success_alert}- Transaction with ID '{transaction_id}' deleted successfully.\n")
        else:
            print(f"{message.status_404}\n- Transaction ID '{transaction_id}' not found.\n")

        exit_confirmation("Do you want to delete another transaction? (yes/no): ", 'delete')

    @classmethod
    def load_from_csv(cls, customers):
        print(message.load_transaction_title)

        csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

        if np.size(customers) == 0:
            print(f"{message.status_404}\n- No customer records found.")
            print("- Try adding some customer records first.")
            input("- Press 'Enter' key to continue...")

        else:
            try:
                with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row if it exists

                    for row in reader:
                        date, transaction_id, customer_id, category, value = row

                        if customer_id in customers[:, 0]:
                            transaction_record = [
                                date,
                                transaction_id,
                                customer_id,
                                category,
                                value
                            ]

                            if len(cls.transactions) == 0:
                                cls.transactions = np.array([transaction_record])
                            else:
                                cls.transactions = np.vstack((cls.transactions, transaction_record))
                        else:
                            print(f"{message.status_404}\n- Customer ID {customer_id} doesn't exist.\n")
            except FileNotFoundError:
                print(f"- {csv_file} not found")
                exit_confirmation("Do you want to try again? (yes/no): ", 'load_csv')
            except Exception as e:
                print(f"An error occurred: {e}")
            else:
                print(f"{message.success_alert}- Transaction records from CSV imported successfully.")
                input("- Press 'Enter' key to continue...")

    @classmethod
    def save_to_csv(cls):
        print(message.save_transaction_title)

        if cls.transactions.size > 0:
            csv_file = Validator.validate_csv_file("Enter CSV file name (required): ")

            if os.path.exists(csv_file):
                print(message.overwrite_title)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_csv_file_name = Validator.validate_csv_file("Enter new CSV file name (required): ")
                        write_csv_file(new_csv_file_name, cls.transactions)
                        return
                    elif choice == '2':
                        write_csv_file(csv_file, cls.transactions)
                        return
                    elif choice == '3':
                        print("- Operation canceled.\n")
                        input("- Press 'Enter' key to continue...")
                        return
                    else:
                        print(f"{message.error_title}\n- Invalid option selected. Try again!\n")
            else:
                write_csv_file(csv_file, cls.transactions)

        else:
            print(f"{message.error_title}\n- No transactions to export.")
            input("- Press 'Enter' key to continue...")

    @classmethod
    def monthly_sales_report(cls):
        print(message.monthly_sales_report_title)

        sorted_data = np.argsort(cls.transactions[:, 0])
        transactions = cls.transactions[sorted_data]

        # Extract month from the transaction date
        # Extract month and year from the transaction date
        transaction_dates = transactions[:, 0]
        values = transactions[:, -1].astype(float)

        # Create a dictionary to store monthly sales and transaction counts
        monthly_data = {}

        for date, value in zip(transaction_dates, values):
            month = date.split('-')[1]
            if month not in monthly_data:
                monthly_data[month] = {'sales_value': 0.0, 'transaction_count': 0}
            monthly_data[month]['sales_value'] += value
            monthly_data[month]['transaction_count'] += 1

        # Sort and extract month names
        sorted_month_names = sorted(monthly_data.keys())
        sorted_sales_values = [monthly_data[month]['sales_value'] for month in sorted_month_names]
        sorted_transaction_numbers = [monthly_data[month]['transaction_count'] for month in sorted_month_names]

        # Replace month numbers with month names for the x-axis labels
        sorted_month_names = [cls.month_names[month] for month in sorted_month_names]

        # Create a line graph
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_month_names, sorted_sales_values, marker='o', label='Sales Value')
        plt.plot(sorted_month_names, sorted_transaction_numbers, marker='o', label='Transaction Numbers')
        plt.title('Monthly Sales and Transaction Numbers')
        plt.xlabel('Month')
        plt.ylabel('Value / Number')
        plt.legend()
        plt.grid(True)
        plt.show()

    @classmethod
    def customer_sales_report(cls):
        print(message.customer_sales_report_title)
        customer_id = Validator.validate_customer_id()

        customer_transactions = cls.transactions[cls.transactions[:, 2] == str(customer_id)]

        if customer_transactions.size == 0:
            print(f"No data found for customer with ID {customer_id}")

        # Sort transactions by date
        sorted_indices = np.argsort(customer_transactions[:, 0])
        customer_transactions = customer_transactions[sorted_indices]

        # Extract dates, values, and transaction IDs from customer transactions
        transaction_dates = customer_transactions[:, 0]
        values = customer_transactions[:, -1].astype(float)
        transaction_ids = customer_transactions[:, 1]

        # Create a dictionary to store monthly sales and transaction counts
        monthly_data = {}

        for date, value, transaction_id in zip(transaction_dates, values, transaction_ids):
            month = date.split('-')[1]
            if month not in monthly_data:
                monthly_data[month] = {'sales_value': 0.0, 'transaction_count': 0}
            monthly_data[month]['sales_value'] += value
            monthly_data[month]['transaction_count'] += 1

        # Sort and extract month names
        sorted_month_names = sorted(monthly_data.keys())
        sorted_sales_values = [monthly_data[month]['sales_value'] for month in sorted_month_names]
        sorted_transaction_numbers = [monthly_data[month]['transaction_count'] for month in sorted_month_names]

        # Replace month numbers with month names for the x-axis labels
        sorted_month_names = [cls.month_names[month] for month in sorted_month_names]

        # Create a line graph
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_month_names, sorted_sales_values, marker='o', label='Sales Value')
        plt.plot(sorted_month_names, sorted_transaction_numbers, marker='o', label='Transaction Numbers')
        plt.title(f'Monthly Sales and Transaction Numbers for Customer {customer_id}')
        plt.xlabel('Month')
        plt.ylabel('Number')
        plt.legend()
        plt.grid(True)
        plt.show()

        exit_confirmation("Do you want to show report for another customer ID? (yes/no): ", 'customer_sales_report')

    @classmethod
    def customer_postcode_report(cls, customers):
        print(message.customer_postcode_report_title)

        postcode = Validator.validate_postcode()

        # Extract customer IDs from customers_in_that_postcode
        customers_in_that_postcode = customers[customers[:, 2] == postcode]

        if customers_in_that_postcode.size == 0:
            print(f"No customers found in the postcode area {postcode}")

        else:
            # Extract customer IDs from customers
            customer_ids = customers_in_that_postcode[:, 0]

            # Filter transactions for the matching customer IDs
            postcode_transactions = cls.transactions[np.isin(cls.transactions[:, 2], customer_ids)]

            if postcode_transactions.size == 0:
                print(f"No data found for customers in the postcode area {postcode}")

            else:
                # Sort transactions by date
                sorted_indices = np.argsort(postcode_transactions[:, 0])
                postcode_transactions = postcode_transactions[sorted_indices]

                # Extract dates and values from postcode transactions
                transaction_dates = postcode_transactions[:, 0]
                values = postcode_transactions[:, -1].astype(float)

                # Create a dictionary to store monthly sales and transaction counts
                monthly_data = {}

                for date, value in zip(transaction_dates, values):
                    month = date.split('-')[1]
                    if month not in monthly_data:
                        monthly_data[month] = {'sales_value': 0.0, 'transaction_count': 0}
                    monthly_data[month]['sales_value'] += value
                    monthly_data[month]['transaction_count'] += 1

                # Sort and extract month names
                sorted_month_names = sorted(monthly_data.keys())
                sorted_sales_values = [monthly_data[month]['sales_value'] for month in sorted_month_names]
                sorted_transaction_numbers = [monthly_data[month]['transaction_count'] for month in sorted_month_names]

                # Replace month numbers with month names for the x-axis labels
                sorted_month_names = [cls.month_names[month] for month in sorted_month_names]

                # Create a line graph
                plt.figure(figsize=(10, 6))
                plt.plot(sorted_month_names, sorted_sales_values, marker='o', label='Sales Value')
                plt.plot(sorted_month_names, sorted_transaction_numbers, marker='o', label='Transaction Numbers')
                plt.title(f'Monthly Sales and Transaction Numbers for Postcode Area {postcode}')
                plt.xlabel('Month')
                plt.ylabel('Value / Number')
                plt.legend()
                plt.grid(True)
                plt.show()

        exit_confirmation("Do you want to show report for another postcode? (yes/no): ", 'customer_postcode_report')


def write_csv_file(name, transactions):
    with open(name, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['transaction_id', 'customer_id', 'product_category', 'transaction_date', 'sales_value'])
        writer.writerows(transactions)

    print(f"{message.success_alert}- Data has been written to '{name}'.")
    input("- Press 'Enter' key to continue...")

def exit_confirmation(prompt, fn):
    from q3.q3_main import show_menu
    from q3.customer import Customer

    while True:
        choice = input(prompt).lower()

        if choice == 'yes':
            if fn == 'add':
                Transaction.add(Customer.customers)
            elif fn == 'search':
                Transaction.search()
            elif fn == 'show_customer_transactions':
                Transaction.show_customer_transactions(Customer.customers)
            elif fn == 'load_csv':
                return Transaction.load_from_csv(Customer.customers)
            elif fn == 'customer_sales_report':
                Transaction.customer_sales_report()
            elif fn == 'customer_postcode_report':
                Transaction.customer_postcode_report(Customer.customers)
            else:
                Transaction.delete()

        elif choice == 'no':
            show_menu()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")
