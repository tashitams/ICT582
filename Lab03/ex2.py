print("""
+-------------------------------------------+
|    Program Name: Finding Largest Number   |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
+-------------------------------------------+
""")

input_error_msg = """
+-------------------------------------------+
|        Oops something went wrong!         |
+-------------------------------------------+
- Invalid value entered.
- Except for "stop" other texts are not allowed.
- Can't use special symbols
- Type 'stop' to terminate the program
"""

program_output = """
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
"""

largest_number = 0

while True:

    decimal_number = input("Enter a decimal number: ")

    if decimal_number == 'stop':
        print(f"{program_output}- The largest number is {largest_number:.3f} \n")
        break

    try:
        number = float(decimal_number)

    except ValueError:
        print(input_error_msg)

    else:
        if number > largest_number:
            largest_number = number
