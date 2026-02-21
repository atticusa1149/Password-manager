import csv
import hashlib
from cryptography.fernet import Fernet

def verify_master_password():
    with open("master.hash", "r") as f:
        saved_hash = f.read().strip()

    attempt = input("Enter master password: ")
    attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

    return attempt_hash == saved_hash



def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def load_passwords():
    passwords = []
    with open("Vault.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            passwords.append(row)
    return passwords



def add_password(website, username, password, fernet):
    encrypted = fernet.encrypt(password.encode()).decode()

    with open("Vault.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([website, username, encrypted])

    print("Password saved.")


def find_password(website, fernet):
    passwords = load_passwords()
    for row in passwords:
        if row["website"] == website:
            decrypted = fernet.decrypt(row["password"].encode()).decode()
            return {
                "website": row["website"],
                "username": row["username"],
                "password": decrypted
            }
    return None


def delete_password(website):
    passwords = load_passwords()
    passwords = [p for p in passwords if p["website"] != website]

    with open("Vault.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["website", "username", "password"])
        for p in passwords:
            writer.writerow([p["website"], p["username"], p["password"]])

    print("Entry deleted (if it existed).")



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
