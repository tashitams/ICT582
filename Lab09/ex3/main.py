from machine import Machine as MachineSystem
from ticket import Ticket as TicketMachine

print("""
+-------------------------------------------+
|    Program Name: TicketMachine Program    |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab09 (Exercise 3)             |
+-------------------------------------------+
""")

def main():

    # creating two instance of TicketMachine class
    machine_1 = TicketMachine(5)
    machine_2 = TicketMachine(15)

    # creating object of MachineSystem that is
    # responsible to add, remove and display the
    # sales report
    machine = MachineSystem()

    machine.add_machine(machine_1)
    machine.add_machine(machine_1)

    machine_1.insert_money(50)
    machine_1.print_ticket()

    machine_1.insert_money(50)
    machine_1.print_ticket()

    # Remove a machine
    # machine.remove_machine(machine_1)

    # Get total sales for a specific machine
    print(f"Total sales for machine 1: ${machine.get_total_for_a_machine(machine_1)}")
    print(f"Total sales for machine 2: ${machine.get_total_for_a_machine(machine_2)}")

    # Get total sales for all machines
    print(f"Total sales for all machines: ${machine.get_total_sales_of_all_machine()}")


if __name__ == '__main__':
    main()
