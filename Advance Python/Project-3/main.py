class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks
    def displayAvailableBooks(self):
        print("The Books present in this library are: ")
        for book in self.books:
            print(" *" + book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print("You have been issues {} .Please return on Time".format(bookname))
            self.books.remove(bookname)
            return True
        else:
            print("This book has already been issued")
            return False

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book.")       

class Student:

    def __init__(self):
        self.booklist = []

    def requestBook(self):
        self.book = input("Enter the name of the book you want to Borrow:")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:")

if __name__ == "__main__":
    centralLibrary = Library(["DSA","OOP","Stat","ML"])
    student = Student()
    
    while(True):
        welcomemsg ='''~~~~Welcome To Central Library~~~~
        Please choose an option
        1.Listing all the Books
        2.Request a book
        3.Return a book
        4.Exit the library
        '''
        print(welcomemsg)
        a = int(input("Enter your choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowbook()
        elif a==3:
            centralLibrary.returnBook()
        elif a==4:
            print("Thanks for using library!")
            exit()
        else:
            print("Enter a valid choice")

        



