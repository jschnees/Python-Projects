# Circle Module for Area Calculator
# Justin Schnees
# Date: 06/12/18

def areaCir():
    """ find area of a cricle """

    # user instructions        
    print ('To find the Area of a Circle, enter the Tadius below.')

    # decleration of local variables
    radiusInput = 0

    # user input with error handling
    while radiusInput <= 0:
        try:
            radiusInput = float(input('Radius: '))
            if radiusInput <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
            
    # do the math
    circleArea = 3.14 * (radiusInput * 2)

    # print results
    print ('Radius =', radiusInput)
    print ('The area of a circle is =', circleArea)

def perCir():
    """ find perimeter of a circle """

    # user instructions        
    print ('To find the Perimeter of a Circle, enter the Radius below.')

    # decleration of local variables
    radiusInput = 0

    # user input with error handling
    while radiusInput <= 0:
        try:
            radiusInput = float(input('Radius: '))
            if radiusInput <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
            
    # do the math
    circleArea = 3.14 * radiusInput * 2

    # print results
    print ('Radius =', radiusInput)
    print ('The perimeter of a circle is =', circleArea)
