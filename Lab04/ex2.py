print("""
+-------------------------------------------+
|    Program Name: Largest Number Finder    |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 2)             |
+-------------------------------------------+
""")

input_error_msg = """
+-------------------------------------------+
|         Oops something went wrong!        |
+-------------------------------------------+
- Invalid input entered.
- Except for 'stop' other texts aren't allowed.
- OR type "stop" to terminate the program.
"""

"""
+-------------------------------------------+
|       @return array <int, float, null>    |
+-------------------------------------------+
"""
def validate_input():

    validated_number_list = []

    while True:
        number = input("Enter a decimal number: ")

        if number == 'stop':
            return validated_number_list

        try:
            validated_number_list.append(float(number))

        except ValueError:
            print(input_error_msg)


"""
+-------------------------------------------+
|         @arg array <int, float>           |
|         @return <float>                   |
+-------------------------------------------+
"""
def find_largest_number(args):

    largest_number = 0

    for i in args:
        if i > largest_number:
            largest_number = i

    return largest_number


validated_list = validate_input()

print(f"""
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
- The largest number is {find_largest_number(validated_list):.3f}
- Program terminated successfully.""")
