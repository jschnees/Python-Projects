# Useless Trivia
# Justin Schnees
# Date: 05/30/18
# Gets personal information from the user and then
# prints true but useless information about him or her
# I added extra trivia to the program.

# Title
print("The Useless Trivia Program\n")

# Ask for users name
name = input("Hi.  What's your name? ")

# Ask for users age, then convert the string into an integer
age = nput("How old are you? ")
age = int(age) 

# Ask for the users weight and convert to an integer on input
weight = int(input("Okay, last question.  How many pounds do you weigh? "))

# Print the user inputs name in ee cummings format - lower then upper
print("\nIf poet ee cummings were to email you, he'd address you as",
      name.lower())
print("But if ee were mad, he'd call you", name.upper())

# Print the users name 5 times
called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:\n" + called)

# Calculate the users age in seconds
seconds = age * 365 * 24 * 60 * 60
minutes = age * 365 * 24 * 60
hours = age * 365 * 24
days = age * 365 
months = age * 12

print("\nYou're over", seconds, "seconds,", minutes, "minutes", hours, "hours", days, "days", months, "months, old")

# Calculate the users weight on the moon
moon_weight = weight / 6
round(moon_weight)

moon_kg = moon_weight * 0.4536
round(moon_kg)
print("\nDid you know that on the Moon you would weigh only",
      round(moon_weight), "pounds or ", moon_kg, "in kilograms")

sun_weight = weight * 27.1
round(sun_weight)

sun_kg = sun_weight * 0.4536
round(sun_kg)

print("On the Sun, you'd weigh", sun_weight, "pounds or ", round(sun_kg), "in kilograms...(but, ah... not for long).")

# Calculate the users weight on the mars - rounding the weight to whole numbers
mars_weight = weight / .38

mars_kg = mars_weight * 0.4536

print("\nDid you know that on the Mars you would weigh only",
      round(mars_weight), "pounds or", round(mars_kg), "in kilograms")

input("\n\nPress the enter key to exit.")
