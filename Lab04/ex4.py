print("""
+-------------------------------------------+
|    Program Name: Next Letter Converter    |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 4)             |
+-------------------------------------------+
""")

output_msg = """
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
"""

def get_next_letter(letter):

    next_letter = ''

    if letter.isalpha():
        next_letter = ord(letter) + 1

    return chr(next_letter) if letter.isalpha() else letter


input_letter = input("Enter a English letter: ")

result = get_next_letter(input_letter)

if result.isalpha():
    print(f"{output_msg}- The next letter after {input_letter} is {result}.")

else:
    print(f"{output_msg}- {result} is not an English letter.")


