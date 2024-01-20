#!/usr/bin/env python3

# Script Name: File Encryption 2
# Author: Eveangalina Campos
# Date of latest revision: 01/19/2024
# Purpose: This Python script Encrypts and Decrypts files or messages
# Resources:
# - Python: List Of Files In Directory And Subdirectories
# - Recursive File and Directory Manipulation in Python
# - ChatGPT assistance

import os
from cryptography.fernet import Fernet

def generate_key():
    """Generate and save a new encryption key."""
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from file."""
    return open("encryption_key.key", "rb").read()

def encrypt_file(filepath, key):
    """Encrypt a file using Fernet encryption."""
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = fernet.encrypt(file.read())
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    """Decrypt a file using Fernet decryption."""
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        decrypted_data = fernet.decrypt(file.read())
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def encrypt_string(text, key):
    """Encrypt a string."""
    return Fernet(key).encrypt(text.encode()).decode()

def decrypt_string(text, key):
    """Decrypt a string."""
    return Fernet(key).decrypt(text.encode()).decode()

def encrypt_folder(folder_path, key):
    """Recursively encrypt all files in a folder."""
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            print(f"Encrypted {file_path}")

def decrypt_folder(folder_path, key):
    """Recursively decrypt all files in a folder."""
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
            print(f"Decrypted {file_path}")

def main():
    if not os.path.exists("encryption_key.key"):
        generate_key()
    key = load_key()

    while True:
        print("1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n7. Exit")
        mode = input("Enter the mode (1/2/3/4/5/6/7): ")

        if mode == '1':
            filepath = input("Enter file path to encrypt: ")
            encrypt_file(filepath, key)
            print("File encrypted successfully.")
        elif mode == '2':
            filepath = input("Enter file path to decrypt: ")
            decrypt_file(filepath, key)
            print("File decrypted successfully.")
        elif mode == '3':
            text = input("Enter message to encrypt: ")
            print("Encrypted message:", encrypt_string(text, key))
        elif mode == '4':
            text = input("Enter encrypted message: ")
            print("Decrypted message:", decrypt_string(text, key))
        elif mode == '5':
            folder_path = input("Enter folder path to encrypt: ")
            encrypt_folder(folder_path, key)
            print("Folder encrypted successfully.")
        elif mode == '6':
            folder_path = input("Enter folder path to decrypt: ")
            decrypt_folder(folder_path, key)
            print("Folder decrypted successfully.")
        elif mode == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid mode. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()

