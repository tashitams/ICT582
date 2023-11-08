def main():
    copy_file()


def copy_file():
    try:
        # Open the file "foo.txt" for reading
        with open("foo.txt", "r") as file_to_copy:
            file_content = file_to_copy.read()

    except FileNotFoundError:
        print("Error: The file 'foo.txt' doesn't exist.")

    else:
        try:
            with open("bar.txt", "x") as copied_file:
                copied_file.write(file_content)

        except FileExistsError:
            print("Error: The file 'bar.txt' already exists.")

        else:
            print("File 'foo.txt' copied to 'bar.txt' successfully.")


if __name__ == '__main__':
    main()
