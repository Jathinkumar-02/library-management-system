
books = []

def add_book(title, author):
    book = {
        "title": title,
        "author": author,
        "available": True
    }
    books.append(book)
    print(f"Book added: {title}")

def display_books():
    if not books:
        print("No books in the library.")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(f'{book["title"]} by {book["author"]} - {status}')

def issue_book(title):
    for book in books:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            print(f"Book issued: {title}")
            return

    print("Book not available.")
