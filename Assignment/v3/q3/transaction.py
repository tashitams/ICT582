import csv
import os
from random import randint

import numpy as np
from matplotlib import pyplot as plt


class Transaction:
    # Create an empty NumPy structured array
    transactions = np.array([])

    # Map month numbers to month names
    month_names = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    def add_transaction(self, customer_id, date, category, value):
        transaction_id = str(randint(100000, 999999))

        transaction = [date, transaction_id, customer_id, category, value]

        if self.transactions.size == 0:
            self.transactions = np.array([transaction])
        else:
            self.transactions = np.vstack((self.transactions, transaction))

        print(f"\nTransaction record with ID '{transaction_id}' saved successfully.\n")

    def search_transactions(self, search_term):
        search_result = [
            transaction for transaction in self.transactions
            if search_term in ' '.join(map(str, transaction))
        ]

        if search_result:
            print("+---------------------------------------+")
            print("|      Transaction search results       |")
            print("+---------------------------------------+")
            display_search_result(search_result)
        else:
            print(f"No transaction found for search term '{search_term}'.\n")

    def show_customer_transaction(self, customer_id):
        search_result = np.where(self.transactions[:, 2] == customer_id)

        if search_result:
            print("+---------------------------------------+")
            print("|  Customer transaction search results  |")
            print("+---------------------------------------+")
            display_search_result(search_result)
        else:
            print(f"\nNo transaction found for customer id '{customer_id}'.")

    def delete_transaction(self, transaction_id):
        transaction_to_delete = np.where(self.transactions[:, 1] == transaction_id)

        if len(transaction_to_delete) > 0:
            self.transactions = np.delete(self.transactions, transaction_to_delete, axis=0)
            print(f"\nTransaction with ID '{transaction_id}' deleted successfully.")
        else:
            print(f"\nTransaction with ID '{transaction_id}' not found.")

    def load_transaction_from_csv(self, customer_ids, csv_file):
        if len(self.transactions) > 0:
            transaction_ids = set(self.transactions[:, 1])

        else:
            transaction_ids = set()

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    date, transaction_id, customer_id, category, value = row

                    if customer_id in customer_ids:
                        if transaction_id in transaction_ids:
                            transaction_id = str(randint(100000, 999999))

                        transaction = np.array([date, transaction_id, customer_id, category, value])

                        if self.transactions.size == 0:
                            self.transactions = np.array([transaction])
                        else:
                            self.transactions = np.vstack((self.transactions, transaction))

        except FileNotFoundError:
            print(f"- {csv_file} not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Transaction records from CSV file imported successfully.")

    def save_transaction_to_csv(self, csv_file):
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
                        save_to_csv_file(new_file_name, self.transactions)
                        break
                    case '2':
                        save_to_csv_file(csv_file, self.transactions)
                        break
                    case '3':
                        print("Operation canceled.")
                        break
                    case _:
                        print("Invalid option selected. Try again!")

        else:
            save_to_csv_file(csv_file, self.transactions)

    def plot_monthly_sales_and_transactions(self):
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

    def plot_customer_monthly_sales_and_transactions(self):
        customer_id = validate_customer_id()

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

    def plot_postcode_monthly_sales_and_transactions(self, customers):
        postcode = validate_postcode()

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


def display_search_result(result):
    for transaction in result:
        print(f"Transaction ID  : {transaction[1]}")
        print(f"Customer ID     : {transaction[2]}")
        print(f"Date            : {transaction[0]}")
        print(f"Category        : {transaction[3].title()}")
        print(f"Sales Value     : {transaction[4]}")
        print("+=======================================+ \n")

def validate_customer_id():
    while True:
        try:
            customer_id = int(input("Enter customer ID: "))
        except ValueError:
            print("Customer ID is invalid, try again!")
        else:
            return str(customer_id)

def validate_csv_file():
    while True:
        csv_file = input("Enter a csv file path (required): ")

        if not csv_file:
            print("CSV file path is required!")
        elif not csv_file.endswith('.csv'):
            print("File path you provided doesn't end in '.csv'. \n")
        else:
            return csv_file

def validate_postcode():
    while True:
        postcode = input("Enter customer's postcode (required): ")
        if not postcode:
            print("Postcode is required.")
        if postcode:
            if len(postcode) != 4 and not postcode.isdigit():
                print("Postcode should be 4 digit in length.")
            else:
                return postcode

def save_to_csv_file(name, transactions):
    try:
        with open(name, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'transaction_id', 'customer_id', 'category', 'value'])
            writer.writerows(transactions)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Transaction data saved to '{name}' successfully. \n")
