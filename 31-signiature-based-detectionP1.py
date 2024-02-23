#!/usr/bin/env python3
# Script Name: Ops Challenge: Signature-based Malware Detection Part 1 of 3
# Author: E.Campos
# Date of latest revision: Feb 22 2024
# Resources: Classmates; Rodolfo Gonzalez / Juan Cano / chat.openai.com
# Purpose: Search for specific files within a given directory and its subdirectories.

import os

def search_file(file_name, directory):
    hits = 0
    files_searched = 0

    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return 0, 0

    print(f"Searching for '{file_name}' in '{directory}'...")
    for root, _, files in os.walk(directory):
        for file in files:
            files_searched += 1
            if file == file_name:
                hits += 1
                print("Found:", os.path.join(root, file))
            if files_searched % 100 == 0:
                print_progress(files_searched)

    return hits, files_searched

def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')

def list_directories(base_directory="/"):
    print(f"Available directories in {base_directory}:")
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)
        if os.path.isdir(item_path):
            print(f"- {item_path}")
    print()

def get_directory_input():
    directory = input("Enter the directory to search in or type 'list' for root directories: ").strip()
    if directory.lower() == "list":
        list_directories()
        directory = input("Enter the directory to search in: ").strip()
    return directory

def search_files():
    file_name = input("Enter the file name to search for: ").strip()
    if not file_name:
        print("Error: Please provide a file name.")
        return

    directory = get_directory_input()
    if not directory or not os.path.exists(directory):
        print("Error: Directory does not exist or was not provided.")
        return

    hits, files_searched = search_file(file_name, directory)
    print_search_summary(hits, files_searched)

def print_search_summary(hits, files_searched):
    print("\nTotal files searched:", files_searched)
    print("Total hits found:", hits)

def main():
    while True:
        print("\nMenu:")
        print("1. Search for files")
        print("2. List root directories")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_files()
        elif choice == "2":
            list_directories()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
