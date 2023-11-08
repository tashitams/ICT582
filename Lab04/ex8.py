import triangle

print("""
+-------------------------------------------+
|   Program Name: Number pattern            |      
|   Coded by: Tashi Dorji Tamang            |
|   Language used: Python (3.11.3)          |
|   Remark: Lab04 (Exercise 8)              |
+-------------------------------------------+
""")


# rows = int(input("Enter row number: "))
# generate_triangle(rows)

for rows in [3, 5, 9]:
    triangle.generate_triangle(rows)  # call function generate inside triangle module
