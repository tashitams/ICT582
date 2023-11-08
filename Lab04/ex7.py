print("""
+-------------------------------------------+
|    Program Name: String Generator         |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 7)             |
+-------------------------------------------+
""")

success_msg = """
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
"""

stop_msg = """
+-------------------------------------------+
|            Program Terminated             |
+-------------------------------------------+
- You entered stop.
- Program terminated successfully.
"""


def generate_new_string(_str):

    final_string = ""  # initialize the variable to hold the final string

    for i in _str:

        if ord(i) == 32:  # check for blank space
            new_string = 32

        else:
            new_string = ord(i) + 1  # increment the ascii value by 1

        final_string = final_string + chr(new_string)

    print(f"{success_msg}- The new string is '{final_string}' \n")


while True:

    string = input("Enter a string: ")

    if string == 'stop':
        print(stop_msg)
        break

    generate_new_string(string)