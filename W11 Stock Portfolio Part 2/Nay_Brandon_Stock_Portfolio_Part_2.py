###############################################################################
# Brandon Nay
# Stock Portfolio Part 2
###############################################################################
#
###############################################################################


# Asks the user for a stock symbol and name pairing then adds it to the Names
# dictionary.
def add_name():
    n_error = '\n\nNumbers and special characters not allowed.'

    # Get stock symbol
    while True:
        try:
            n_symbol = str(input("\nEnter a stock symbol: "))
        except ValueError:
            print(n_error)
            continue
        else:
            if n_symbol == '':  # error if nothing is entered
                print(n_error)
                continue
            else:
                if n_symbol.isalpha():  # check for special characters and nums
                    break
                else:
                    print(n_error)  # error if numbers or special character
                    continue

    # Get name
    while True:
        try:
            n_name = str(input("\nEnter the company name corresponding"
                               " to the symbol you just entered: "))
        except ValueError:
            print(n_error)
            continue
        else:
            if n_name == '':
                print(n_error)
                continue
            else:
                if n_name == n_symbol:
                    print('\n\nName cannot be the same as the symbol.')
                    continue
                else:
                    if n_name.isalpha():
                        break
                    else:
                        print(n_error)
                        continue

    global Names
    Names[n_symbol.upper()] = n_name    # add symbol and name to dict
    return n_symbol.upper()     # upper() returns all capitals


# Takes a stock symbol as an input parameter, then asks the user for the Buy
#    price and the current price of the corresponding stock, adding them to the
#    Prices dictionary.
def add_prices(symbol):
    p_error = '\n\nPlease enter a dollar amount. (x.xx)'

    # Get buy price
    while True:
        try:
            buy_price = float(input('\nWhat was the buy price for this '
                                    'companies stock when you purchased it? '))
        except ValueError:
            print(p_error)
            continue
        else:
            break

    # Get current price
    while True:
        try:
            current_price = float(input('\nWhat is the current buy price of'
                                        'this companies stock? '))
        except ValueError:
            print(p_error)
            continue
        else:
            break

    p_list = [buy_price, current_price]

    global Prices
    Prices[symbol] = p_list     # add list to Prices dict


# Takes a Stock Symbol as an input parameter, then asks the user for the Risk
#    and Shares of the corresponding stock, adding them to the Exposure
#    dictionary.
def add_exposure(symbol):
    risk_error = '\n\nnPlease enter a percent in decimal form.'
    shares_error = '\n\nPlease enter a number.'

    # Get risk
    while True:
        try:
            risk = format(float(input('\nWhat is the % risk? (.xx) ')), '.2f')
        except ValueError:
            print(risk_error)
            continue
        else:
            break

    # Get shares
    while True:
        try:
            shares = float(input('\nHow many shares do you have? '))
        except ValueError:
            print(shares_error)
            continue
        else:
            break

    e_list = [risk, shares]

    global Exposure
    Exposure[symbol] = e_list   # add list to Exposure dict


# Calls addName, addPrices, and addExposure to add a new stock to the portfolio
def add_stock():
    s_symbol = add_name()
    add_prices(s_symbol)
    add_exposure(s_symbol)
    return s_symbol


# Finds the maximum expected value of selling a stock.
def get_sale(buy_price, current_price, risk, shares):
    step_1 = current_price - buy_price
    expected_sale_value = (step_1 - risk * current_price) * shares
    return expected_sale_value


# create 2 stocks which means 2 entries in each dictionary with the key in each
#    dictionary being the stock symbol.  Then, the program should display all
#    the information for each stock.
def main():
    symbol_list = []

    for x in range(2):
        # Run add_stock and place the stock symbol in symbol_list
        symbol_list.append(add_stock())

    print('\n\n--------------------------')

    # Iterate through symbol_list to print stock information for each company
    for x in symbol_list:
        price_list = Prices[x]      # extract the lists from their dicts
        expo_list = Exposure[x]     # so we can index them
        risk = float(expo_list[0]) * 100    # convert float to actual %

        print('\nCompany name:', Names[x])

        print('\nOriginal stock purchased for $' +
              str(format(price_list[0], '.2f')) + '.')
        print('Current market price ------- $' +
              str(format(price_list[1], '.2f')))
        print('Stocks owned:', expo_list[1])
        print('Risk:', str(risk) + '%')
        print()

    print('--------------------------')


###############################################################################

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
