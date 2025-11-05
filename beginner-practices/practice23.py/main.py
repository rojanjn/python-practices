from mylibrary.library import Library

def menu():
    library = Library()

    while True:
        print("---Library Menu---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(title, author)
            print("Book added.")

        elif choice == "2":
            title = input("Book title to remove: ")
            if library.remove_book(title):
                print("Book removed.")
            else:
                print("Book not found")
                
        elif choice == "3":
            title = input("Book title to search: ")
            result = library.search_book(title)
            if result:
                print(f"Found: {result}")
            else:
                print("Book not found.")

        elif choice == "4":
            print("Books in library:", library.show_books())
            
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
