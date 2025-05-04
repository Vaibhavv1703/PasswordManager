import checker
import manager
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_menu():
    print("=" * 45)
    print("||{:^41}||".format("Vaibh's CyberSec Project"))
    print("=" * 45)
    print("||{:^41}||".format("1. Password Strength Checker"))
    print("||{:^41}||".format("2. Password Manager"))
    print("||{:^41}||".format("3. About Me"))
    print("||{:^41}||".format("4. Contact"))
    print("||{:^41}||".format("0. Exit"))
    print("=" * 45 + "\n")

def main():
    while True:
        cls()
        print_main_menu()
        ch = input("Enter your choice: ")
        print("\n")

        if ch == '0':
            print("Exiting the program.")
            break
        elif ch == '1':
            try:
                checker.run()
            except Exception as e:
                print(f"An error occurred in the Password Strength Checker: {e}")
        elif ch == '2':
            try:
                manager.run()
            except Exception as e:
                print(f"An error occurred in the Password Manager: {e}")
        elif ch == '3':
            cls()
            print("\n" + "=" * 45)
            print("||{:^41}||".format("About Me"))
            print("=" * 45)
            print("||{:^41}||".format("Hello! I'm Vaibhav"))
            print("||{:^41}||".format("A Computer Science Student"))
            print("=" * 45 + "\n")
            input("Press any key to go back to the main menu\n")
        elif ch == '4':
            cls()
            print("\n" + "=" * 100)
            print("||{:^96}||".format("Contact"))
            print("=" * 100)
            print("||{:^96}||".format("Email: vaibhavvsingh1703@gmail.com"))
            print("||{:^96}||".format("LinkedIn: https://www.linkedin.com/in/vaibhavsingh1703/"))
            print("||{:^96}||".format("GitHub: https://github.com/Vaibhavv1703"))
            print("=" * 100 + "\n")
            input("Press any key to go back to the main menu\n")
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()