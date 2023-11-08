from sys import exit

welcome_screen = """
+-------------------------------------------+
|                Welcome to                 |
|         Student Management System         |
|            Coded by Tashi Tam'$           |
|-------------------------------------------|
|          Select an option below           |
+-------------------------------------------+
Press 1 - Add new student details
Press 2 - Show all student
Press 3 - Search a particular student
Press 4 - Delete a particular student
Press 5 - Display dean's list students
Press 6 - Exit the program
"""

no_student_found = """
- No students found in the database.
- Please add some students and try again.
"""

press_enter_key = "- Press Enter key to continue..."

student_list = []

dean_list = []


def main():
    while True:
        print(welcome_screen)

        selected_option = input("Enter your option number: ")

        if selected_option == '1':
            add_new_student()

        elif selected_option == '2':
            show_all_student()

        elif selected_option == '3':
            search_student()

        elif selected_option == '4':
            delete_student()

        elif selected_option == '5':
            display_dean_list()

        elif selected_option == '6':
            exit("Program terminated successfully.")

        else:
            print("Invalid option selected, please select a correct option.")


def exit_confirmation(prompt):
    while True:
        select_option = input(prompt).lower()

        if select_option == 'yes':
            print()
            break

        elif select_option == 'no':
            main()

        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def add_new_student():
    print("+-------------------------------------------+")
    print("|       You selected 1st option             |")
    print("|       Add a new student details           |")
    print("+-------------------------------------------+")

    global student_list

    while True:

        while True:
            try:
                student_id = int(input("Enter student id: "))
            except ValueError:
                print("Invalid student ID entered. Try again!")
            else:
                break

        name = input("Enter student name: ").title()

        while True:
            try:
                gpa = float(input("Enter student GPA between 0-4: "))
            except ValueError:
                print("Invalid GPA entered. Try again!")
            else:
                if 0 <= gpa <= 4:
                    break
                else:
                    print("Sorry enter GPA between 0 and 4")

        major = input("Enter student major: ").title()

        while True:
            try:
                contact_number = int(input("Enter student contact number: "))
            except ValueError:
                print("Invalid contact number entered. Try again!")
            else:
                break

        student = [student_id, name, gpa, major, contact_number]

        student_list.append(student)

        exit_confirmation("Type 'yes' to add another student or 'no' to exit: ")


def show_all_student():
    print("+-------------------------------------------+")
    print("|        You selected 2nd option            |")
    print("|        View all student details           |")
    print("+-------------------------------------------+")

    if len(student_list) > 0:
        print(*student_list, sep="\n")

    else:
        print(no_student_found)

    input(press_enter_key)


def search_student():
    print("+-------------------------------------------+")
    print("|         You selected 3rd option           |")
    print("|         Search student details            |")
    print("+-------------------------------------------+")

    if len(student_list) > 0:
        while True:
            while True:
                try:
                    student_id = int(input("Enter student id: "))
                except ValueError:
                    print("Invalid student ID entered. Try again!")
                else:
                    break

            search_flag = False

            for student in student_list:
                if student[0] == student_id:
                    print("+-------------------------------------------+")
                    print("|               Search Result               |")
                    print("+-------------------------------------------+")
                    print(f"Student ID: {student[0]}")
                    print(f"Name: {student[1]}")
                    print(f"GPA: {student[2]}")
                    print(f"Major: {student[3]}")
                    print(f"Contact Number: {student[4]}")
                    search_flag = True
                    break

            if not search_flag:
                print(f"No student details found for student id {student_id}")

            exit_confirmation("Type 'yes' to search another student or 'no' to exit: ")

    else:
        print(no_student_found)


def delete_student():
    print("+-------------------------------------------+")
    print("|         You selected 4th option           |")
    print("|         Delete student details            |")
    print("+-------------------------------------------+")

    if len(student_list) > 0:
        while True:
            while True:
                try:
                    student_id = int(input("Enter student id: "))
                except ValueError:
                    print("Invalid student ID entered. Try again!")
                else:
                    break

            delete_flag = False

            for student in student_list:
                if student[0] == student_id:
                    if student in dean_list:
                        dean_list.remove(student)
                    student_list.remove(student)
                    print(f"Student record with ID {student_id} deleted successfully.")
                    delete_flag = True

            if not delete_flag:
                print(f"No record found for student id {student_id}")

            exit_confirmation("Type 'yes' to delete another student or 'no' to exit: ")

    else:
        print(no_student_found)


def display_dean_list():
    print("+-------------------------------------------+")
    print("|         You selected 5th option           |")
    print("|         Dean list (GPA>=3.75)             |")
    print("+-------------------------------------------+")

    if len(student_list) > 0:
        for student in student_list:
            if student[2] >= 3.75:
                dean_list.append(student)

        if len(dean_list) > 0:
            print("+-------------------------------------------+")
            print("|       List of students in Dean list       |")
            print("+-------------------------------------------+")
            print(*dean_list, sep="\n")

        else:
            print("Sorry no student in dean list.")

    else:
        print(no_student_found)

    input(press_enter_key)


main()
