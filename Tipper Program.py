# Tipper Program
# Justin Schnees
# Date: 05/30/18
# Simple tip calculator for a resturant bill

# Title
print("The Tipper program\n")

# Inputing the amount without a tip
bill_total = float(input("Please enter the total dollar amount of the bill: "))

# caculating the tip
total_15 = (bill_total * 0.15) + bill_total
total_20 = (bill_total * 0.20) + bill_total

# Show the user the bill - the total is formmted for currency 
print(
      "\nThe bill came to: ", '${:,.2f}'.format(total_15), " with a 15% tip \
      \nOr \
      \nThe bill came to: ", '${:,.2f}'.format(total_20), " with a 20% tip"
      )

input("\n\nPress enter key to exit")
