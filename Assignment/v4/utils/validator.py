from datetime import datetime
from utils.helper import Helper
from utils import message
import re


class Validator:
    @staticmethod
    def validate_customer_id():
        while True:
            try:
                customer_id = int(input("Enter customer ID (required): "))

            except ValueError:
                print(f"{message.error_title}{message.customer_id_invalid}")

            else:
                return customer_id

    @staticmethod
    def validate_transaction_id():
        while True:
            try:
                transaction_id = int(input("Enter transaction ID (required): "))

            except ValueError:
                print(f"{message.error_title}{message.transaction_id_invalid}")

            else:
                return transaction_id

    @staticmethod
    def validate_name():
        while True:
            customer_name = input("Enter customer name (required): ").lower()

            name_pattern = r'^[a-zA-Z\s-]+$'

            if not customer_name:
                print(f"{message.error_title}\n- Customer name is required!\n")

            elif not re.match(name_pattern, customer_name):
                print(f"{message.error_title}{message.customer_name_invalid}")

            else:
                return customer_name

    @staticmethod
    def validate_postcode():
        while True:
            postcode = input("Enter customer postcode (optional): ")

            if not postcode:
                return postcode

            if postcode:
                if not postcode.isdigit():
                    print(f"{message.error_title}\n- Postcode must be number between 0000-9999.\n")

                elif len(postcode) != 4:
                    print(f"{message.error_title}\n- Postcode must be 4 digits in length.\n")

                else:
                    return postcode

    @staticmethod
    def validate_phone_number():
        while True:
            phone_number = input("Enter customer phone number (optional): ")

            if not phone_number:
                return phone_number

            if not phone_number.isdigit():
                print(f"{message.error_title}\n- Phone number must be number.\n")

            elif not len(phone_number) == 10:
                print(f"{message.error_title}\n- Phone number must be 10 digits in length.\n")

            elif not phone_number.startswith('04'):
                print(f"{message.error_title}\n- Phone number must start with 04.\n")

            else:
                return phone_number

    @staticmethod
    def validate_transaction_date():
        while True:
            transaction_date = input("Enter transaction date in the format YYYY-MM-DD: ")

            try:
                datetime.strptime(transaction_date, '%Y-%m-%d')

            except ValueError:
                print("Transaction date is invalid. Try again.\n")

            else:
                if datetime.strptime(transaction_date, '%Y-%m-%d') < datetime.today():
                    return transaction_date
                print(f"{message.error_title}\n- Future date is not allowed.\n")

    @staticmethod
    def validate_product_category():
        product_categories = [
            "food",
            "alcohol and beverage",
            "apparel",
            "furniture",
            "household appliances",
            "computer equipment"
        ]

        print(message.product_category)

        while True:

            product_category = input("Enter product category (required): ").lower()

            if not product_category:
                print(f"{message.error_title}\n- Product category is required.\n")

            elif product_category not in product_categories:
                print(f"{message.error_title}\n- Choose a category from the available option.\n")

            else:
                return product_category

    @staticmethod
    def validate_sales_value():
        while True:
            try:
                sales_value = float(input("Enter sales value (required): $"))

            except ValueError:
                print(f"{message.error_title}{message.sales_value_invalid}")

            else:
                if sales_value > 0:
                    return sales_value
                print(f"{message.error_title}\n- Sales value can't be in negative.\n")

    @staticmethod
    def validate_csv_file(prompt):
        while True:
            file_path = input(prompt).lower()

            if not file_path:
                print(f"{message.error_title}\n- CSV file name is required!\n")

            elif not file_path.endswith('.csv'):
                print(f"{message.error_title}\n- Invalid file format. Please provide a CSV file.\n")

            else:
                return file_path
