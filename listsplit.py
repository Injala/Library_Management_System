#declaring the variables
global bookName
global authorName
global Pdate
global quantity
global price

#creating the empty list
bookName = []
authorName = []
Pdate = []
quantity = []
price = []

#creating function listSplit()
def listSplit():
    
    #opening the bookstock to split each line 
    with open ("bookstock.txt","r") as bookstock:
        
        lines = bookstock.readlines()
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind = 0
            #seperating book name, author name, publish date, quantity and price and giving index number to them
            for a in lines [i].split(','):
                if ind==0:
                    bookName.append(a)
                elif ind == 1:
                    authorName.append(a)
                elif ind == 2:
                    Pdate.append(a)
                elif ind == 3:
                    quantity.append(a)
                elif ind == 4:
                    price.append(a.strip('NPR.'))
                ind += 1
