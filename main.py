"""
Console app entry point for the library checkout system.
Run with: python main.py
"""

from library_app.book import Book
from library_app.catalog import Catalog


def main():
    catalog = Catalog()

    catalog.add_book(Book("The Pragmatic Programmer", "David Thomas", "9780135957059", 3))
    catalog.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884", 2))
    catalog.add_book(Book("The DevOps Handbook", "Gene Kim", "9781942788003", 1))

    running = True
    while running:
        print()
        print("=== Library Menu ===")
        print("1. List all books")
        print("2. Search by title")
        print("3. Add a new book")
        print("4. Check out a book (by ISBN)")
        print("5. Return a book (by ISBN)")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for book in catalog.books:
                print(f"{book.title} by {book.author} ({book.isbn}) \u2014 {book.available_copies}/{book.total_copies} available")

        elif choice == "2":
            title_query = input("Enter a title to search for: ")
            results = catalog.search_by_title(title_query)
            if not results:
                print("No matches found.")
            else:
                for book in results:
                    print(f"Found: {book.title} by {catalog.books[0].author}")

        elif choice == "3":
            new_title = input("Title: ")
            new_author = input("Author: ")
            new_isbn = input("ISBN: ")
            copies = int(input("Total copies: ") or "0")
            catalog.add_book(Book(new_title, new_author, new_isbn, copies))
            print("Book added.")

        elif choice == "4":
            checkout_isbn = input("ISBN to check out: ")
            catalog.check_out_book(checkout_isbn)
            print("Checked out successfully.")

        elif choice == "5":
            return_isbn = input("ISBN to return: ")
            catalog.return_book(return_isbn)
            print("Returned successfully.")

        elif choice == "6":
            running = False

        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()
