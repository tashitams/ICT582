import csv
from sys import exit

print("""
+-----------------------------------------------+
|        Program Name: Read CSV File            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab08 (Exercise 4)             |
+-----------------------------------------------+
""")


def main():
    check_if_csv_file_exist()
    check_if_staff_id_is_missing()
    print_staff_detail()


def check_if_csv_file_exist():
    try:
        with open('staff.csv', 'r') as csv_file:
            pass

    except FileNotFoundError:
        print("The file 'staff.csv' is not found.")
        exit()


def check_if_staff_id_is_missing():
    staff_id_list = []

    with open('staff.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)  # exclude the first row

        for row in reader:
            staff_id_list.append(row[0])

    try:
        if "" in staff_id_list:
            raise FileNotFoundError("The Staff ID is missing in the staff.csv")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit()


def print_staff_detail():
    with open('staff.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)  # exclude the first row

        for row in reader:
            print(f"Staff Name    : {row[1]}")
            print(f"Home Address  : {row[3]}")
            print("+-----------------------------------------------+ \n")


if __name__ == '__main__':
    main()
