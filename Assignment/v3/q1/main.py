from datetime import datetime
from customer import Customer
from transaction import Transaction

category_list = """
+ ---------- Select a category ----------+
1. Food
2. Alcohol and Beverage
3. Apparel
4. furniture
5. Household Appliances
6. Computer Equipment
"""


class SalesManagement:
    def __init__(self):
        self.customer = Customer()
        self.transaction = Transaction()

    def check_if_customer_exist(self, customer_id):
        customer_ids = [customer['customer_id'] for customer in self.customer.customers]
        if customer_id in customer_ids:
            return True
        else:
            return False

    def main(self):

        categories = [
            "food",
            "alcohol and beverage",
            "apparel",
            "furniture",
            "household appliances",
            "computer equipment"
        ]

        while True:
            print("===============================================")
            print("|           Question 1: Program Menu          |")
            print("===============================================\n")
            print("1. Add a new customer")
            print("2. Add a new transaction for a customer")
            print("3. Search for customers")
            print("4. Search for transactions")
            print("5. Display transactions for a customer")
            print("6. Delete a transaction")
            print("7. Delete a customer")
            print("8. Quit \n")

            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    name = input("Enter customer's name (required): ")
                    if not name:
                        print("Customer's name is required")
                    else:
                        break

                while True:
                    postcode = input("Enter customer's postcode (optional): ")
                    if not postcode:
                        break
                    if postcode:
                        if len(postcode) == 4 and postcode.isdigit():
                            break
                        else:
                            print("Invalid postcode entered")

                while True:
                    phone_number = input("Enter customer's phone number (optional): ")
                    if not phone_number:
                        break
                    if phone_number:
                        if phone_number.isdigit() and phone_number.startswith('04'):
                            break
                        else:
                            print("Invalid phone number, phone number starts with 04")

                self.customer.add_customer(name, postcode, phone_number)

            elif choice == '2':
                customer_id = validate_customer_id()

                if self.check_if_customer_exist(customer_id):
                    while True:
                        date = input("Enter transaction date (YYYY-MM-DD): ")

                        try:
                            datetime.strptime(date, '%Y-%m-%d')
                        except ValueError:
                            print("Transaction date is invalid. Try again. \n")
                        else:
                            if datetime.strptime(date, '%Y-%m-%d') < datetime.today():
                                break
                            print("Date in future not allowed. \n")

                    while True:
                        print(category_list)

                        category = input("Enter transaction category: ").lower()

                        if not category:
                            print(f"Category is required. \n")
                        elif category not in categories:
                            print("Choose a category from the available option. \n")
                        else:
                            break

                    value = input("Enter transaction value: ")

                    self.transaction.add_transaction(customer_id, date, category, value)

                else:
                    print(f"Customer with ID {customer_id} not found.")

            elif choice == '3':
                search_key = input("Enter your search key: ")
                self.customer.search_customers(search_key)

            elif choice == '4':
                search_key = input("Enter your search key: ")
                self.transaction.search_transactions(search_key)

            elif choice == '5':
                customer_id = validate_customer_id()

                if self.check_if_customer_exist(customer_id):
                    self.transaction.show_customer_transaction(customer_id)

                else:
                    print(f"No customer found for ID {customer_id}. \n")

            elif choice == '6':
                transaction_id = validate_transaction_id()
                self.transaction.delete_transaction(transaction_id)

            elif choice == '7':
                customer_id = validate_customer_id()
                if self.check_if_customer_exist(customer_id):
                    self.customer.delete_customer(customer_id)

                else:
                    print(f"No customer found for ID {customer_id}.")

            elif choice == '8':
                print("Program terminated successfully.")
                break

            else:
                print("Invalid choice. Please select a valid option. \n")


def validate_customer_id():
    while True:
        try:
            customer_id = int(input("Enter customer ID: "))
        except ValueError:
            print("Invalid Customer ID entered.")
        else:
            return str(customer_id)

def validate_transaction_id():
    while True:
        try:
            transaction_id = int(input("Enter transaction ID: "))
        except ValueError:
            print("Invalid Transaction ID entered.")
        else:
            return str(transaction_id)


if __name__ == "__main__":
    sales_system = SalesManagement()
    sales_system.main()
