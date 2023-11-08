print("""
+-------------------------------------------+
|    Program Name: Digit Counter            |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 6)             |
+-------------------------------------------+
""")

stop_msg = """
+-------------------------------------------+
|            Program Terminated             |
+-------------------------------------------+
- You entered stop.
- Program terminated successfully.
"""


def count_digit_inside_string(string):

    digit_in_str = ''

    for i in string:

        if i.isdigit():
            digit_in_str = digit_in_str + i

    return digit_in_str if len(digit_in_str) > 0 else 0


while True:

    word = input("Enter a word: ")

    if word == 'stop':
        print(stop_msg)
        break

    result = count_digit_inside_string(word)

    print(f"\nThe digit present are {result}. \n")
