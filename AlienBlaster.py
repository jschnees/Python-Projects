# Alient Blaster
# Justin Schnees
# 07 - 05 - 18
# Alien Translator https://lingojam.com/AlienLanguage
import time
from time import sleep
import sys
import random

class Blaster(object):
    """ print out a fancy blaster for effect"""
    def Pew(self):            
        print("""
              __,_____
             / __.==--" ~~~~~
            /#(-'
            `-'
        """)

class Soldier(object):
    """ Soldier Actions"""
    # initialize 
    def __init__(self, health, ammo):
        self.health = health
        self.ammo = ammo
        self.lose = False

    # blaster action
    def blast(self, enemy):
        pewpew = Blaster() # loads the blaster
        time.sleep(2)  # Delay the action for 2 seconds
        if self.lose:
            print("You were unsuccessful and did not kill the alien!\n They retaliate and a war begins.")
        else:
            print("The soldier blasts an enemy.")
            pewpew.Pew() # prints the blaster
            if self.ammo > 0:
                self.ammo -= 1
                print("Ammo" , str(self.ammo))
                print("The alien took 1 damage!\n")
                enemy.die()
            else:
                if enemy.health == 0:
                    print("They're already dead, yo.")
                else:
                    self.lose = True
                    print("The alien has more health than you have ammo.")
                    print("You run out of ammo and die!")
                    
    def die(self):
        if self.health > 1:
            self.health -= 1
            print("Is that all you've got??\n")
        elif self.health == 1:
            self.health -= 1
            print("*Space Force soldier cries out* Oh no! I'm gonna die")
        else:
            print("The alien is already dead.  What you're doing is unneccessary.")

class Alien(object):
    """ An alien in a shooter game. """
    # initialize 
    def __init__(self, health, ammo):
        self.health = health
        self.ammo = ammo
        self.lose = False

    def blast(self, enemy):
        pewpew = Blaster() # loads the blaster
        time.sleep(2)  # Delay the action for 2 seconds
        if self.lose:
            print("You were unsuccessful and did not kill the alien!\n They retaliate and a war begins.")
        else:
            print("The alien blasts the enemy.")
            pewpew.Pew() # prints the blaster
            if self.ammo > 0:
                self.ammo -= 1
                print("Ammo" , str(self.ammo))
                print("The enemy took 1 damage!\n")
                enemy.die()
            else:
                if enemy.health == 0:
                    print("They're already dead, yo.")
                else:
                    self.lose = True
                    print("The enemy has more health than you have ammo.")
                    print("You run out of ammo and die!")
        def die(self):
            if self.health > 1:
                self.health -= 1
                print("Is that all you've got??\n")
            elif self.health == 1:
                self.health -= 1
                print("*Space Force Soldier cries out* Oh no! I'm gonna die!")
                raise SystemExit(0)
            else:
                print("The enemy is already dead.  What you're doing is unneccessary.")

    def die(self):
        """ what happens when the alien dies"""
        if self.health > 1:
            self.health -= 1
            print("Is that all you've got??\n")
        elif self.health == 1:
            self.health -= 1

            def print_slowly(text):
                """ This prints out the translation text slowly for effect"""
                for c in text:
                    print(c, end=''),
                    sys.stdout.flush()
                    sleep(0.125)
                        
            print("*Alien cries out*")
            print("⊑⟒⌰⌿ ⟟⋔ ☌⍜⟟⋏☌ ⏁⍜ ⎅⟟⟒! ⍙⊑⊬ ⎅⟟⎅ ⏁⊑⟒⊬ ⏃⏁⏁⏃☊☍!?")
            print_slowly("\nTranslation: \"Help i'm going to die! Why did they attack!?\"")
            #raise SystemExit(0)
    
        else:
            print("The alien is already dead.  What you're doing is unneccessary.")

class Main(object):
    def Title(self):
        print("""
         ____  ____  ____  ____  _____   _____ ____  ____  ____  _____
        / ___\/  __\/  _ \/   _\/  __/  /    //  _ \/  __\/   _\/  __/
        |    \|  \/|| / \||  /  |  \    |  __\| / \||  \/||  /  |  \  
        \___ ||  __/| |-|||  \__|  /_   | |   | \_/||    /|  \__|  /_ 
        \____/\_/   \_/ \|\____/\____\  \_/   \____/\_/\_\\____/\____\\
        \n\n
        \tWe enter as the hero(?) of the story
        Encounters an unknown life form and a battle ensues
        """)


    def Actions(self):

        time.sleep(2)  # Run after 3 seconds
        times = 10 # number of times in shoot
        hero = Soldier(times,times)
        invader = Alien(times,times)

        while hero.health > 0 and invader.health > 0:
            #for i in range(times):
                # pick who shoots first
            val = random.randint(0,1)
            if val == 0:
                hero.blast(invader)
            else:
                invader.blast(hero)
                    
# run the main program
run = Main()
run.Title()
run.Actions()


input("\n\nPress the enter key to exit.")
