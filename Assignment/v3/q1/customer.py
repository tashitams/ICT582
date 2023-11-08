from random import randint
from transaction import Transaction


class Customer:
    customers = []

    def add_customer(self, name, postcode='', phone_number=''):
        customer_id = str(randint(1, 10000))
        customer = {
            'customer_id': customer_id,
            'name': name,
            'postcode': postcode,
            'phone_number': phone_number
        }
        self.customers.append(customer)

        print(f"\nCustomer record with ID {customer_id} saved successfully.\n")

    def search_customers(self, search_string):
        result = []
        for customer in self.customers:
            if (search_string in customer['customer_id'] or
                    search_string in customer['name'].lower() or
                    search_string in customer['postcode'] or
                    search_string in customer['phone_number']):
                result.append(customer)

        if result:
            print("+---------------------------------------+")
            print("|       Customer search results         |")
            print("+---------------------------------------+")

            for customer in result:
                print(f"Customer ID   : {customer['customer_id']}")
                print(f"Customer Name : {customer['name'].title()}")
                print(f"Postcode      : {customer['postcode']}")
                print(f"Phone Number  : {customer['phone_number']}")
                print("+---------------------------------------+ \n")
        else:
            print(f"No customer found for search term '{search_string}'.\n")

    def delete_customer(self, customer_id):
        delete_flag = False
        for customer in self.customers:
            if customer_id == customer['customer_id']:
                self.customers.remove(customer)
                delete_customer_transactions(customer_id)
                delete_flag = True

        if delete_flag:
            print(f"Customer with id {customer_id} deleted successfully.\n")
        else:
            print(f"No customer for id {customer_id} found. \n")

def check_if_customer_transaction_exist(customer_id):
    customer_ids = [transaction['customer_id'] for transaction in Transaction.transactions]
    if customer_id in customer_ids:
        return True
    else:
        return False

def delete_customer_transactions(customer_id):
    if check_if_customer_transaction_exist(customer_id):
        for transaction in Transaction.transactions:
            if customer_id == transaction['customer_id']:
                Transaction.transactions.remove(transaction)


