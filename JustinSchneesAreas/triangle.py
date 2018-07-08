# Triangle Module for Area Calculator
# Justin Schnees
# Date: 06/12/18

def areaTri():
    """ find area of a triangle """

    # user instructions
    print ('\nTo find the area of a Triangle, enter the base and height below.')
    
    # decleration of local variables
    b = 0
    h = 0
    
    # user input with error handling        
    while b <= 0:
        try:
            b = float(input('Base: '))
            if b <=0:
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
    triArea = (b * h)*.5

    # print results
    print ('Width =', b, 'Height =', h)
    print ('The area of a triangle is =', triArea)

def perTri():
    """ find perimeter of a Triangle """

    # user instructions
    print ('\nTo find the area of a Triangle, enter the base and height below.')
    
    # decleration of local variables
    a = 0
    b = 0
    c = 0
    
    # user input with error handling

    while a <= 0:
        try:
            a = float(input('Side 1: '))
            if a <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
                
        while b <= 0:
            try:
                b = float(input('Side 2: '))
                if b <=0:
                    print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")

    while c <= 0:
        try:
            c = float(input('Side 3: '))
            if c <=0:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

    # do the math
    triPerim = a + b + c

    # print results
    print ('Side 1 =', a, 'Side 2 =', b, 'Side 3 =', c)
    print ('The perimeter of a Triangle is =', triPerim)
