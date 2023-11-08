import csv

print("""
+-----------------------------------------------+
|        Program Name: Read CSV File            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab07 (Exercise 4)             |
+-----------------------------------------------+
""")


def main():
    display_staff_info()


def display_staff_info():
    with open("staff.csv", newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # exclude the first row
        for row in reader:
            print(f"Staff Name    : {row[1]}")
            print(f"Home Address  : {row[3]}")
            print("+-----------------------------------------------+ \n")


if __name__ == '__main__':
    main()
