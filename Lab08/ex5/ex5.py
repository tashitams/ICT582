# Import the triangle module
import triangle

print("""
+-------------------------------------------+
|   Program Name: Number pattern            |      
|   Coded by: Tashi Dorji Tamang            |
|   Language used: Python (3.11.3)          |
|   Remark: Lab08 (Exercise 5)              |
+-------------------------------------------+
""")

"""
+-----------------------------------------------------------------+
|     Test case     |     Row Value     |     Expected Result     |
+-----------------------------------------------------------------+

|  Positive number  |         3         |     Generate triangle   |
|  Negative number  |        -3         |     Raise AssertionError|
|  String value     |        '3'        |     Raise AssertionError|
+-----------------------------------------------------------------+
"""

# Define a main() function
def main():
    for rows in [3, 5, 19]:
        triangle.generate_triangle(rows)  # call function generate inside triangle module


if __name__ == "__main__":
    main()
