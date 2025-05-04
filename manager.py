import os
import json
import getpass
from cryptography.fernet import Fernet
from hashlib import sha256
import base64
import main

VAULT_PATH = 'vault.enc'

def get_fernet(master_password):
    key = sha256(master_password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))

def load_vault(f, master_password):
    with open(f, 'rb') as file:
        encrypted_data = file.read()
    fernet = get_fernet(master_password)
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
    except:
        return {-1}

def save_vault(f, master_password, vault):
    fernet = get_fernet(master_password)
    data = json.dumps(vault).encode()
    encrypted_data = fernet.encrypt(data)
    with open(f, 'wb') as file:
        file.write(encrypted_data)

def add_password(vault, master_password):
    site = input("Website: ").strip()
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()
    remark = input("Remark (optional): ").strip()

    if site not in vault:
        vault[site] = []
    vault[site].append({"username": username, "password": password, "remark": remark})
    print("Entry added.")
    save_vault(VAULT_PATH, master_password, vault)

def view_passwords(vault):
    if not vault:
        print("Vault is empty.")
        return
    for site, accounts in vault.items():
        print(f"\nWebsite: {site}")
        for i, acc in enumerate(accounts):
            print(f"  {i+1}. Username: {acc['username']}, Password: {acc['password']}, Remark: {acc['remark']}")

def delete_password(vault, master_password):
    site = input("Website to delete from: ").strip()
    if site not in vault:
        print("[!] Site not found.")
        return
    for i, acc in enumerate(vault[site]):
        print(f"  {i+1}. Username: {acc['username']}")
    try:
        idx = int(input("Choose account to delete: ")) - 1
        if 0 <= idx < len(vault[site]):
            del vault[site][idx]
            if not vault[site]:
                del vault[site]
            print("Entry deleted.")
            save_vault(VAULT_PATH, master_password, vault)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def search_password(vault):
    site = input("Website to search: ").strip()
    if site in vault:
        for i, acc in enumerate(vault[site]):
            print(f"  {i+1}. Username: {acc['username']}, Password: {acc['password']}, Remark: {acc['remark']}")
    else:
        print("Site not found.")

def update_password(vault, master_password):
    site = input("Website to update: ").strip()
    if site not in vault:
        print("Site not found.")
        return
    for i, acc in enumerate(vault[site]):
        print(f"  {i+1}. Username: {acc['username']}")
    try:
        idx = int(input("Choose account to update: ")) - 1
        if 0 <= idx < len(vault[site]):
            new_username = input("New Username: ").strip()
            new_password = getpass.getpass("New Password: ").strip()
            new_remark = input("New Remark (optional): ").strip()
            vault[site][idx] = {"username": new_username, "password": new_password, "remark": new_remark}
            print("Entry updated.")
            save_vault(VAULT_PATH, master_password, vault)
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def print_menu():
    print("\n" + "=" * 45)
    print("||{:^41}||".format("1. Add Password"))
    print("||{:^41}||".format("2. View Passwords"))
    print("||{:^41}||".format("3. Delete Password"))
    print("||{:^41}||".format("4. Search Password"))
    print("||{:^41}||".format("5. Update Password"))
    print("||{:^41}||".format("0. Back to Main Menu"))
    print("=" * 45 + "\n")

def run():
    main.cls()
    print("\n" + "=" * 45)
    print("||{:^41}||".format("Password Manager"))
    print("=" * 45)
    if not os.path.exists(VAULT_PATH):
        print("Vault not found. Creating a new one.")
        while True:
            master_password = getpass.getpass("Set a master password: ")
            confirm_password = getpass.getpass("Confirm master password: ")
            if master_password == confirm_password:
                print("Master password set.")
                break
            else:
                print("Passwords do not match. Please try again.")
        vault = {}
    else:
        master_password = getpass.getpass("Enter master password: ")
        vault = load_vault(VAULT_PATH, master_password)
        if(vault == {-1}):
            print("Invalid master password or corrupted vault.")
            return

    save_vault(VAULT_PATH, master_password, vault)
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_password(vault, master_password)
        elif choice == '2':
            view_passwords(vault)
        elif choice == '3':
            delete_password(vault, master_password)
        elif choice == '4':
            search_password(vault)
        elif choice == '5':
            update_password(vault, master_password)
        elif choice == '0':
            print("Going back to the main menu...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    run()