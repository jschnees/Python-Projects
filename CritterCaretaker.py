# Justin Schnees
# 06-28-18
# Critter CareTaker

import random

class Critter(object):
    """A virtual pet"""
    # generate random hunger and mood
    x = random.randint(1,20)
    y = random.randint(1,20)

    def __init__(self, name, hunger = x, boredom = y):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom


    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1


    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        """ displays the mood of your critter"""
        print(self.name, "feels", self.mood(), "\n")
        self.__pass_time()


    def eat(self, food = 1):
        """ Critter reaction when its fed """
        print("*chitters with glee*")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()


    def play(self, fun = 1):
        """ Critter reaction when you play with it """
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def Menu():
    """ display menu options """
    print("""
    What would you like to do with your pet?
    
    0 - Quit
    1 - Listen to your critter
    2 - Feed your critter
    3 - Play with your critter
    """)


def main():
    """ main part of program - display menu and reactions """
    crit_name = input(" \nWhat do you want to name your critter?: ")
    crit = Critter(crit_name)

    print("You've just brought home", crit_name, "and it's nervous and scared",)

    print("""
          .   .
           \ /
         `/ ! \`
         | o:o |
        ~| o:o |~
        / \_:_/ \        \n

          """)

    Menu() # display menu

    choice = None #initate choice variable
    while choice != "0":

        choice = input("Choice: ") # user prompt for action selection
        
        # exit
        if choice == "0":
            print("Bye Anon!")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # Asks the user how much they want to feed their critter
        # Passes the input through our method
        elif choice == "2":
            food = int(input("How much food would you like to feed your critter?: "))
            if food > 5:
                print("That is too much. You don't want to make your critter fat! ")
            elif food == 0:
                print(crit_name, "chitters angrily and wants food")
            else:
                crit.eat(food)
            
        # Asks the user how long they want to play with their critter
        elif choice == "3":
            fun = int(input("How long would you like to play with your critter?: "))
            if fun == 0:
                print("Ok no play time")
            else:
                crit.play(fun)
                print("SQU"+"E"*fun)

        # some unknown choice
        else:
            print("\n", choice, "isn't a valid choice.")
        Menu() # display menu

main()
("\n\nPress the enter key to exit")
