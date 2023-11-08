def main():
    copy_file()


def copy_file():
    with open('foo.txt', 'r') as source, open('bar.txt', 'w') as destination:
        file_contents = source.read()

        destination.write(file_contents)

        print("File 'foo.txt' copied to 'bar.txt' successfully.")


if __name__ == '__main__':
    main()
