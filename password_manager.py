import json
import getpass

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def add_password(passwords):
    account = input("Enter account name: ")
    password = getpass.getpass("Enter password: ")
    passwords[account] = password
    save_passwords(passwords)
    print(f"Password for {account} saved successfully!")

def get_password(passwords):
    account = input("Enter account name: ")
    if account in passwords:
        print(f"Password for {account}: {passwords[account]}")
    else:
        print(f"No password found for {account}")

def main():
    passwords = load_passwords()
    
    while True:
        print("\n1. Add Password\n2. Get Password\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            get_password(passwords)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
