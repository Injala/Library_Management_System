import listsplit

#creating function Display()
def Display():
    listsplit.listSplit()   #calling function listSplit()
    print()
    print("\t\t\t\t\tBooks in the library")
    print("+", "-"*110, "+")
    #using .format to give format for table heading
    print("{:<3}{:<5}{:<3}{:<20}{:<3}{:<20}{:<3}{:<20}{:<3}{:<10}{:<3}{:<20}{:<3}".format("|", "S.N", "|", "Book Name" , "|", "Author Name", "|", "Publish Date(A.D)", "|", "Quantity", "|", "Price(for 10 days)", "|"))
    print("+", "-"*110, "+")
    number = 1
    for i in range(5):
        #using .format to give format for body of the table
        print("{:<3}{:<5}{:<3}{:<20}{:<3}{:<20}{:<3}{:<20}{:<3}{:<10}{:<3}{:<17}{:<3}".format("|", str(number), "|", listsplit.bookName[i] ,"|", listsplit.authorName[i], "|", listsplit.Pdate[i], "|", listsplit.quantity[i], "| NPR.", listsplit.price[i],"|"))
        print("+",5*"-", "+", 20*"-", "+" , 20*"-", "+", 20*"-", "+", 10*"-", "+", 20*"-", "+")
        #increasing the number for serial number by 1
        number+=1

