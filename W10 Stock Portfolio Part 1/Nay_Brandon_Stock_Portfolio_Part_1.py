###############################################################################
# Brandon Nay
# Stock Portfolio Part 1
###############################################################################
# In this assignment you will build the first part of a stock portfolio manager
###############################################################################

#####################################################
# Your program should have the following functions: #
#   add_name()                                      #
#   add_prices()                                    #
#   add_exposure()                                  #
#   add_stock()                                     #
#   main()                                          #
#####################################################


# Asks the user for a stock symbol and name pairing then adds it to the Names
# dictionary.
def add_name():
    n_error = '\nNumbers and special characters not allowed.'

    # Get stock symbol
    while True:
        try:
            n_symbol = str(input("Enter a stock symbol: "))
        except ValueError:
            print(n_error)
            continue
        else:
            if n_symbol == '':
                print(n_error)
                continue
            else:
                if n_symbol.isalpha():
                    break
                else:
                    print(n_error)
                    continue

    # Get name
    while True:
        try:
            n_name = str(input("Enter the company name corresponding"
                               "to the symbol you just entered: "))
        except ValueError:
            print(n_error)
            continue
        else:
            if n_name == '':
                print(n_error)
                continue
            else:
                if n_name == n_symbol:
                    print('\nName cannot be the same as the symbol.')
                    continue
                else:
                    if n_name.isalpha():
                        break
                    else:
                        print(n_error)
                        continue

    global Names
    Names[n_symbol] = n_name   # add symbol and name to dict
    return n_symbol


# Takes a stock symbol as an input parameter, then asks the user for the Buy
#    price and the current price of the corresponding stock, adding them to the
#    Prices dictionary.
def add_prices(symbol):
    p_error = '\nPlease enter a dollar amount (x.xx).'

    # Get buy price
    while True:
        try:
            buy_price = float(input('What was the buy price for this companies'
                                    'stock when you purchased it? '))
        except ValueError:
            print(p_error)
            continue
        else:
            break

    # Get current price
    while True:
        try:
            current_price = float(input('What is the current buy price of'
                                        'this companies stock? '))
        except ValueError:
            print(p_error)
            continue
        else:
            break

    p_list = (buy_price, current_price)

    global Prices
    Prices[symbol] = p_list     # add list to Prices dict


# Takes a Stock Symbol as an input parameter, then asks the user for the Risk
#    and Shares of the corresponding stock, adding them to the Exposure
#    dictionary.
def add_exposure(symbol):
    global Exposure


# Calls addName, addPrices, and addExposure to add a new stock to the portfolio
def add_stock():
    s_symbol = add_name()
    add_prices(s_symbol)
    add_exposure(s_symbol)


# create 2 stocks which means 2 entries in each dictionary with the key in each
#    dictionary being the stock symbol.  Then, the program should display all
#    the information for each stock.
def main():
    for x in range(2):
        add_stock()
    # print statements


###############################################################################

#######################################################
# The manager program will consist of 3 dictionaries. #
#######################################################

# The first dictionary, called Names, maps the stock symbol to the company
#    name (example: "GM" maps to "General Motors").
Names = {}      # {'GM':'General Motors'}

# The second dictionary, called Prices, maps the stock symbol to a list of 2
#    floating point numbers corresponding to the buy price (the price the user
#    paid for the stock) and the current market price (the price the user could
#    sell the stock for today).
Prices = {}     # {'GM':floats_list}

# The third dictionary, called Exposure, maps the stock symbol to a list of 2
#    floating point numbers, corresponding to the number of shares purchased,
#    and the risk associated with holding onto the stock (i.e. How likely the
#    stock is to gain value in the future). The risk associated with holding
#    onto the stock should be a percentage (the stock is high risk so the
#    exposure value would be .5 or the stock is low risk so the exposure value
#    would be .05)
Exposure = {}   # {'GM':floats_list}

###############################################################################


main()  # execute
