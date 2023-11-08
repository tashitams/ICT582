from customer import Customer
from transaction import Transaction

def main():
    print("+------------------------------------+")
    print("|      Western Wholesales Pty Ltd    |")
    print("+------------------------------------+")
    print()

    while True:
        print("------------ Program Menu ------------\n")

        print("1. Add a new customer")
        print("2. Add a new transaction")
        print("3. Search customers")
        print("4. Search transactions")
        print("5. Display transactions for a customer")
        print("6. Delete a transaction")
        print("7. Delete a customer")
        print("8. Quit \n")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer.add_customer()

        elif choice == '2':
            transaction.add_transaction(customer.customers)

        elif choice == '3':
            customer.search_customers()

        elif choice == '4':
            transaction.search_transactions()

        elif choice == '5':
            transaction.display_transactions_for_customer()

        elif choice == '6':
            transaction.delete_transaction()

        elif choice == '7':
            customer.delete_customer()

        elif choice == '8':
            print("Program terminated successfully.")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press 'Enter' key to continue...")


if __name__ == "__main__":
    customer = Customer()
    transaction = Transaction()
    main()
