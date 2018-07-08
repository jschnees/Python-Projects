# Car Salesman Program
# Justin Schnees
# Date: 05/30/18
# Car Sales Man Program
# Find the total cost of a car

# Title
print("Welcome to the Car Sales Man Program!\n\n")

#Input base amount - using float to account for decimal places
price = float(input("Please enter the base price (in US $) of the car: "))

# Print the base amount
print("\nPrice of the car without taxes: ", '${:,.2f}'.format(price))

# Add fees
# Tax percentance
tax = 0.50

# Licence Fee percentage
license = 0.30

# Dealership car preperation fee
dealer_prep = 100

# Dealership designation fee
dest_charge = 100

# Find the cost of tax and license fees based off original price
totalTax = price * tax
totalLicense = price * license

# Find the total fees
total_fees = totalTax + totalLicense + dealer_prep + dest_charge

# Find the total price of the vehicle 
total_price = (price + total_fees)

# Print the total price with taxes
print("The price of the car with taxes is: ", '${:,.2f}'.format(total_price))

input("\n\nPress the Enter key to exit.")
