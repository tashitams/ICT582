print("""
+-------------------------------------------+
|      Program Name: Result System          |      
|      Coded by: Tashi Dorji Tamang         |
|      Language used: Python (3.11.3)       |
+-------------------------------------------+
""")

input_error_msg = """
+-------------------------------------------+
|        Oops something went wrong!         |
+-------------------------------------------+
- Invalid input entered.
- Except for "end" other texts are not allowed.
- Special symbols aren't allowed
"""

total_mark = mark_count = hd_count = d_count = c_count = p_count = n_count = fail_percentage = 0

while True:

    marks = input("Enter the mark: ")

    if marks == 'end':
        break

    try:
        mark = float(marks)

    except ValueError:
        print(input_error_msg)

    else:
        total_mark += mark

        mark_count += 1

        if mark >= 80:
            hd_count += 1

        elif mark >= 70:
            d_count += 1

        elif mark >= 60:
            c_count += 1

        elif mark >= 50:
            p_count += 1

        else:
            n_count += 1

        fail_percentage = (n_count / mark_count) * 100

print(f"""
+-------------------------------------------+
|             Program Output                |      
+-------------------------------------------+
- Total Mark: {total_mark}

- Total unit marks entered: {mark_count}
- High Distinction: {hd_count}
- Distinction: {d_count}
- Credit: {c_count}
- Pass: {p_count}
- Fail: {n_count}

- Fail %: ({fail_percentage:.1f}% of students failed the unit)
""")