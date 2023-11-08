print("""
+-----------------------------------------------+
|        Program Name: Result System            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab05 (Exercise 6)             |
+-----------------------------------------------+
""")

result_list = []

value_error_msg = """
+-----------------------------------------------+
|           Oops something went wrong!          |
+-----------------------------------------------+
- Invalid value entered.
- Please enter whole number.
"""

mark_error_msg = """
+-----------------------------------------------+
|            Invalid mark entered!              |   
+-----------------------------------------------+
- Please enter marks between 0 and 100.
"""


def main():
    while True:
        try:
            student_id = int(input("Enter student id: "))

        except ValueError:
            print(value_error_msg)

        else:
            if student_id <= 0:
                break

            else:
                quiz_1 = validate_mark("Enter mark for quiz 1: ")

                quiz_2 = validate_mark("Enter mark for quiz 2: ")

                final_exam = validate_mark("Enter mark for final exam: ")

                total_mark = round((quiz_1 * 0.20) + (quiz_2 * 0.30) + (final_exam * 0.50))

                grade = find_grade(total_mark)

                student_mark = [student_id, quiz_1, quiz_2, final_exam, total_mark, grade]

                result_list.append(student_mark)

                print()


def validate_mark(prompt):
    while True:
        try:
            mark = int(input(prompt))

        except ValueError:
            print(value_error_msg)

        else:
            if 0 <= mark <= 100:
                return mark
            else:
                print(mark_error_msg)


def find_grade(mark):
    if mark >= 80:
        grade_letter = "HD"

    elif mark >= 70:
        grade_letter = "D"

    elif mark >= 60:
        grade_letter = "C"

    elif mark >= 50:
        grade_letter = "P"

    else:
        grade_letter = "N"

    return grade_letter


main()

print("""
+-----------------------------------------------+
| Std ID | Q1 | Q2 | Final Exam | Total | Grade |
+-----------------------------------------------+
""")
print(*result_list, sep="\n")