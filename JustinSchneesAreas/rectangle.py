# Rectangle Module for Area Calculator
# Justin Schnees
# Date: 06/12/18

def areaRect():
    """ find area of a rectangle or square """

    # user instructions
    print ('\nTo find the Area of a Rectangle, enter the width and height below.')
    
    # decleration of local variables
    w = 0
    h = 0
    
    # user input with error handling
    while w <= 0:
        try:
            w = float(input('Width: '))
            if w <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
            
    while h <= 0:
        try:
            h = float(input('Height: '))
            if h <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

    # do the math
    rectangleArea = w * h

    # print results
    print ('Width =', w, 'Height =', h)
    print ('The area of a Rectangle is =', rectangleArea)

def perRectangle():
    """ find perimeter of a rectangle or square """

    # user instructions
    print ('\nTo find the Perimeter of a Rectangle, enter the width and height below.')
    
    # decleration of local variables
    w = 0
    h = 0
    
    # user input with error handling
    while w <= 0:
        try:
            w = float(input('Width: '))
            if w <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
            
    while h <= 0:
        try:
            h = float(input('Height: '))
            if h <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

    # do the math
    recPer = 2*(w * h)

    # print results
    print ('Length =', w, 'Width =', h)
    print ('The perimeter of a Rectangle is =', recPer)
