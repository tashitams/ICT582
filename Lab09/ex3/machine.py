class Machine:
    def __init__(self):
        self.machines = []

    def add_machine(self, machine):
        self.machines.append(machine)

    def remove_machine(self, machine):
        self.machines.remove(machine)

    def get_total_for_a_machine(self, machine):
        return machine.total

    def get_total_sales_of_all_machine(self):
        total_sales = sum(machine.total for machine in self.machines)
        return total_sales
