import listsplit
import borrowBook
import returnBook
import displaystock

#creating function library_
def library_():
    print("\n\t\t    Junkiree's Library ")
    print("\t\t"+"="*30 + "\n")
    print("\t\t         Main Menu  ")
    
    print("\t\t  Press A to display a book")
    print("\t\t  Press B to borrow a book")
    print("\t\t  Press C to return a book")
    print("\t\t  Press D to exit")
    print("\t\t"+"="*30 + "\n")
    while True:
        try:
            a = str(input("Select a choice: "))
            a = a.lower()
            assert a == "a" or a == "b" or a == "c" or a == "d"
        except:
            print("\n\t\tPlease input given options only!!")
            continue
        break
    
    if a == "a":
        listsplit.listSplit()  #calling method listSplit()
        displaystock.Display() #calling method Display()
        library_()

    elif a == "b":
        borrowBook.Borrow()   #calling method Borrow()
        library_()

    elif a == "c":
        returnBook.Return()   #calling method Return()
        library_()
        
    elif a == "d":
        print("\t\tThank you for using our library. Good day!")
        print("\t\t  " + "*"*30)
                
library_()
