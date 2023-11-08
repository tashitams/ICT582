from customer import Customer
from transaction import Transaction

def main():
    print("+------------------------------------+")
    print("|      Western Wholesales Pty Ltd    |")
    print("+------------------------------------+")

    while True:
        print("\n------------ Program Menu ------------\n")

        print("1. Add a new customer")
        print("2. Add a new transaction")
        print("3. Search customers")
        print("4. Search transactions")
        print("5. Display transactions for a customer")
        print("6. Delete a transaction")
        print("7. Delete a customer")
        print("8. Import customer from csv")
        print("9. Export customer to csv")
        print("10. Import transaction from csv")
        print("11. Export transaction to csv")
        print("12. Display monthly sales & transaction")
        print("13. Display customer monthly sales and transactions")
        print("14. Display given postcode's monthly sales and transactions")
        print("15. Quit \n")

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
            customer.import_customer_from_csv()

        elif choice == '9':
            customer.export_customer_to_csv()

        elif choice == '10':
            transaction.import_transaction_from_csv(customer.customers)

        elif choice == '11':
            transaction.export_transaction_to_csv()

        elif choice == '12':
            transaction.display_monthly_sales_and_transactions()

        elif choice == '13':
            transaction.display_customer_monthly_sales_and_transactions()

        elif choice == '14':
            transaction.display_postcode_monthly_sales_and_transactions(customer.customers)

        elif choice == '15':
            print("Program terminated successfully.")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press 'Enter' key to continue...")


if __name__ == "__main__":
    customer = Customer()
    transaction = Transaction()
    main()
