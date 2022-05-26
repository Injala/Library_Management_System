#importing the module dateTime and listsplit
import dateTime
import listsplit

listsplit.listSplit()   #calling method listSplit from listsplit


# creating function to borrow book
def Borrow():
    #declaring the global variables
    global firstName
    global lastName
    global txtfile
    print()
    print("\n\t\t\t\t\tBorrow Process")
    # checking whether the name of the borrow is alphabet or not
    while True:
        firstName = str(input("Enter your first name: "))
        if firstName.isalpha():  #chechking whether the name is alphabet or not
            break
        print("\t\tPlease input letters from A-Z!!\n")
    while True:
        lastName = input("Enter your second name: ")
        if lastName.isalpha():
            break
        print("\t\tPlease input letters from A-Z!!\n")

    # creating text file for borrowed book details
    txtfile = "Borrower - " + firstName + ".txt"
    forWrite()


# creating function for writing the information in borrower text file
def forWrite():
    with open(txtfile, "w+") as txtFile:
        txtFile.write("\n" + "*" * 80 + "\n")
        txtFile.write("\t\t  Junkiree's Library Management System\n")
        txtFile.write("*" * 80 + "\n")
        txtFile.write("\t\t\t  Library's Borrow Receipt\n\n")
        txtFile.write("  The book is borrowed by - " + firstName + " " + lastName + "\n\n")
        txtFile.write("  Date: " + dateTime.getDate() + "\t\t\t\tTime:" + dateTime.getTime() + "\n\n")
        line_ = "|{:<6} {:<36} {:<36}|\n".format("S.N", "Book Name", "Author Name")
        txtFile.write("|" + "-" * 80 + "|" + "\n")
        txtFile.write(line_)
        txtFile.write("|" + "-" * 80 + "|" + "\n")
    #calling the function displayBookList
    displaybooklist()


# creating function for entering the book code
def displaybooklist():
    global bookChoice
    global user_book_choice
    print("\n\t\t\t     Please select an option below:")
    print("\t\t" + "=" * 60 + "\n")
    for i in range(5):
        # giving the user the book code for them to borrow
        print("\t\t  Enter", i, "to borrow", listsplit.bookName[i], "by", listsplit.authorName[i], "[",
              listsplit.Pdate[i], "]", "\n")
    print("\t\t" + "=" * 60 + "\n")

    while True:
        #exception handling for ValueError, IndexError, AssertionError
        try:  
            bookChoice = int(input("Enter the number of book you want to borrow: "))
            #using assert to check for negative input and non-existed input
            assert bookChoice >= 0
            assert bookChoice <= 4
            user_book_choice = str(listsplit.bookName[bookChoice])
            samebook()
        except:
            print("\n\t\tPlease enter the given code only!!\n")
            continue
        break

count = 1
Total_price = 0.0


# creating function for availability, confirmation, appending and decreasing quantity
def bookstock():
    global count
    global Total_price

    price_bef = 0.0

    price_bef = float(listsplit.price[bookChoice])
    # if the quantity of book selected is zero
    if int(listsplit.quantity[bookChoice]) > 0:
        print("\n\t\t\t\t[Available]")
        print("\tThe price of the book you want to borrow is NPR.", listsplit.price[bookChoice], " for 10 days.", "\n")
        while True:
            try:
                # asking confirmation from user
                question = str(input("Are you sure you want to borrow it? Type Y for yes and N for no: ", ))
                question = question.upper()
                #to check if input value is Y or N
                assert question == "Y" or question == "N"
                if question == "Y":
                    # update the details in the borrower text file
                    with open(txtfile, "a") as file:
                        line_ = "|{:<6} {:<36} {:<36}|\n".format(str(count), listsplit.bookName[bookChoice],listsplit.authorName[bookChoice])
                        file.write(line_)
                        count += 1
                        space = "  "
                        price = "|{:<6} {:<36} {:<36}|\n".format(space, space, "Price: NPR." + str(price_bef))
                        file.write(price)
                        file.write("|" + "-" * 80 + "|" + "\n")
                        Total_price = Total_price + price_bef
                        print("\n\t\tYou have successfully borrowed the book.", "\n")
                        print("\t\t   " + "*" * 30 + "\n")
                    # decreasing the quantity as per the borrow of the book in the selected collection data type and
                    listsplit.quantity[bookChoice] = int(listsplit.quantity[bookChoice]) - 1
                    #reading and writing the text file book stock to update the quantity
                    with open("bookstock.txt", "w+") as file:
                        for i in range(5):
                            file.write(listsplit.bookName[i] + "," + listsplit.authorName[i] + "," + listsplit.Pdate[
                                i] + "," + str(listsplit.quantity[i]) + "," + "NPR." + listsplit.price[i] + "\n")
                    multibook()
                elif question == "N":
                    multibook()

            except:
                print("\t\tPlease input Y/N only!! \n")
                continue
            break
    # if stock is finished
    elif int(listsplit.quantity[bookChoice]) == 0:
        print("\n\t\t\t[Not Available]")
        multibook()


# creating function for borrowing twice    
def multibook():
    #declaring the global variables
    global count
    global Total_price
    global txtfile
    global lines
    while True:
        try:
            # asking for borrowing more books
            option = str(input("\t\tDo you want to borrow other books? \nEnter Y for yes and N for no: "))
            assert (option.lower() == "y" or option.lower() == "n")
            # if user input y call function displaybooklist
            if option.lower() == "y":
                displaybooklist()
            # if user input n append total price to the borrower text file
            elif option.lower() == "n":
                with open(txtfile, "a") as file:
                    file.write("\t\t\tTotal price: NPR." + str(Total_price) + "\n")
                    file.write("|" + "-" * 80 + "|")
                #reading the borrow text file to print it in terminal
                with open(txtfile, "r") as f:
                    lines = f.read()
                print(lines)
                print("\t\tThank you for using our library. Good day! \n")
                print("\t\t     " + "*" * 30)
                return
        except:
            print("\t\tPlease input y/n only!!\n")
            continue
        break


# creating function for borrowing same book
def samebook():
    global user_book_choice
    # opening the borrow txt file and readling lines
    with open(txtfile, 'r') as readdetails:
        detail = readdetails.read()
        # checking for already borrowed book
        if user_book_choice in detail:
            print("\t\tYou have already borrowed the book\n")
            multibook()
        else:
            bookstock() #calling function bookstock()
