class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        try:
            self.file = open(self.filename, "a+")
        except FileNotFoundError:
            print("File not found!")

    def __del__(self):
        if hasattr(self, "file"):
            self.file.close()

    def listBooks(self ):
        self.file.seek(0)
        lines = self.file.readlines()
        for i in lines:
            bInfo = i.strip().split(",")
            bName = bInfo[0]
            bAuthor = bInfo[1]
            print("Book Name:", bName)
            print("Author:", bAuthor)

    def addBook(self):
        bName = input("Enter Book Name: ")
        bAuthor = input("Enter Author's Name: ")
        rYear = input("Enter Release Year: ")
        pageNum = input("Enter Number of Pages: ")

        bInfo = f"{bName},{bAuthor},{rYear},{pageNum}\n"
        self.file.write(bInfo)
        print("Book added!")

    def removeBook(self):
        whichBook = input("Enter the book you want to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        books = [line.strip() for line in lines]
        index = None
        for i, book in enumerate(books):
            if whichBook in book:
                index = i
                break
        if index is not None:
            del books[index]

            self.file.seek(0)
            self.file.truncate()

            for book in books:
                self.file.write(book + "\n")
            print("Book removed!")
        else:
            print("Book not found!")

lib = Library()

# Menü
while True:

    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.listBooks()
    elif choice == "2":
        lib.addBook()
    elif choice == "3":
        lib.removeBook()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")