#automated check writing system
#converts numerical input to English words

    
#TRIPLET CREATOR SECTION-----------------------------------------
#given a list of numbers and an iterator,
#print out the matching word for each given number at the iterator's position
#check if there are 3 digits, if so, print "hundred" after first num
#check also for special cases, like "eleven"
def NumberClump(digits, i):
    
    if digits[i] !=0:
        if digits[i-1] != 1 and digits[i-1] !=0:
            print(words.get(digits[i]), "hundred", tens.get(digits[i-1]), words.get(digits[i-2]), end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==0:
            print(words.get(digits[2]), "hundred and ten", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==1:
            print(words.get(digits[2]), "hundred and eleven", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==2:
            print(words.get(digits[2]), "hundred and twelve", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==3:
            print(words.get(digits[i]), "hundred and thirteen", end = '')
    
        elif digits[i-1] == 1:
            print(words.get(digits[i]), "hundred",  words.get(digits[i-2])+ tens.get(digits[i-1]), end = '')
            
    elif digits[i-1] !=0:
        if digits[i-1] != 1 and digits[i-1] !=0:
            print( tens.get(digits[i-1]), words.get(digits[i-2]), end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==0:
            print("ten", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==1:
            print("eleven", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==2:
            print("twelve", end = '')
    
        elif digits[i-1] == 1 and digits[i-2]==3:
            print("thirteen", end = '')
    
        elif digits[i-1] == 1:
            print(words.get(digits[i-2])+ tens.get(digits[i-1]), end = '')
    else:
        print(words.get(digits[i-2]), end = '')

#WORD-NUMBER MATCHES--------------------------------------------
#the first dictionary matches numbers with their English word counterparts
#the second dictionary matches multiples of ten with their words.
words = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
    }

tens = {
    1:"teen",
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"nintey"
    }


#TRIPLET CLUMPER SECTION----------------------------------------------
#this section slices up a number and puts it into a list one number at a time
#it also stores any decimal value to be printed as a fraction at the end
#it appends extra 0s so the number clump function doesn't have an out of bounds
#it then calls the number clump function the appropriate number of times
#linking triples with words like "thousand" and "million"

def NumberCrunch(num):
    amount = int(num)
    #slice number into individual digits, store into list
    digits = []
    i = 1
    while amount>=1: #keep collecting digits for any sized number
        digits.append(amount%10)
        num -= (amount%10)* i 
        amount = amount//10
        i*=10
        
    #turn remaining change into non-decimal numbers
    num = round(num, 2)
    num = num * 100

    #add 0s to make sure list is divisible by 3
    if len(digits)%3 == 2:
        digits.append(0)
    elif len(digits)%3==1:
        digits.append(0)
        digits.append(0)

    #print for testing purposes
    #print(digits)

    #print millions
    if len(digits)>6:
        NumberClump(digits, 8)
        print(" million, ", end = '')

    #print thousands
    if len(digits)>3:
        NumberClump(digits, 5)
        print(" thousand, ", end = '')

    #hundreds
    NumberClump(digits, 2)
    print(" dollars and", int(num),"/ 100")

#main---------------------------------------------------------
#this section sets up a game loop and repeatedly calls the
#number crunch function until the user types "0"
    
doExit = False
print("-------------------------------------------------------")
print("Welcome to the Auto Check Writing Program!")
while doExit == False:
    num = float(input("\n\nPlease enter dollar amount for check, 0 to quit:"))
    if num !=0:
        NumberCrunch(num)
    else:
        print("Thank you for using the Auto Check Writing Program!")
        doExit = True
        
print("goodbye!")
