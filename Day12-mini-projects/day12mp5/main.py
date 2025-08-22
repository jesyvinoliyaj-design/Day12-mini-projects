from library import catalog, search, reader

if __name__ == "__main__":
    print("=== eBook Library Organizer ===")
    while True:
        print("\n1. List eBooks\n2. Add eBook\n3. Search eBook\n4. Open eBook\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            books = catalog.list_ebooks()
            print("Your eBooks:", books if books else "No books found.")
        elif choice == "2":
            path = input("Enter file path of eBook: ")
            print(catalog.add_ebook(path))
        elif choice == "3":
            key = input("Enter search keyword: ")
            results = search.search_ebooks(key)
            print("Matches:", results if results else "No matches found.")
        elif choice == "4":
            name = input("Enter exact filename: ")
            print(reader.open_ebook(name))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
