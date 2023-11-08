print("""
+-------------------------------------------+
|   Program Name: °F to °C Converter        |      
|   Coded by: Tashi Dorji Tamang            |
|   Language used: Python (3.11.3)          |
|   Remark: Lab04 (Exercise 9)              |
+-------------------------------------------+
""")

success_msg = """
+-------------------------------------------+
|             Program Output                |
+-------------------------------------------+
"""

range_error_msg = """
+-------------------------------------------+
|         Oops something went wrong!        |
+-------------------------------------------+
- The temperature you entered is out of range.
- Please enter between -60 and 130 (°F).
"""

input_error_msg = """
+-------------------------------------------+
|         Oops something went wrong!        |
+-------------------------------------------+
- Invalid number enter.
- Type "end" to terminate the program.
"""

end_msg = """
+-------------------------------------------+
|            Program Terminated             |
+-------------------------------------------+
- You entered end.
- Program terminated successfully.
"""


def temperature_converter(temp_fah):
    temp_in_cel = (temp_fah - 32) * 5 / 9
    print(f"{success_msg}- Temperature: {_temp}°F -----> {temp_in_cel:.1f}°C. \n")


while True:
    _temp = input("Enter the temperature in Fahrenheit: ")

    if _temp == 'end':
        print(end_msg)
        break

    try:
        temp_in_fah = float(_temp)

    except ValueError:
        print(input_error_msg)

    else:
        if -60 <= temp_in_fah <= 130:
            temperature_converter(temp_in_fah)

        else:
            print(range_error_msg)


