# Justin Schnees
# Coin Toss Program
# 06-29-18
# Prompts the user to play the game
# Coin is tossed

import random
 
class Coin:
    """ initialize variables and create random toss """
    def __init__ (self, coins=20, sideup="Heads"):
        self.sideup = sideup
        self.coins = coins
 
    def toss(self):
        """ randomize coin toss - generate a 0 or 1 """
        val = random.randint(0,1)
        if val == 0:
            self.sideup = "HEADS!"
        else:
            self.sideup = "TAILS!"

def Title():
    print("""
                    Hello Players
     Test your luck on this not so random game of
    ____ ____ _ _  _    ___  ____ ___ ___ _    ____ 
    $    $  $ $ $\ $    $__] $__$  $   $  $    $___ 
    $___ $__$ $ $ \$    $__] $  $  $   $  $___ $___ 
    """)

      
def Main():
    """ main program - decide coin toss results """

    # Run Title of program
    Title()
    
    # recieve coin toss for each player
    c1 = Coin()
    c2 = Coin()
    counter = 0

    # prompt user
    play = input("\nWould you like to play? (y/n): ")

    # if user yes perform coin toss for both players
    while play.lower() == 'y':
        c1.toss() # runs toss function in Coin class
        c2.toss() # runs toss function in Coin class
        
        # player 1 gets 1 coin player 2 loses 1 
        if c1.sideup == c2.sideup:
            c1.coins += 1 # adds 1 to player 1 if player 1 wins
            c2.coins -= 1 # subtracts 1 from player 2 if if player 1 wins
            
            print("\n", c1.sideup , "Player 1 wins") # print result
            
        # player 2 gets 1 coin player 1 loses 1     
        else:
             c1.coins -= 1 # subtracts 1 from player 1 if if player 2 wins
             c2.coins += 1 # adds 1 to player 2 if player 2 wins
             print("\n", c2.sideup , "Player 2 wins") # print result

        counter += 1
        
        # prompt user
        play = input("\nDo you want to continue playing? (y/n): ")
    
        if counter == 5:
            print(f"Game Update: \nAfter 5 turns  \nPlayer 1 has {c1.coins} coins and Player 2 has {c2.coins} coins")
            if c1.coins > c2.coins:
                print ("Player 1 is winning!")
            else:
                print("Player 2 is winning!")
    # print total results
    print(f"\nPlayer 1 has {c1.coins} coins and Player 2 has {c2.coins} coins")

# initialize program
Main()
