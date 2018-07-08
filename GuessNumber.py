# Justin Schnees
# Date: 05/30/18
# This is a guess the number game.
import random

# randomize the number
the_number = random.randint(1, 100)

# initialize the tries variable
tries = 1
# Title
print("\tWelcome to 'Guess My Number'!")

# Prompt - Directions
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Ask the user to pick a number
guess = int(input('Guess what number I am thinking of: '))

# While loop to run the progam until end

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    
    # Counts the number of tries
    tries += 1 

# Print results                 
print("\nYou guessed it! The number was", the_number)
print("And it only took you", tries, "tries!")

# Close program
input("\n\nPress the Enter key to exit.")
