
from library import add_book, display_books, issue_book

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            add_book(title, author)
        elif choice == "2":
            display_books()
        elif choice == "3":
            title = input("Enter title to issue: ")
            issue_book(title)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
