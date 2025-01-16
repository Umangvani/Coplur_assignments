

class Book():
    def __init__(self, BookID:int, Title:str, Author:str):
        if not Title or not Author:
            raise ValueError("Title or authore not define")
        
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.is_available = True
        
    def __str__(self):
        return f"ID: {self.BookID}, Title: {self.Title}, Author: {self.Author}, Available: {'Yes' if self.is_available else 'No'}"

        
class Library():
    def __init__(self):
        self.Books = {}

    
    def addBook(self, BookID:int, Title:str, Author:str):
        
        if BookID in self.Books:
            print(f"Error: Book ID {BookID} already exists.")
            return
        
        try:
            book = Book(BookID, Title, Author)
            self.Books[BookID] = book
            print(f"Book added: {book}")
            
        except ValueError as e:
            print(f"Error: {e}")
        
                
    def BorrowBook(self, BookID:int):
        
        if BookID not in self.Books:
            print(f"Error: Book ID {BookID} does not exist.")
            return 
        
        book = self.Books[BookID]
        
        if not book.is_available:
            print(f"Error: Book ID {BookID} is already borrowed.")
            return
        
        book.is_available = False
        print(f"Book borrowed: {book}")
        
    
    def returnBook(self, BookID: int):
        
        if BookID not in self.Books:
            print(f"Error: Book ID {BookID} does not exist.")
            return
        
        book = self.Books[BookID]
        if book.is_available:
           print(f"Error: Book ID {BookID} was not borrowed.")
           return

        book.is_available = True
        print(f"Book returned: {book}")
        
    def viewBooks(self):
        available_books = [book for book in self.Books.values() if book.is_available]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:\n")
            for book in available_books:
                print(f"ID: {book.BookID}, Title: {book.Title}, Author: {book.Author}, Available: {'Yes' if book.is_available else 'No'}")


if __name__== "__main__":
    
    library = Library()
    
    #adding book
    library.addBook(101, "Shape of Things to Come", "H.G Wells")
    library.addBook(102, "Alice in Wonderland", "Lewis Carroll")
    library.addBook(103, "The Room on the Roof", " Ruskin Bond")
    
    
    #borrowBook form Libracy
    library.BorrowBook(103)
    
    #return Book into library
    library.returnBook(102)
    
    #view available Book
    library.viewBooks()
    