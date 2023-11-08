"""
Function to generate a triangle
based on row number
"""

def generate_triangle(row_no):
    for i in range(row_no, 0, -1):
        for j in range(1, i + 1):
            print(j, end="  ")
        print() 
    print()

