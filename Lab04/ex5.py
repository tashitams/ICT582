print("""
+-------------------------------------------+
|    Program Name: Digit Counter            |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 5)             |
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

    print(f"\nThere are {len(digit_in_str)} digit inside {string} \n")


while True:

    word = input("Enter a word: ")

    if word == 'stop':
        print(stop_msg)
        break

    count_digit_inside_string(word)
