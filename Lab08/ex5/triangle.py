"""
Function to generate a triangle
based on row number
"""

def generate_triangle(row_no):
    # Assert that row_no is an integer else
    # Raise an AssertionError
    assert isinstance(row_no, int), "Must be an integer."

    # Assert that row_no must be in the range of 1 to 9 else
    # Raise an AssertionError
    assert 1 <= row_no <= 9, "Must be in the range of 1 to 9."

    for i in range(row_no, 0, -1):
        for j in range(1, i + 1):
            print(j, end="  ")
        print()
    print()
