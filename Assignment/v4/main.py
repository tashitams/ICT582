from q1.q1_main import show_menu as q1_menu
from q2.q2_main import show_menu as q2_menu
from q3.q3_main import show_menu as q3_menu
from utils import message

def main():
    print(message.menu_option)
    while True:
        choice = input("Select an option: ")

        match choice:
            case '1':
                q1_menu()

            case '2':
                q2_menu()

            case '3':
                q3_menu()

            case '4':
                exit(f"{message.quit_}")

            case _:
                print(f"{message.error_title}{message.program_invalid_choice}")


if __name__ == '__main__':
    main()
