# Library Management System

import os
FILE_NAME = "library.txt"

def load_library():
    library = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                title, author, isbn, available = line.strip().split("|")
                library.append({"Title": title, "Author": author, "ISBN": isbn, "Available": available == "True"})
    return library

def save_library(library):
    with open(FILE_NAME, "w") as file:
        for book in library:
            file.write(f"{book['Title']}|{book['Author']}|{book['ISBN']}|{book['Available']}\n")

library = load_library()

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    isbn = input("Enter the ISBN: ")
    library.append({"Title": title, "Author": author, "ISBN": isbn, "Available": True})
    save_library(library)
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available in the library.\n")
        return
    for index, book in enumerate(library, start=1):
        print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Available: {'Yes' if book['Available'] else 'No'}")
    print()

def edit_book():
    view_books()
    if not library:
        return
    try:
        book_index = int(input("Enter the book number to edit: ")) - 1
        if 0 <= book_index < len(library):
            library[book_index]["Title"] = input("Enter new title: ")
            library[book_index]["Author"] = input("Enter new author: ")
            library[book_index]["ISBN"] = input("Enter new ISBN: ")
            save_library(library)
            print("Book details updated successfully!\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def search_book():
    query = input("Enter the title or author to search: ").lower()
    results = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    if results:
        for book in results:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Available: {'Yes' if book['Available'] else 'No'}")
    else:
        print("No matching books found.\n")

def delete_book():
    view_books()
    if not library:
        return
    try:
        book_index = int(input("Enter the book number to delete: ")) - 1
        if 0 <= book_index < len(library):
            library.pop(book_index)
            save_library(library)
            print("Book deleted successfully!\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main_menu():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Edit Book")
        print("4. Search Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            edit_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()