class Library:
    def __init__(self,listofbook):
        self.book=listofbook

    def displayAvailableBooks(self):
        print("The books available are: ")
        for book in self.book:
            print("*",book)

    def borrowbook(self,bookname):
        if bookname in self.book:
            self.book.remove(bookname)
            print(f"you borrow book name is {bookname} please keep it safe and return after 30 dyas...Thank you.. ")
            return True

        else:
            print("the book is not available yet keep trying within 2-3 dyas...Thank you...")     
            return False  

    def returnBook(self,bookname):
        self.book.append(bookname)
        print("Thanks for returning or adding  a book hope you are enjoy ....keep reading...")


class Student:
    def reqBook(self):
        self.book=input("Enter a name a book you want to borrow..:  ")
        return self.book
    def returnBook(self):
        self.book=input("Enter a name a book you want to return..:  ")
        return self.book

if __name__=="__main__":
    centralLibrary=Library(["PYTHON","C++","C","HTML","JAVA","JAVASCRIPT"])
    student=Student()
    while(True):
        
        welcome_message='''====Welcome to CENTRAL LIBRARY====
        please read a instruction press a no. acoordingly
        1. List of book
        2. borrow a book
        3. return a book
        4. exit a library 
        
    '''
        print(welcome_message)  
        a=int(input("enter a choice:   "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowbook(student.reqBook())    
        elif a==3:
            centralLibrary.returnBook(student.returnBook()) 
        elif a==4:
            exit()
        else:
            print("invalid choice...")               
        

