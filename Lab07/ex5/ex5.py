import csv
from sys import exit

print("""
+-----------------------------------------------+
|        Program Name: Read CSV File            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab07 (Exercise 5)             |
+-----------------------------------------------+
""")


def main():
    display_menu()
    display_staff_info()
    add_new_staff()


def display_menu():
    while True:
        print("Select an option:")
        print("Press 1. Show staff details")
        print("Press 2. Add new staff")
        print("Press 3. Quit \n")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_staff_info()

        elif choice == "2":
            add_new_staff()

        elif choice == "3":
            exit("Program terminated successfully.")

        else:
            print("Invalid choice. Please select a valid option. \n")


def add_new_staff():
    print()
    row = []
    try:
        staff_id = int(input("Enter staff id: "))

    except ValueError:
        print("Invalid value entered, please enter number only.")

    else:
        name = input("Enter staff name: ").title()
        phone_number = input("Enter staff phone number: ")
        home_address = input("Enter staff home address: ").title()
        print()

        row = [staff_id, name, phone_number, home_address]

    with open("staff.csv", "a", newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row)

    while True:
        option = input("Type 'yes' to add another record or 'no' to return to main menu: ").lower()
        if option == "yes":
            add_new_staff()
        elif option == "no":
            display_menu()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def display_staff_info():
    print()
    with open("staff.csv", newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # exclude the first row
        for row in reader:
            print(f"Staff ID      : {row[0]}")
            print(f"Staff Name    : {row[1]}")
            print(f"Phone Number  : {row[2]}")
            print(f"Home Address  : {row[3]}")
            print("+-----------------------------------------------+ \n")


if __name__ == '__main__':
    main()
