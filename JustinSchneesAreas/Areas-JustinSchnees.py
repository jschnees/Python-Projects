# Area Calculator
# Justin Schnees
# Date: 06/12/18
# ask user for measurements and get result for areas of basic shapes

def title():
    # welcome and title of program
    print(
        "\t\tWelcome to the Area Calculation App\n"
        "\tPlease select from the options below to get started.\n"
        )
    
def programStart():  
    # print menu
    menu()
    
    # ask user their selection
    choice = input("\nWhat shape would you like to find the area of? ")

    # return the selection
    return choice

def menu():
    """ prints the options for the menu"""
    print (
        "\nFind Areas\n"
        "\t1 Rectangle\n"
        "\t2 Circle\n"
        "\t3 Triangle\n"
        "\nFind Perimeters\n"
        "\t4 Rectangle\n"
        "\t5 Circle\n"
        "\t6 Triangle\n\n"
        "\tq quit the program"
        )
    
# menu options
def menuSelect():
    """" call the options that are selected by the user """
    choice = programStart()
    while choice != "q":
        if choice == "1":
            import rectangle
            rectangle.areaRect()
            menuSelect()
        elif choice == "2":
            import circle
            circle.areaCir()
            menuSelect()
        elif choice == "3":
            import triangle
            triangle.areaTri()
            menuSelect()
        elif choice == "4":
            import rectangle
            rectangle.perRectangle()
            menuSelect()             
        elif choice == "5":
            import circle
            circle.perCir()
            menuSelect()                 
        elif choice == "6":
            import triangle
            triangle.perTri()
            menuSelect()
# load the title screen
title()
menuSelect()
