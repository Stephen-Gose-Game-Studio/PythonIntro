##########################################################################
# Brandon Nay
# Let's Play Dice! Pt. 1
##########################################################################
# In this assignment you will write a  Python program that is the first
# in a 2 part series. This program will roll 2 dice by default. The
# program will then do some mathematical operations on the results,
# including multiplication, division, addition, subtraction, and average
# of the dice. The program will output the results using formatted output.
#
# User interaction with the program should look like this:
#
# 1. Program generates two random dice values between 1 and 6 (one value
#    for each dice).
# 2. Program displays the values of both dice.
# 3. Program displays the values of multiplication, division, addition,
#    subtraction, and average of the dice in a nicely formatted display.
##########################################################################

from random import randint

dice_1 = randint(1, 6)
dice_2 = randint(1, 6)

multiplication = dice_1 * dice_2
division = dice_1 / dice_2
addition = dice_1 + dice_2
subtraction = dice_1 - dice_2
average = addition / 2

# Convert int's to strings now to avoid repeating str() in Output.
dice_1 = str(dice_1)
dice_2 = str(dice_2)

# Output
print("---------------------------------------")
print("Rolling dice...\n\n"
      "You rolled", dice_1, "and", dice_2 + "!\n\n"
      "Below is a list of several mathematical\n"
      "operations performed on this roll:\n\n" +
      dice_1, "*", dice_2, "=", multiplication, '\n' +
      dice_1, "/", dice_2, "=", format(division, '.2f'), '\n' +
      dice_1, "+", dice_2, "=", addition, '\n' +
      dice_1, "-", dice_2, "=", subtraction, '\n'
      "Average of", dice_1, "and", dice_2, "=", format(average, '.2f'))
print("---------------------------------------")

#  .........
# :~, *   * ~,
# : ~, *   * ~.
# :  ~........~
# : *:         :      ~'~,
# :  :         :    ~' *  ~,
# ~* :    *    : ,~' *    * ~,
#  ~,:         :.~,*    *  ,~ :
#   ~:.........::  ~, *  ,~   :
#               : *  ~,,~  *  :
#               :* * * :  *   :
#                ~, *  : *  ,~
#                  ~,  :  ,~
#                    ~,:,~
