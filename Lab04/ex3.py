print("""
+-------------------------------------------+
|    Program Name: Largest Number Finder    |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 3)             |
+-------------------------------------------+
""")

largest_number = 0

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

    global largest_number

    for i in args:
        if i > largest_number:
            largest_number = i


validated_list = validate_input()

find_largest_number(validated_list)

print(f"""
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
- The largest number is {largest_number:.3f}
- Program terminated successfully.""")
