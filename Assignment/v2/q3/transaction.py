import csv
import os
from datetime import datetime
from random import randint
import numpy as np
from matplotlib import pyplot as plt


class Transaction:
    transactions = np.array([])

    # Map month numbers to month names
    month_names = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    def add_transaction(self, customers):
        customer_id = validate_customer_id("Enter customer ID (required): ")

        if customer_id not in customers[:, 0]:
            print(f"Warning: Customer with ID {customer_id} doesn't exist.")
        else:
            transaction_id = str(randint(100000, 999999))
            date = validate_date("Enter transaction date in the format YYYY-MM-DD: ")
            category = validate_category("Enter product category (required): ")
            value = validate_value("Enter value (required): ")
            transaction_record = [date, transaction_id, customer_id, category, value]

            if len(self.transactions) == 0:
                self.transactions = np.array([transaction_record])
            else:
                self.transactions = np.vstack((self.transactions, transaction_record))

            print(f"Success: Transaction added successfully for customer id {customer_id}. \n")

        input("Press 'Enter' key to continue...")

    def search_transactions(self):
        search_result = []
        search_term = input("Enter your search term: ")

        for transaction in self.transactions:
            date, transaction_id, customer_id, category, value = transaction

            if (
                    search_term in customer_id or
                    search_term in date or
                    search_term in category or
                    search_term in value
            ):
                search_result.append(transaction)

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
            print(f"\nNo transaction found for search term '{search_term}'.")
        input("Press 'Enter' key to continue...")

    def display_transactions_for_customer(self):
        customer_transaction = []
        customer_id = validate_customer_id("Enter customer ID (required): ")

        for transaction in self.transactions:
            tr_customer_id = map(str, transaction)
            if customer_id in tr_customer_id:
                customer_transaction.append(transaction)

        if customer_transaction:
            print("+---------------------------------------+")
            print("|     Customer transaction results      |")
            print("+---------------------------------------+")
            for transaction in customer_transaction:
                print(f"Transaction ID   : {transaction[0]}")
                print(f"Customer ID      : {transaction[1]}")
                print(f"Transaction Date : {transaction[2]}")
                print(f"Product Category : {transaction[3].title()}")
                print(f"Sales Value      : {transaction[4]}")
                print("------------------------------------------ \n")
        else:
            print(f"\nNo transaction found for customer id '{customer_id}'.")
        input("Press 'Enter' key to continue...")

    def delete_transaction(self):
        transaction_id = validate_transaction_id("Enter transaction ID (required): ")
        transaction_to_delete = np.where(self.transactions[:, 1] == transaction_id)

        if transaction_to_delete[0].size > 0:
            self.transactions = np.delete(self.transactions, transaction_to_delete, axis=0)
            print(f"\nTransaction with ID {transaction_id} deleted successfully.")
        else:
            print(f"\nTransaction with ID {transaction_id} not found.")
        input("Press 'Enter' key to continue...")

    def import_transaction_from_csv(self, customers):
        csv_file = validate_csv_file("Enter CSV file name (required): ")

        if self.transactions.size > 0:
            transaction_ids = set(self.transactions[:, 0])
        else:
            transaction_ids = set()

        if customers.size > 0:
            customer_ids = set(customers[:, 0])
        else:
            customer_ids = set()

        try:
            with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    date, transaction_id, customer_id, category, value = row

                    if customer_id in customer_ids:
                        if transaction_id in transaction_ids:
                            transaction_id = str(randint(100000, 999999))
                        transaction_record = [date, transaction_id, customer_id, category, value]
                        if self.transactions.size == 0:
                            self.transactions = np.array(transaction_record)
                        else:
                            self.transactions = np.vstack((self.transactions, transaction_record))

        except FileNotFoundError:
            print(f"- {csv_file} not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print("Transaction records from CSV file imported successfully.")
        input("Press 'Enter' key to continue...")

    def export_transaction_to_csv(self):
        if np.size(self.transactions) == 0:
            print("Oops: No transaction record to export.")
            print("Try adding some transaction records first.\n")
            input("Press 'Enter' key to continue...")
        else:
            csv_file = validate_csv_file("Enter CSV file name (required): ")

            if os.path.isfile(csv_file):
                print(f"\nWARNING: {csv_file} already exist.")
                print("Press 1: Change the file name")
                print("Press 2: Overwrite the file")
                print("Press 3: Cancel the operation \n")

                while True:
                    choice = input("Please select your option: ")
                    if choice == '1':
                        new_file_name = validate_csv_file("Enter new CSV file name (required): ")
                        export(new_file_name, self.transactions)
                        return

                    elif choice == '2':
                        export(csv_file, self.transactions)
                        return

                    elif choice == '3':
                        print("Operation canceled. \n")
                        input("Press 'Enter' key to continue...")
                        break

                    else:
                        print("Invalid option selected. Try again! \n")

            else:
                export(csv_file, self.transactions)

    def display_monthly_sales_and_transactions(self):
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

    def display_customer_monthly_sales_and_transactions(self):
        customer_id = validate_customer_id("Enter customer ID (required): ")

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

    def display_postcode_monthly_sales_and_transactions(self, customers):
        postcode = validate_postcode("Enter postcode: ")

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


def validate_csv_file(prompt):
    while True:
        file_path = input(prompt).lower()

        if not file_path:
            print("CSV file name is required! \n")
        elif not file_path.endswith('.csv'):
            print("Invalid file format. Please provide a CSV file. \n")
        else:
            return file_path


def validate_postcode(prompt):
    while True:
        postcode = input(prompt)
        if not postcode:
            return postcode

        if postcode:
            if not postcode.isdigit():
                print("Warning: Postcode must be a number between 0000-9999. \n")
            elif len(postcode) != 4:
                print("Warning: Postcode must be 4 digits in length. \n")
            else:
                return postcode
