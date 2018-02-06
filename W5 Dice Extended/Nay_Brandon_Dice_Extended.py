##########################################################################
# Brandon Nay
# Let's Play Dice! Pt. 2
##########################################################################
# In this assignment you will write a Python program that is a
# continuation of the previous Dice program.  This program will simulate a
# game of Craps. It will roll the pair of dice three times. It will keep
# score for the “house” (the computer), and for the player. It will then
# display these scores each time the dice are rolled based on the rules
# listed below. It will lastly display a final winner at the end of the
# game.
#
# Rules of the game (and the program):
#
# 1. Player and “house” start with a score of 0 before the first roll.
#    Scores for both are accumulated through the number of rolls (1,2, and
#    3).
# 2. For each roll of the 2 dice: NOTE – this does not require a loop as
#    we have not covered this, but you may use loops if you have moved
#    ahead and mastered them.
#    a. If the sum of the dice is 7 or 11, display “CRAPS” and increment
#       “house score by 2”.
#    b. If the dice are the same value (doubles) and the values are even,
#       increment the player score by 2 (NOTE – you should use the modulo
#       operator with an operand of 2 for determining whether the value is
#       even).
#    c. If the dice are the same value (doubles) and the values are odd,
#       increment the “house” score by 2.
#    d. If not CRAPS or doubles, and the total is less than 7, houseScore
#       = houseScore +2.
#    e. If not CRAPS or doubles, and the total is greater than 7,
#       playerScore = playerScore + 2.
# 3. Determine the winner and display the results (with 3 rolls, there
#    cannot be a tie!).
##########################################################################

from random import randint


# Determine the outcome of a single roll
def roll():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)

    added_dice = dice_1 + dice_2

    # print "ROLL: (x, y) = z"
    print("  ROLL:", "(" + str(dice_1) + ",", str(dice_2) + ")",
          "=", str(added_dice))

    if added_dice == 7 or added_dice == 11:
        print(format("-CRAPS-", ' >14'))
        return 'house'
    elif dice_1 == dice_2 and dice_1 % 2 == 0:
        return 'player'
    elif dice_1 == dice_2 and dice_1 % 2 != 0:
        return 'house'
    elif added_dice < 7:
        return 'house'
    elif added_dice > 7:
        return 'player'


# Run the game
def main():
    player_score = 0
    house_score = 0

    print('---------------------')

    # Roll 3 times and award points
    for x in range(0, 3):
        roll_result = roll()

        if roll_result == 'player':
            player_score = player_score + 2
            print("Player wins the roll!\n")
        elif roll_result == 'house':
            house_score = house_score + 2
            print(" House wins the roll!\n")

    print("     " + "\033[4mFINAL SCORE\033[0m\n"  # formatted for underline
          "      House: ", str(house_score) + "\n"
          "      Player:", str(player_score))

    if player_score > house_score:
        print(" -The Player Wins!!-")
    elif player_score < house_score:
        print("  -The House Wins!!-")

    print("---------------------")


main()  # Execute

#               _______.
#    ______    | .   . |\
#   /     /\   |   .   |.\
#  /  '  /  \  | .   . |.'|
# /_____/. . \ |_______|.'|
# \ . . \    /  \ ' .   \'|
#  \ . . \  /    \____'__\|
#   \_____\/
