#importing os to check the return text file
import os
import listsplit
import dateTime

#creating function to return book
def Return():
    #declaring the global variables
    global without_fine
    global textF
    global fine
    #calling the method listSplit() from listsplit
    listsplit.listSplit()
    
    total_price = 0.0
    print("\n\t\t\t\t\tReturn Process\n")
    while True:
        #handling file not found exception
        try:
            while True:
                name=input("Enter Name of borrower: ")
                if name.isalpha():
                    break
                print("Please input letters from A-Z!!\n")
            
            #initializing borrowtxt with Borrower - name.txt
            borrowtxt="Borrower - " + name + ".txt"
            
            #opening borrow text file to read it's line
            with open(borrowtxt,"r") as f:
                data = f.read()
        except FileNotFoundError:
            print("\t\tYou have not borrowed any book from this name!! \n")
            continue
        break

    #creating text file for the information of returned book
    textF = "Returned by - "+name+".txt"

    #checking if the return file exist or not
    if os.path.isfile(textF):
        print("\t\t You have already returned all the books.")
        return

    #opening the return txt file and writing the details
    with open(textF,"w+")as filereturn:
        filereturn.write("*" *80 + "\n")
        filereturn.write("\t\t     Junkiree's Library Management System\n")
        filereturn.write("*" *80 + "\n")
        filereturn.write("\t\t\t  Library's Return Receipt\n")
        filereturn.write("  Returned by: "+ name+"\n\n")
        filereturn.write("  Date: " + dateTime.getDate()+"   \t\t Time:"+ dateTime.getTime()+"\n\n")
        filereturn.write("|" + "-"*80 + "|" + "\n")
        filereturn.write("| S.N\t\t\tBook Name \t\t\tAuthor name\t\t |\n")
        filereturn.write("|" + "-"*80 + "|" + "\n")
        
    without_fine = 0.0
    count = 1
    for i in range(5):
        #checking if the data has the book name as in the stock or not
        if listsplit.bookName[i] in data:
            without_fine += float(listsplit.price[i])
            listsplit.quantity[i] = int(listsplit.quantity[i]) + 1
            #opening the file to append the details of book borrowed
            with open(textF, "a") as fileRead:
                fileRead.write("| " + str(count) + "\t\t\t" + listsplit.bookName[i] + "\t\t\t" + listsplit.authorName[i] + "\t\t |\n")
                count +=1
                fileRead.write("|\t\t\t\t\t\t\tPrice: NPR."+ str(listsplit.price[i])+"\t         |\n")
                fileRead.write("|" + "-"*80 + "|" + "\n")
            #opening the stock text file to read and write the data
            with open("bookstock.txt", "w+") as fileRead:
                for i in range(5):
                    fileRead.write(listsplit.bookName[i] + "," + listsplit.authorName[i] + "," + listsplit.Pdate[i] + "," + str(listsplit.quantity[i]) + "," + "NPR." + listsplit.price[i] + "\n") 
           
    forDays()   #calling the function forDays()
    
    #opening the borrower text file and printing it in shell
    with open(textF, "r") as retFile:
        print(retFile.read())
    print("\t\tThank you for using our library!")
    
#initializing total price with float value
total_price = 0.0
def forDays():
    #declaring the global variables
    global fine
    global total_price
    fine = 0.0
    #checking the delayed returned book to add fine to it
    while(True):
        try:
            #checking the delayed returned book to add fine to it
            choose = str(input("\t\tIs it more than 10 days of borrowing?\n Press Y for yes and N for no: "))
            #checking if user input Y or N 
            assert choose.upper() == "Y" or choose.upper() == "N"
        except:
            print("\t\tPlease enter as suggested!!!\n")
            continue
        break
    if choose.upper()  == "Y":  
        while True:
            try:
                #asking input for delayed days
                days = int(input("How many days have passed? "))
                #for handling exception if user input negative value for days
                assert days > 0
            except:
                print("\t\tEnter the valid date.")
                continue
            break

        #adding fine Rs 5 per day
        fine = days * 5   
        total_price = without_fine + fine  #total price with fine
        print("Total price: ", total_price)
        #opening the borrow text file to append the fine and total price in it
        with open(textF, "a") as fileRead:
            fileRead.write("|\t\t\t\t\t\t\tFine: NPR."+ str(fine)+"\t         |\n")
            fileRead.write("|\t\t\t\t\t\t\tTotal price: NPR."+ str(total_price)+"   |\n")
            fileRead.write("|" + "-"*80 + "|" + "\n")
    elif choose.upper() == "N":
        print("Total cost: ", without_fine)
        #opening the borrow text file to append the fine and total price in it
        with open(textF, "a") as fileRead:
            fileRead.write("|\t\t\t\t\t\t\tFine: NPR."+ str(fine)+"\t         |\n")
            fileRead.write("|\t\t\t\t\t\t\tTotal price: NPR."+ str(without_fine)+"  |\n")
            fileRead.write("|" + "-"*80 + "|" + "\n")

