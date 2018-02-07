###############################################################################
# Brandon Nay
# Stock Portfolio Part 1
###############################################################################
# In this assignment you will build the first part of a stock portfolio manager
###############################################################################

#####################################################
# Your program should have the following functions: #
#####################################################


# addName - Asks the user for a Stock Symbol and Name pairing then adds it to
#    the Names dictionary.
def add_name():
    pass


# addPrices - Takes a Stock Symbol as an input parameter, then asks the user
#    for the Buy price and the Current price of the corresponding stock, adding
#    them to the Prices dictionary.
def add_prices():
    pass


# Takes a Stock Symbol as an input parameter, then asks the user for the Risk
#    and Shares of the corresponding stock, adding them to the Exposure
#    dictionary.
def add_exposure():
    pass


# Calls addName, addPrices, and addExposure to add a new stock to the portfolio
def add_stock():
    pass


# create 2 stocks which means 2 entries in each dictionary with the key in each
#    dictionary being the stock symbol.  Then, the program should display all
#    the information for each stock.
def main():
    pass


###############################################################################

#######################################################
# The manager program will consist of 3 dictionaries. #
#######################################################

# The first dictionary, called Names, maps the stock symbol to the company name
#    (example: "GM" maps to "General Motors").
Names = {"GM": "General Motors",
         }

# The second dictionary, called Prices, maps the stock symbol to a list of 2
#    floating point numbers corresponding to the buy price (the price the user
#    paid for the stock) and the current market price (the price the user could
#    sell the stock for today).
Prices = {}

# The third dictionary, called Exposure, maps the stock symbol to a list of 2
#    floating point numbers, corresponding to the number of shares purchased,
#    and the risk associated with holding onto the stock (i.e. How likely the
#    stock is to gain value in the future). The risk associated with holding
#    onto the stock should be a percentage (the stock is high risk so the
#    exposure value would be .5 or the stock is low risk so the exposure value
#    would be .05)
Exposure = {}

###############################################################################


main()  # execute
