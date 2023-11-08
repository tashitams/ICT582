from q1.customer import Customer
from q1.transaction import Transaction
from sys import exit
from utils import message


def show_menu():
    from main import main
    customer = Customer()
    transaction = Transaction()

    while True:
        print(message.q1_menu_option)

        choice = input("Select an option: ")

        match choice:
            case '1':
                customer.add()

            case '2':
                transaction.add(customer.customers)

            case '3':
                customer.search()

            case '4':
                transaction.search()

            case '5':
                transaction.show_customer_transactions(customer.customers)

            case '6':
                transaction.delete()

            case '7':
                customer.delete(transaction.transactions)

            case '8':
                exit(f"{message.quit_}")

            case '9':
                main()

            case _:
                print(f"{message.error_title}{message.q1_invalid_choice}")


if __name__ == '__main__':
    show_menu()
