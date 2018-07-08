# Word Frequency
# Justin Schnees
# Date: 06/12/18
# ask user to open specific file and count the program counts
# the frequency of words used.

import re
import string

def FindWords():

    userInput = input("\nWhat file would you like to open " )

    frequency = {}

    document = open(userInput, 'r')
    wordString = document.read().lower()
    matchPattern = re.findall(r'\b[a-z]{3,15}\b', wordString)
     
    for word in matchPattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
         
    frequencyList = frequency.keys()
     
    for words in sorted(frequencyList):
        print (words, frequency[words])
    RestartProgram()

def RestartProgram():
    """ ask the user if they want to restart the program, if yes then call UserPrompt """
    RunAgain = input("\nWould you like to load a new file?: y/n " )
    # start again if user says yes
    if RunAgain == ("y"):
        FindWords()
    else:
        print("Ok have fun!")

def Title():
    """Welcome the user and explain purpose"""
    print("\t\tWelcome to Word Frequency Reader!\n")
    print("Enter the file name with the .txt extention to get started")
    print("\nExample: words.txt")

    
# start the program
Title()
FindWords()
