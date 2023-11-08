print("""
+-------------------------------------------+
|    Program Name: Calculating Average      |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab04 (Exercise 1)             |
+-------------------------------------------+
""")


def calculate_average(num1, num2):
    return (num1 + num2) / 2


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

average = calculate_average(first_number, second_number)

print(f"""
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
- The average of {first_number} and {second_number}: {average}
- Program terminated successfully.""")
