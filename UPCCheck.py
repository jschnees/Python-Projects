# Justin Schnees
# Date: 06-11-18
# Check Digit Validation
# The UPC-A check digit may be calculated as follows:
# https://en.wikipedia.org/wiki/Universal_Product_Code
#Sum the odd-numbered digits.
#Multiply the result by 3.
#Add the even-numbered digits.
#Find the result modulo.
#If M is not 0, subtract M from 10.
# barcodes for testing  074590508994 376045004149 021500074506

def userInput():
    """ prompt the user if they want to play again """

    userUPC = input("Enter 12-digit UPC-A barcode: ")
    while len(userUPC)!=12:
      print("Invalid UPC-A barcode.")
      userUPC = input("Re-enter 12-digit UPC-A barcode: ")
    return userUPC

def findUPC():
    """ this finds the positions of the digits in the UPC entered (userUPC)"""
    userUPC = userInput() # import the user input
    moddedUPC = userUPC[:11] + userUPC[12:] # remove the 12th character
 
    # set variables
    odd_sum = 0
    even_sum = 0
    totalMOD = 0

    # add even and odd numbers
    for i, char in enumerate(moddedUPC):
        j = i+1
        if j % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    # do the math - multiple odd by 3 and add he even sum
    total_sum = (odd_sum * 3) + even_sum
    # mod total
    totalMod = total_sum % 10

    #check if totalMod is greater than 0 subtract total from 10
    if totalMod >= 0:
        checkValid = 10 - totalMod # if total mod is greater than 0, subtract from 10
        if checkValid == int(userUPC[11]): # if the total (checkvalid) is the same as the last barcode number
            print ("Your UPC " + userUPC + " is Valid")
        else: # if checkValid isn't the same then it isn't valid
            print ("Your UPC " + userUPC + " is Invalid")
     # reload the program
    findUPC()
    
# initialize the program
findUPC()
