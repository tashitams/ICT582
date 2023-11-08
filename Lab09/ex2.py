print("""
+-------------------------------------------+
|    Program Name: TicketMachine Program    |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab09 (Exercise 2)             |
+-------------------------------------------+
""")


class TicketMachine:
    def __init__(self, price):
        if price < 0:
            raise ValueError("Ticket price cannot be negative")
        self._price = price
        self._balance = 0
        self._total = 0

    @property
    def price(self):
        return self._price

    @property
    def balance(self):
        return self._balance

    @property
    def total(self):
        return self._total

    def insert_money(self, amount):
        if amount < 0:
            print("Amount cannot be negative")
        else:
            self._balance += amount
            print(f"You deposited ${amount}.")

    def get_price(self):
        print(f"Ticket price is ${self._price}")
        return self._price

    def get_balance(self):
        print(f"Your balance ${self._balance}")
        return self._balance

    def print_ticket(self):
        if self._balance >= self._price:
            print("Ticket printed.")
            self._total += self._price
            self._balance -= self._price
            print(f"Total amount collected by the machine: ${self._total}")
            print(f"Your current balance is ${self._balance}")
        else:
            print("Insufficient balance.")


def main():
    ticket_price = int(input("Enter ticket price: "))

    amount = int(input("Enter an amount to deposit in your account: "))

    ticket_machine = TicketMachine(ticket_price)

    print()
    print("--------------- Program Output ---------------")
    ticket_machine.insert_money(amount)
    ticket_machine.get_price()
    ticket_machine.get_balance()
    ticket_machine.print_ticket()


if __name__ == '__main__':
    main()
