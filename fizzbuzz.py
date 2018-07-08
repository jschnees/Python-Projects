"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number 
and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""
x = range(1, 101)

for y in x:
    if y % 3 == 0 and y % 5 == 0:
        print ("Fizz Buzz")
    elif y % 5 == 0:
        print ("Buzz")
    elif y % 3 == 0:
        print ("Fizz")
    else:
        print (y)
