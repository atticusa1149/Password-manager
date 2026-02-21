import csv

passwords=[]

def load_passwords():
    passwords=[]
    with open("Vault.csv","r", newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            passwords.append(row)
    return passwords
def add_password(website,username,password):
    with open("Vault.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([website,username,password])

def find_password(website):
    passwords = load_passwords()
    for row in passwords:
        if row["website"] == website:
            return (
                f"Website:  {row['website']}\n"
                f"Username: {row['username']}\n"
                f"Password: {row['password']}"
            )
    return None

def delete_password(website):
    passwords = load_passwords()
    passwords = [p for p in passwords if p["website"] != website]

    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["website", "username", "password"])  # header
        for p in passwords:
            writer.writerow([p["website"], p["username"], p["password"]])
    print("Deleted successfully")
#Main loop
while True:
    print("\n!!!Password Manager!!!")
    print("1. Add a password")
    print("2. Find a password")
    print("3. Delete a password (warning: this is a permanent option & cannot be undone)")
    print("4. Exit")
    
    choice=input("Select option to proceed: ")
    if choice=="1":
        site=input("Website name: ")
        user=input("Enter username: ")
        pw=input("Enter password: ")
        add_password(site,user,pw)
    elif choice=="2":
        site=input("Enter website name: ")
        result=find_password(site)
        if result:
            print(f"Username & password: {result}")
    elif choice=="3":
        site=input("Enter the name of the website whose password and username and data you wish to delete: ")
        delete_password(site)
    elif choice=="4":
        break

