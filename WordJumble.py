# selectedWord Jumble Game
# Justin Schnees
# Date: 06/03/18
# The computer picks a random selectedWord and then "jumbles" it.
# The player has to guess the original selectedWord.

import random

# Title
print ("""
            Welcome to Word Jumble!

    Unscramble the letters to make a selectedWord.

    (Press the enter key at the prompt to quit.)

""".title())

# Begin the game
def main():
    print ("Would you like to play the game?")
    userPrmpt = input("Type yes to continue or no to quit ")
    if userPrmpt.isalpha(): 
        if userPrmpt.lower() == "yes":
            playGame()
        else:
            print("OK Bye ^^/")
            input("Press the Enter to Exit program")
    else:
        print("Please only enter a-z letters\n")
        userPrmpt = input("Type yes to continue or no to quit ")

def playGame():
    # create a sequence of selectedWords to choose from
    WORDS = ("bark", "airplane", "starfish", "nail", "python", "alligator", "house", "factory"
    "stain", "mist", "organize", "dressing", "dressing", "dressing", "visit", "energy", "collect", "neutral",
    "delivery", "pupil", "cotton", "argument", "split", "cooperate", "shark")

    # pick one selectedWord randomly from the sequence
    global selectedWord
    selectedWord = random.choice(WORDS)

    # create a variable to use later to see if the guess is correct
    correct = selectedWord

    # create a jumbled version of the selectedWord
    global jumble
    jumble = ""

    # move the positions of the selectedWords characters around - len means length
    # randomize the selected word by analyzing the length
    while selectedWord:
        position = random.randrange(len(selectedWord)) 

        jumble += selectedWord[position]

        selectedWord = selectedWord[:position] + selectedWord[(position + 1):]

    # show the selected jumbled selectedWord
    # .title capitalizes each word .join adds a space between each letter
    print ("\nThe jumble:".title(), " ".join(jumble))

    # user prompt
    guess = input("\nYour guess: ")

    # make sure user input is lower case
    guess = guess.lower()

    while (guess != correct) and (guess != ""):
        print ("\nSorry, that's not it.\n")
        # user prompt
        guess = input("Your guess: ")
        guess = guess.lower()
        
    # if the user guesses correctly
    if guess == correct:
        print("\nThat's it! You guessed it!")
        print("\nThanks for playing.")
        
        # prompt the user if they want to play again
        playAgain = input("Would you like to play again? ")

        # start game again if user says yes
        if playAgain == "yes":
            playGame()
        else:
            print("Ok have fun!")
            input("Press the Enter to Exit program")

# start the game
main()
