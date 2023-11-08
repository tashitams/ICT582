print("""
+-------------------------------------------+
|      Program Name: Cube Root Finder       |      
|      Coded by: Tashi Dorji Tamang         |
|      Language used: Python (3.11.3)       |
+-------------------------------------------+
""")

value_error_msg = """
+-------------------------------------------+
|        Oops something went wrong!         |
+-------------------------------------------+
- Invalid input entered, try again.
"""

while True:

    int_number = input("Enter an integer number: ")

    if int_number == 'stop':
        break

    try:
        number = int(int_number)

    except ValueError:
        print(value_error_msg)

    else:
        if number == 1:
            loop_iterate = 1

        else:
            loop_iterate = number // 2

        for i in range(loop_iterate + 1):
            if i ** 3 == number:
                print(f"\nThe cube root of {number} is: {i} \n")
                break

print(f"""
+-------------------------------------------+
|            Program terminated             |
+-------------------------------------------+
- You entered stop.
- Exiting the program...
""")
