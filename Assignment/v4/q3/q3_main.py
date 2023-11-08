from sys import exit
from utils import message
from q3.customer import Customer
from q3.transaction import Transaction

def show_menu():
    from main import main

    while True:
        print(message.q3_menu_option)

        choice = input("Select an option: ")

        match choice:
            case '1':
                Customer.add()

            case '2':
                Transaction.add(Customer.customers)

            case '3':
                Customer.search()

            case '4':
                Transaction.search()

            case '5':
                Transaction.show_customer_transactions(Customer.customers)

            case '6':
                Transaction.delete()

            case '7':
                Customer.delete(Transaction.transactions)

            case '8':
                Customer.load_from_csv()

            case '9':
                Customer.save_to_csv()

            case '10':
                Transaction.load_from_csv(Customer.customers)

            case '11':
                Transaction.save_to_csv()

            case '12':
                Transaction.monthly_sales_report()

            case '13':
                Transaction.customer_sales_report()

            case '14':
                Transaction.customer_postcode_report(Customer.customers)

            case '15':
                exit(f"{message.quit_}")

            case '16':
                main()

            case _:
                print(f"{message.error_title}{message.q2_invalid_choice}")


if __name__ == '__main__':
    show_menu()
