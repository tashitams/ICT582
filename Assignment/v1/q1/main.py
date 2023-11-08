import sys
from customer import Customer
from transaction import Transaction

program_menu = """
+----------------- Program Menu -----------------+
|                                                |
|   Press 1   :  Add a new customer              |
|   Press 2   :  Add a new transaction           |
|   Press 3   :  Search customers                |
|   Press 4   :  Search transactions             |
|   Press 5   :  Display customer transactions   |
|   Press 6   :  Delete a transaction            |
|   Press 7   :  Delete a customer               |
|   Press 8   :  Quit                            |
|                                                |
+--------------- Select an option  --------------+
"""

def main():
    customer = Customer()
    transaction = Transaction()

    while True:
        print(program_menu)

        

        choice = input("Enter your choice: ")

        if choice == '1':
            customer.add()

        elif choice == '2':
            transaction.add(customer.customers)

        elif choice == '3':
            customer.search()

        elif choice == '4':
            transaction.search()

        elif choice == '5':
            transaction.display_transactions_for_customer()

        elif choice == '6':
            transaction.delete()

        elif choice == '7':
            customer.delete()

        elif choice == '8':
            sys.exit("Program terminated successfully.")

        else:
            print("Invalid choice. Please try again.")
            print("Press 'Enter' key to continue...")
            sys.stdin.read(1)


if __name__ == "__main__":
    main()
