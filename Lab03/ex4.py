print("""
+-------------------------------------------+
|   Program Name: Print a number pattern    |      
|   Coded by: Tashi Dorji Tamang            |
|   Language used: Python (3.11.3)          |
+-------------------------------------------+
""")

char = "123456789"

for i in range(len(char), 0, -1):
    # print(i) 987654321

    for j in range(0, i):
        # print(j)  012345678
        print(char[j], end="   ")

    print()  # for line break for each iteration of outer loop
