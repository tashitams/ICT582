print("""
+-----------------------------------------------+
|        Program Name: Result System            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab06 (Exercise 2)             |
+-----------------------------------------------+
""")

student_list = {}
highest_grade = {}
lowest_grade = {}
fail_student_count = 0

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
                name = input("Enter your name: ").title()

                quiz_1 = validate_mark("Enter mark for quiz 1: ")

                quiz_2 = validate_mark("Enter mark for quiz 2: ")

                final_exam = validate_mark("Enter mark for final exam: ")

                unit_mark = round((quiz_1 * 0.20) + (quiz_2 * 0.30) + (final_exam * 0.50))

                grade = find_grade(unit_mark)

                if student_id not in student_list:
                    student_list[student_id] = {}

                student_list[student_id]['name'] = name
                student_list[student_id]['quiz_1'] = quiz_1
                student_list[student_id]['quiz_2'] = quiz_2
                student_list[student_id]['final_exam'] = final_exam
                student_list[student_id]['unit_mark'] = unit_mark
                student_list[student_id]['grade'] = grade
                student_list[student_id]['highest_mark'] = max(quiz_1, quiz_2, final_exam)
                student_list[student_id]['lowest_mark'] = min(quiz_1, quiz_2, final_exam)
                student_list[student_id]['average_mark'] = (quiz_1 + quiz_2 + final_exam) / 3

                print()

    find_highest_grade()

    find_lowest_grade()

    count_fail_student_number()

    print("+-----------------------------------------------+")
    print("|             Student statistics                |")
    print("+-----------------------------------------------+")
    for student_id, result in student_list.items():
        print(f"Name: {result['name']}")
        print(f"Student ID: {student_id}")
        print(f"Quiz 1: {result['quiz_1']}")
        print(f"Quiz 2: {result['quiz_2']}")
        print(f"Final Exam: {result['final_exam']}")
        print(f"Unit Mark: {result['unit_mark']}")
        print(f"Grade: {result['grade']}")
        print(f"Highest Mark: {result['highest_mark']}")
        print(f"Lowest Mark: {result['lowest_mark']}")
        print(f"Average Mark: {result['average_mark']} \n")

    print("+-----------------------------------------------+")
    print("|          Student with Highest Grade           |")
    print("+-----------------------------------------------+")
    if len(highest_grade) > 0:
        for student_id, result in highest_grade.items():
            print(f"Student Name: { result['name'] }")
            print(f"Student ID: { student_id } \n")

    else:
        print("No students found in HD category")

    print("+-----------------------------------------------+")
    print("|          Student with Lowest Grade            |")
    print("+-----------------------------------------------+")
    if len(lowest_grade) > 0:
        for student_id, result in lowest_grade.items():
            print(f"Student Name: {result['name']}")
            print(f"Student ID: {student_id} \n")
    else:
        print("No students found in N category")

    print(f"\nTotal Number of Failed student: {fail_student_count}")

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


def find_highest_grade():
    for student_id, result in student_list.items():
        if student_id not in highest_grade and result['grade'] == 'HD':
            highest_grade[student_id] = {}

        if result['grade'] == 'HD':
            highest_grade[student_id]['name'] = result['name']


def find_lowest_grade():
    for student_id, result in student_list.items():
        if student_id not in lowest_grade and result['grade'] == 'N':
            lowest_grade[student_id] = {}

        if result['grade'] == 'N':
            lowest_grade[student_id]['name'] = result['name']


def count_fail_student_number():
    global fail_student_count

    for student_id, result in student_list.items():
        if result['grade'] == 'N':
            fail_student_count += 1


main()
