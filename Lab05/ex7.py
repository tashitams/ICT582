print("""
+-------------------------------------------+
|    Program Name: Result System            |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab05 (Exercise 7)             |
+-------------------------------------------+
""")

result_list = []
highest_grade_id_list = []
lowest_grade_id_list = []
average_mark_list = []

highest_mark = 0
average_mark = 0
fail_student_count = 0
lowest_mark = 100

no_item_found = "None"

value_error_msg = """
+-------------------------------------------+
|       Oops something went wrong!          |
+-------------------------------------------+
- Invalid value entered.
- Please enter whole number.
"""

mark_error_msg = """
+-------------------------------------------+
|          Invalid mark entered!            |   
+-------------------------------------------+
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

    calculate_highest_lowest_average_mark()

    find_highest_and_lowest_grade()

    count_fail_student_number()


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


def find_highest_and_lowest_grade():
    global highest_grade_id_list, lowest_grade_id_list

    for result in result_list:
        if result[5] == 'HD':
            highest_grade_id_list.append(result[0])

        if result[5] == 'N':
            lowest_grade_id_list.append(result[0])


def calculate_highest_lowest_average_mark():
    global highest_mark, lowest_mark, average_mark

    for result in result_list:
        for mark in range(1, 4):
            if result[mark] > highest_mark:
                highest_mark = result[mark]

            if result[mark] < lowest_mark:
                lowest_mark = result[mark]

        average_mark_list.append(result[4])

    try:
        average_mark = sum(average_mark_list) / len(result_list)
    except ZeroDivisionError:
        lowest_mark = 0


def count_fail_student_number():
    global fail_student_count

    for result in result_list:
        if result[5] == 'N':
            fail_student_count += 1


main()

print(f"""
+-------------------------------------------+
|          Final Result Statistics          |
+-------------------------------------------+
""")
print("Student List", *result_list, sep="\n")

print(f"""
1) Highest Mark: {highest_mark}
2) Lowest Mark: {lowest_mark}
3) Average Mark: {average_mark:.2f}%

4) Student IDs of Highest Grade: {highest_grade_id_list if len(highest_grade_id_list) > 0 else no_item_found}
5) Student IDs of Lowest Grade: {lowest_grade_id_list if len(lowest_grade_id_list) > 0 else no_item_found}
6) Total Number of Failed student: {fail_student_count}
""")
