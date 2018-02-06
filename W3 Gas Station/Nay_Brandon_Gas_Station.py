#############################################################################################
# Brandon Nay
# Gas Station
#############################################################################################
# You are writing a program for a gas station, and one of the things they need is to be
# able to print out a receipt when someone fills up their car with gas. Your task is to
# write a program that will print a receipt to the screen. (*Note, your program does not
# need to do the math since we have not covered this yet in class, but it does need to
# format the output. See the helpful information section of this page for help with the
# formatting.)
#
# Your receipt should show the following information:
#
# Display the station name and location
# Date of the receipt is being issued/given
# Type of Gas
# Number of Gallons of Gas (a number that is displayed to three decimal places)
# Cost per gallon (this should be a number that is formatted as US currency)
# Total Cost (this should be a number that is formatted as US currency)
# Your receipt program must:
#
# Use at least three literals.
# Use at least three variables.
# The number of gallons, cost per gallon, and total cost should all be displayed on one line.
# Use the str.format() method to format all of your output.
# Display all required information in a way that is well organized and easy to read.
# Be sure to use comments for both structure of the program and documentation of the code.
#############################################################################################

import datetime as dt

current_date = dt.datetime.now()

STATION_NAME = "Chevron Shell QuickTrip Megaheck"
STATION_LOCATION = "1924 E. Meme St Tempe, AZ 85250"
GAS_TYPES = ["1: standard", "2: unleaded", "3: premium"]


def get_gas_type():

    for i in GAS_TYPES:  # display gas options
        print(i)

    user_selection = int(input("\nEnter # of desired gas type: "))

    if user_selection == 1:  # standard
        gas_price = 2.78
        return gas_price

    elif user_selection == 2:  # unleaded
        gas_price = 2.94
        return gas_price

    elif user_selection == 3:  # premium
        gas_price = 3.03
        return gas_price

    else:
        print("Something went wrong.\n")
        main()


def get_gallons_purchased():
    gallons_purchased = int(input("Enter how many gallons purchased: "))
    return float(format(gallons_purchased, '.3f'))


# In class I was facing that issue of having to call
# 'get_gallons_purchased()' twice, and at the time
# decided I could write half the print statement before
# the total calculation. I ended up instead passing
# them into the variables at the start of main().


def main():
    gas_price = get_gas_type()
    gallons = get_gallons_purchased()
    total_cost = gas_price * gallons

    print("\n\n",
          STATION_NAME, "\n",
          STATION_LOCATION, "\n",
          current_date.strftime("%m/%d/%Y %H:%M"), "\n")
    print("You purchased", str(format(gallons, '.3f')),
          "gallons of gas for $" + str(format(gas_price, '.2f')),
          "per gallon, \nbringing your total cost to $"
          + str(format(total_cost, '.2f')) + ".")


main()  # execute
