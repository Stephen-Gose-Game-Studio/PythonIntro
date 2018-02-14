###############################################################################
# Brandon Nay
# 10 Functions
###############################################################################
# For this assignment you will create and test 10 functions in Python. The 10
# functions that you must create and test are described in detail below.
#
# Be sure that you take  input provided by function 10 for all of your other
# function arguments! If you do not, you cannot properly test them and neither
# can your professor to properly grade your assignment!
###############################################################################


###############################################################################
# 1. A function that displays your name and your major at UAT. The output
#    should look like this:
#        Name: Drale Glacen
#        Major: Advancing Computer Science
###############################################################################
def print_name():
    print('Name:  Brandon Nay\n'
          'Major: Advancing Computer Science')


###############################################################################
# 2. A function that prompts the user to enter their age and returns the user's
#    input as an int.
###############################################################################
def get_age():
    while True:
        try:
            age = int(input('What is your age? '))
        except ValueError:
            print('\nPlease enter a number.')
            continue
        else:
            print('Age is', str(age) + '.')
            return age


###############################################################################
# 3. A function that takes one argument - the argument will be a name that is a
#    string. The function will display a message like this:
#        Hello Drale Glacen!
###############################################################################
def greet_person(name):
    print('Hello', name + '!')


###############################################################################
# 4. A function that takes an integer argument called number and returns the
#    inverse of that number. For example, if you pass it 3, it will return -3,
#    and if you pass it -3 it will return 3
###############################################################################
def return_inverse(number):
    inverse = number * -1
    print('Inverse of', number, 'is', str(inverse) + '.')
    return inverse


###############################################################################
# 5. A function that takes an integer argument called count and a string
#    argument called message. The function will display the message <count>
#    times. For example, if the message is "Hello!" and the count is 3, then
#    the functions will display "Hello!" three times.
###############################################################################
def repeat_message(count, message):
    for x in range(count):
        print(str(x + 1) + '.', message)


###############################################################################
# 6. A function called getBiggest that takes two int arguments called num1 and
#    num2. The function will return the largest of the two argument values. If
#    the arguments are equal, then it will return the first argument value.
###############################################################################
def getBiggest(num1, num2):
    if num1 > num2:
        print(num1, 'is bigger than', str(num2) + '.')
        return num1
    elif num1 < num2:
        print(num2, 'is bigger than', str(num1) + '.')
        return num2
    elif num1 == num2:
        print('Both numbers are equal.')
        return num1

	# Alternative
	# return sorted([num1, num2])[1]

###############################################################################
# 7. A function that takes a string argument and counts and returns the number
#    of capital letters in the argument string. For example, if the argument
#    value is "My name is Albert Einstein.", then the return value will be 3.
###############################################################################
def count_capitals(string):
    capital_count = 0
    for x in string:
        if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            capital_count += 1
    print('String contained', capital_count, 'capital letters.')
    return capital_count


###############################################################################
# 8. A function that takes three int arguments and returns the middle value.
#    for example, if the argument values are 5, 3, and 4, then the function
#    will return 4. If there is no middle value then the function will return
#    the most common value. For example, if the argument values are 5, 3, and
#    5, then the function will return 5.
###############################################################################
def return_middle_value(a, b, c):
    middle_value = sorted([a, b, c])[1]
    print('Middle value of', a, b, 'and', c, 'is', str(middle_value) + '.')
    return middle_value


###############################################################################
# 9. A function that takes two string arguments and returns a string with only
#    the characters that are in both of the argument strings. There should be
#    no duplicate characters in the return value. For example, if the two
#    argument values are "spaghetti" and "shipping" then the function should
#    return "spghi" (or any five character string with these five characters
#    that are common to both argument strings).
###############################################################################
# passing strings through set() to get rid of duplicate characters, then using
# .join() to add common characters to a string.
def venn_strings(string_1, string_2):
    set_1 = set(string_1)
    set_2 = set(string_2)

    # output = "".join(set_1 & set_2) # I think the next way is more efficient?
    output = "".join([x for x in set_1 if x in set_2])
    print(output)
    return output


###############################################################################
# 10. A function that calls each of the functions above in order to show that
#    they work correctly and provides all data to run them so the user of the
#    main program doesn't have to provide inputs for the other 9 functions.
###############################################################################
def main():
    print_name()
    get_age()
    greet_person('Goobermin')
    
    return_inverse(-42)
    return_inverse(24)
    
    repeat_message(6, 'STOP! YOU VIOLATED THE LAW! PAY THE COURT A FINE OR '
                      'SERVE YOUR SENTENCE, YOUR STOLEN GOODS ARE NOW FORFEIT.﻿')

    getBiggest(12, 14)
    getBiggest(9, 4)
    getBiggest(5, 5)
    
    count_capitals("Number 15: Burger King foot lettuce. The last thing you'd "
                   "want in your Burger King burger is someone's foot fungus.")

    return_middle_value(4, 6, 2)
    return_middle_value(5, 1, 5)
    
    venn_strings('spaghetti', 'shipping')


main()

#
#                        A
#                        M
#                        M
#                        M
#                        M
#                        M
#                        M
#                        M
#                       /M\
#                      '[V]'
#                       [A]
#                      [,-']
#                      [/"\]
#                      / _ \
#                     / / | \
#                    / /_O_| \
#                   /______|__\
#                   |=_==_==_=|
#                   |  |   |  |
#                  V|  |.V.|__|V
#                  A|  |'A'| =|A
#                   |__|___|= |
#                   |__|___| =|
#                   |####|####|
#                  |    o|     |
#                  |     |     |
#                  |     |     |
#                 |      |      |
#                 |      |      |
#                 |      |      |
#                |       |       |
#                |       |       |
#                |-------|-------|
#               |        |        |
#               |        |        |
#               |___.____|____.___|
#              |                   |
#              |___________________|
#             /|HH|      |HH][HHHHHI
#             [|##|      |##][#####I
#             [|##|      |#########I
#             [|##|______|#######m#I
#             [I|||||||||||||||||||I
#             [I|||||||||||||||||||I
#             [|                   |
#             [|    H  H          H|
#             [|    H  H          H|
#             [|    \hdF          V|
#             [|     `'            |
#             [|    d##b          d|
#             [|    #hn           #|
#             [|     ""#          }|
#             [|    \##/          V|
#             [|                   |
#             [|     dh           d|
#             [|    d/\h          d|
#             [|    H""H          H|
#             [|    "  "          "|
#             [|________.^.________|
#             [I########[ ]########I
#             [I###[]###[.]########I
#             [I###|||||[_]####||||I
#             [####II####|        n |
#            /###########|         " \
#            ############|           |
#           /############|            \
#           ######"######|            |
#          /             |####### #####\
#          |             |#######.######
#         /              |##############\
#         |              |###############
#        /_______________|###############\
#        I|||||||||||||||||||||||||||||||I
#        I|||||||||||||||||||||||||||||||I
#        I|||||||||||||||||||||||||||||||I
#        I|||||||||||||||||||||||||||||||I
#        |                               |
#        |-------------------------------|
#        |                               |
#        | [                  U          |
#        | [                  N          |
#        | !                  I          |
#        | [                  T          |
#        | [                  E          |
#        | }                  D          |
#        |                               |
#        |                               |
#        | {                  S          |
#        | [                  T          |
#        | :                  A          |
#        | [                  T          |
#        | [                  E          |
#       /| {  /|              S    |\    |
#      | |   | |                   | |   |
#      | |   | |                   | |   |
#      | |   | |                   | |   |
#      |_|___|_|___________________|_|___|
#      | |   | |                   | |   |\
#      | |___| |___________________| |___|]
#      | |###| |###################| |###|]
#      | |###| |###################| |###|]
#      | |###| |""""""""""#########| |"""|]
#      | |###| |         |#########| |   |]
#       \|####\|---------|#########|/----|]
#        |#####|         |#########|     |/
#        |#####|         |#########|     |
#       /]##### |        | ######## |    [\
#       []##### |        | ######## |    []
#       []##### |        | ######## |    []
#       []##### |        | ######## |    []
#       []##### |        | ######## |    []
#        |#####|---------|#########|-----|
#        |#####|         |#########|     |
#        |#####|         |##H######|     |
#        |#####|         |##H######|     |
#        |#####|         |##H######|     |
#        |#####|_________|##H######|_____|
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |     ####"""""""  H            |
#        |     ####"""""""  H            |
#        |     """""""""""  H            |
#        |     """""""""""  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |                  H            |
#        |__________________H____________|
#        |                  H            |
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        I||||||||||||||||||H||||||||||||I
#        |#####|         |##H######|     |
#        |#####|         |##H######|     |
#        |#####|  H   H  |##H######|   H |
#        |#####|  H   H  |##H######|   H |
#        |#####|  H   H  |##H######|   H |
#        |#####|  \h_dF  |##H######|   Vm|
#        |#####|   `"'   |##H######|    "|
#        |#####|         |##H######|     |
#        |#####|  /###\  |##H######|   /#|
#        |#####|  #   '  |##H######|   # |
#        |#####|  \###\  |##H######|   \#|
#        |#####|  .   #  |##H######|   . |
#        |#####|  \###/  |##H######|   \#|
#        |#####|         |##H######|     |
#        |#####|    H    |##H######|     [
#        |#####|   dAh   |##H######|    H|
#        |#####|  dF qL  |##H######|   dF|
#        |#####|  HhmdH  |##H######|   Hm|
#        |#####|  H   H  [%]H#apx##|   H |
#        |#####|         |##H######|     |
#        |#####A         |##H######A     |
#        |####| |        |##H#####|#|    |
#        |####| |        |##H#####|#|    |
#        |###|   |       |##H####|###|   |
#        |###|   |       |##H####|###|   |
#        |##|     |      |##H###|#####|  |
#        |#-|     |      |##H###|#####|-_|
#     _-"==|       |     |##H##|#######|=="-_
#  _-"=[]==|       |     |##H##|#######|==[]="-_
# |========|_______|_____|##H##|#######|========|
# !=======|=========|____|##H#|=========|=======!
#         !=========! /#####\ !=========!
#          /#######\ /#######\ /#######\
#         d#########V#########V#########h
#         H#########H#########H#########H
#        |###########H#######H###########|
#        |###########|"""""""|###########|
#         """""""""""         """""""""""
#
#                 Apollo Saturn V
#                  (c) apx 2000
