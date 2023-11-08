import sys
import validator
from random import randint


class Customer:
    customers = []

    def add(self):
        print("+---------------------------------------+")
        print("|              Add customer             |")
        print("+---------------------------------------+")
        customer_id = str(randint(100000, 999999))

        self.customers.append({
            'customer_id': customer_id,
            'name': validator.validate_name("Enter customer name (required): "),
            'postcode': validator.validate_postcode("Enter postcode (optional): "),
            'phone_number': validator.validate_phone_number("Enter phone_number (optional): ")
        })

        print(f"Customer with id '{customer_id} saved successfully.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def search(self):
        print("+---------------------------------------+")
        print("|           Search customers            |")
        print("+---------------------------------------+")
        search_term = input("Search using customer's id, name, postcode or phone number: ")

        search_result = []

        for customer in self.customers:
            if (search_term == customer['customer_id'] or
                    search_term.lower() in customer['name'].lower() or
                    search_term == customer['postcode'] or
                    search_term == customer['phone_number']):
                search_result.append(customer)

        if search_result:
            print("+---------------------------------------+")
            print("|       Customer search results         |")
            print("+---------------------------------------+")

            for customer in search_result:
                print(f"Customer ID   : {customer['customer_id']}")
                print(f"Customer Name : {customer['name'].title()}")
                print(f"Postcode      : {customer['postcode']}")
                print(f"Phone Number  : {customer['phone_number']}")
                print("+---------------------------------------+ \n")
        else:
            print(f"No customer found for search term '{search_term}'.\n")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)

    def delete(self):
        print("+---------------------------------------+")
        print("|            Delete customer            |")
        print("+---------------------------------------+")
        delete_flag = False

        customer_id = validator.validate_customer_id("Enter customer id to delete: ")

        for customer in self.customers:
            if customer_id == customer['customer_id']:
                self.customers.remove(customer)
                remove_customer_transaction(customer_id)
                delete_flag = True
                break

        if delete_flag:
            print(f"Customer with id {customer_id} deleted successfully.")
        else:
            print(f"No customer for id {customer_id} found.")

        print("Press 'Enter' key to continue...")
        sys.stdin.read(1)


def remove_customer_transaction(customer_id):
    from transaction import Transaction

    Transaction.transactions = [
        transaction for transaction in Transaction.transactions
        if transaction['customer_id'] != customer_id
    ]
