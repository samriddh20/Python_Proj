# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and showhow you can print all 
# books, add abook and gett the number of books using different method.

class Library:
    def __init__(self, book_l):
        self.book = book_l
        self.no = len(book_l)
        
        
    def show(self):    
        for i in self.book:
            print(f"{i}")
    
    def add(self, new_book):
        self.book.append(new_book)
        self.no = len(self.book)
        print(f"\n'{new_book}' has been added to the library")

    def total_books(self):
        return f"\nTotal no of books are : {self.no}"


print(type(Library.book))
my_library = Library(["Atomic Habits", "Rich Dad Poor Dad", "The Alchemist"])
my_library.show()
print(my_library.total_books())


my_library.add("GOT")
my_library.show()
print(my_library.total_books())