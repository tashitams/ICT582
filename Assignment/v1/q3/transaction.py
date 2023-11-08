import csv
import os
import sys

import validator
from random import randint
import numpy as np
from matplotlib import pyplot as plt

file_exist_warning = """
+----------------- WARNING -----------------+
|          The file already exist.          |
|                                           |
|  Press 1: Change the file name            |
|  Press 2: Overwrite the file              |
|  Press 3: Cancel the operation            |
+-------------------------------------------+

+------------ Select an option  ------------+
"""

class Transaction:
    transactions = np.empty((0, 5))

    # Map month numbers to month names
    month_names = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    def add(self, customers):
        print("+---------------------------------------+")
        print("|           Add transactions            |")
        print("+---------------------------------------+")

        customer_id = validator.validate_customer_id("Enter customer ID (required): ")

        customer_ids = set(customers[:, 0])

        if customer_id not in customer_ids:
            print(f"Customer with ID {customer_id} doesn't exist.")
        else:
            date = validator.validate_date("Enter transaction date (YYYY-MM-DD): ")
            transaction_id = str(randint(100000, 999999))
            category = validator.validate_category("Enter product category (required): ")
            value = validator.validate_value("Enter value (required): ")

            transaction_record = np.array([date, transaction_id, customer_id, category, value])

            self.transactions = np.append(self.transactions, [transaction_record], axis=0)

            print(f"Transaction saved successfully for customer id {customer_id}.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def search(self):
        print("+---------------------------------------+")
        print("|         Search transactions           |")
        print("+---------------------------------------+")

        search_term = input("Enter customer id, date, category or value: ")

        search_result = [
            transaction for transaction in self.transactions
            if any(search_term in str(value) for value in transaction)
        ]

        if search_result:
            print("+---------------------------------------+")
            print("|      Transaction search results       |")
            print("+---------------------------------------+")
            for transaction in search_result:
                print(f"Transaction ID   : {transaction[1]}")
                print(f"Customer ID      : {transaction[2]}")
                print(f"Transaction Date : {transaction[0]}")
                print(f"Product Category : {transaction[3].title()}")
                print(f"Sales Value      : {transaction[4]}")
                print("------------------------------------------ \n")
        else:
            print(f"No transaction found for search term '{search_term}'.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def display_transactions_for_customer(self):
        print("+---------------------------------------+")
        print("|     Display customer transactions     |")
        print("+---------------------------------------+")

        customer_id = validator.validate_customer_id("Enter customer ID (required): ")

        data = (self.transactions[:, 2] == customer_id)

        customer_transaction = self.transactions[data]

        if customer_transaction:
            print("+---------------------------------------+")
            print("|     Customer transaction results      |")
            print("+---------------------------------------+")
            for transaction in customer_transaction:
                date, transaction_id, customer_id, category, value = transaction
                print("Customer ID       :", customer_id)
                print("Transaction ID    :", transaction_id)
                print("Transaction Date  :", date)
                print("Product Category  :", category.title())
                print("Sales Value       :", value)
                print("------------------------------------------ \n")
        else:
            print(f"No transaction found for customer id '{customer_id}'.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def delete(self):
        print("+---------------------------------------+")
        print("|          Delete transaction           |")
        print("+---------------------------------------+")

        transaction_id = validator.validate_transaction_id("Enter transaction ID (required): ")

        transaction_array = len(self.transactions)

        data = (self.transactions[:, 1] != transaction_id)

        transaction_to_delete = self.transactions[data]

        if len(transaction_to_delete) < transaction_array:
            print(f"Transaction with ID {transaction_id} deleted successfully.")
        else:
            print(f"Transaction with ID {transaction_id} not found.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def load_transaction_from_csv(self, customers):
        print("+---------------------------------------+")
        print("|    Load transaction from CSV file     |")
        print("+---------------------------------------+")

        csv_file = validator.validate_csv_file("Enter CSV file path (required): ")

        customer_ids = set(customers[:, 0])
        transaction_ids = set(self.transactions[:, 1])

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    date, transaction_id, customer_id, category, value = row

                    if customer_id in customer_ids:
                        if transaction_id in transaction_ids:
                            transaction_id = str(randint(100000, 999999))

                        transaction_record = np.array([date, transaction_id, customer_id, category, value])
                        self.transactions = np.append(self.transactions, [transaction_record], axis=0)

        except FileNotFoundError:
            print(f"- {csv_file} not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Transaction records from CSV file imported successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def save_transaction_to_csv(self):
        print("+---------------------------------------+")
        print("|     Save transaction to CSV file      |")
        print("+---------------------------------------+")

        if np.size(self.transactions) == 0:
            print("There is no transaction record to save.")

        else:
            csv_file = validator.validate_csv_file("Enter CSV file path (required): ")

            if os.path.isfile(csv_file):
                print(file_exist_warning)

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_file_name = validator.validate_csv_file("Enter new csv file path (required): ")
                        save_to_csv_file(new_file_name, self.transactions)
                        break

                    elif choice == '2':
                        save_to_csv_file(csv_file, self.transactions)
                        break

                    elif choice == '3':
                        print("Operation canceled.")
                        input("Press 'Enter' key to continue...")
                        break

                    else:
                        print("Invalid option selected. Try again!")
            else:
                save_to_csv_file(csv_file, self.transactions)

    def monthly_sales_and_transaction_report(self):
        # Sort transactions by date
        sorted_data = np.argsort(self.transactions[:, 0])
        transactions = self.transactions[sorted_data]

        # Extract dates and values from transactions
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
        sorted_month_names = [self.month_names[month] for month in sorted_month_names]

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

    def customer_monthly_sales_and_transaction_report(self):
        customer_id = validator.validate_customer_id("Enter customer ID (required): ")

        customer_transactions = self.transactions[self.transactions[:, 2] == customer_id]

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
        sorted_month_names = [self.month_names[month] for month in sorted_month_names]

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

    def postcode_monthly_sales_and_transaction_report(self, customers):
        postcode = validator.validate_postcode("Enter postcode: ")

        # Extract customer IDs from customers_in_that_postcode
        customers_in_that_postcode = customers[customers[:, 2] == postcode]

        if customers_in_that_postcode.size == 0:
            print(f"No customers found in the postcode area {postcode}")

        else:
            # Extract customer IDs from customers
            customer_ids = customers_in_that_postcode[:, 0]

            # Filter transactions for the matching customer IDs
            postcode_transactions = self.transactions[np.isin(self.transactions[:, 2], customer_ids)]

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
                sorted_month_names = [self.month_names[month] for month in sorted_month_names]

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


def export(name, transactions):
    try:
        with open(name, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'transaction_id', 'customer_id', 'category', 'value'])
            writer.writerows(transactions)
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

    else:
        print(f"Transaction data has been exported to '{name}' successfully.")
    input("Press 'Enter' key to continue...")

def save_to_csv_file(name, transactions):
    try:
        with open(name, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'transaction_id', 'customer_id', 'category', 'value'])
            writer.writerows(transactions)
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
    else:
        print(f"Transaction data has been exported to '{name}'.")

    print("Press 'Enter' key to continue...")
    sys.stdin.read(1)
