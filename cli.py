from functions import (
    load_key,
    verify_master_password,
    load_passwords,
    add_password,
    find_password,
    delete_password
)
from cryptography.fernet import Fernet

def main():
    print("=== Password Manager ===")

    # Require master password
    if not verify_master_password():
        print("Incorrect master password.")
        return

    # Load encryption key
    key = load_key()
    fernet = Fernet(key)

    while True:
        print("\n1. Add password")
        print("2. Find password")
        print("3. Delete password")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            site = input("Website: ")
            user = input("Username: ")
            pw = input("Password: ")
            add_password(site, user, pw, fernet)

        elif choice == "2":
            site = input("Website: ")
            result = find_password(site, fernet)
            if result:
                print("\n=== Entry Found ===")
                print(f"Website:  {result['website']}")
                print(f"Username: {result['username']}")
                print(f"Password: {result['password']}")
            else:
                print("Not found.")

        elif choice == "3":
            site = input("Website: ")
            delete_password(site)

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


# Run the program
if __name__ == "__main__":
    main()
