from random import randint


class Transaction:
    transactions = []

    def add_transaction(self, customer_id, date, category, value):
        transaction_id = str(randint(1, 10000))
        transaction = {
            'date': date,
            'transaction_id': transaction_id,
            'customer_id': customer_id,
            'category': category,
            'value': value
        }
        self.transactions.append(transaction)

        print(f"\nTransaction for Customer ID {customer_id} saved successfully.\n")

    def search_transactions(self, search_string):
        result = []
        for transaction in self.transactions:
            if (search_string in transaction['transaction_id'] or
                    search_string in transaction['date'] or
                    search_string in transaction['customer_id'] or
                    search_string in transaction['category'] or
                    search_string in transaction['value']):
                result.append(transaction)

        if result:
            print("+---------------------------------------+")
            print("|       Transaction search results      |")
            print("+---------------------------------------+")

            display_search_result(result)

        else:
            print(f"No transaction found for search term '{search_string}'.\n")

    def show_customer_transaction(self, customer_id):
        result = []
        for transaction in self.transactions:
            if customer_id in transaction['customer_id']:
                result.append(transaction)

        if result:
            print("+---------------------------------------+")
            print("|      Customer transaction results     |")
            print("+---------------------------------------+")

            display_search_result(result)

        else:
            print(f"No transaction found for customer id '{customer_id}'.\n")

    def delete_transaction(self, transaction_id):
        delete_flag = False
        for transaction in self.transactions:
            if transaction['transaction_id'] == transaction_id:
                self.transactions.remove(transaction)
                delete_flag = True
                break
        if delete_flag:
            print(f"Transaction for id {transaction_id} deleted successfully. \n")
        else:
            print(f"No transaction found for {transaction_id}. \n")

def display_search_result(result):
    for transaction in result:
        print(f"Transaction ID  : {transaction['transaction_id']}")
        print(f"Customer ID     : {transaction['customer_id']}")
        print(f"Date            : {transaction['date']}")
        print(f"Category        : {transaction['category'].title()}")
        print(f"Sales Value     : {transaction['value']}")
        print("+---------------------------------------+ \n")