from os.path import getsize

print("""
+-----------------------------------------------+
|        Program Name: Read & Write File        |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab07 (Exercise 3)             |
+-----------------------------------------------+
""")

def main():
    get_file_size()
    add_new_lines()
    print_first_two_lines()


def get_file_size():
    initial_file_size = getsize('file.txt')
    print(f"File Size: {initial_file_size} bytes \n")


def add_new_lines():
    with open("file.txt", 'a', newline='', encoding='utf-8-sig') as file:
        for _ in range(3):
            line = input("Enter new line: ").capitalize()
            file.write(f"{line} \n")


def print_first_two_lines():
    with open("file.txt", newline='', encoding='utf-8-sig') as file:
        first_line = file.readline()
        second_line = file.readline()

    print()
    print("First line:", first_line, end="")
    print("Second line:", second_line, end="")


if __name__ == '__main__':
    main()
