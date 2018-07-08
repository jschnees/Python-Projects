# Reverse phrase program
# Justin Schnees
# Date: 06/04/18

# Slicing
# If there is no value before the first colon, it means to start at the beginning index of the list.
# If there isn't a value after the first colon, it means to go all the way to the end of the list.
# -1 means to increment the index every time by -1, meaning it will traverse the list by going backwards.

#Title
print ("Type a word or phrase and view it backwards\n".title())
print ("")

print ("Option 1")
print("(This uses the slice method)\n")

userInput1 = input("Enter a string: ")

print ("The original string is : ",userInput1)
print ("The reversed string is : ", userInput1[::-1])

# Python code to reverse a string 
# using loop

print ("\n\nOption 2")
print("(This uses a for loop)\n")

def reverse(userInput2):
  str = ""
  for i in userInput2:
    str = i + str
  return str
 
userInput2 = input("Enter a string: ")
 
print ("The original string is : ",userInput2)

print ("The reversed string is : ", reverse(userInput2))

