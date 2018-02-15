###############################################################################
# Brandon Nay
# Multiplication Tutor
###############################################################################
# In this assignment you will write a python program that will create and
# display simple multiplication problems for the user to solve.
#
# User interaction with the program should look like this:
#
# 1. Program Starts and asks the user how many problems they want to solve. If
#    user enters any input other than the valid range of one through 10,
#    program interprets this as an error and re-asks for input.
# 2. Program generates a random multiplication problem with two random factors
#    between zero and 12 (zero and 12 are valid factors).
# 3. Program displays the problem for the user.
# 4. Program asks the user for the answer to the current problem. If the user's
#    answer is not correct then the program gives a hint by telling the user if
#    their answer is too high or too low, and then returns to step 3. If the
#    user's answer is correct then the program displays a message telling the
#    user that the answer is correct, and then the program either returns to
#    step 2 (if the user has not solved the requested number of problems) or
#    the program continues on to step 5.
# 5. The program displays the average number of tries the user took to get the
#    correct answer.
###############################################################################

from random import randint
import time


# Ask user how many problems they want to solve, return #
def num_problems():
    error = '\n**Please enter a number 1 to 10.'

    while True:
        try:
            problems = int(input(
                'How many problems would you like to solve? (Max 10): '))
        except ValueError:
            print(error)
            continue
        else:
            if problems < 1 or 10 < problems:
                print(error)
                continue
            else:
                return problems


# Give a question and output the attempts it took to get it right.
# Output is used to keep track of total attempts across many problems in main()
def generate_problem():
    num_1 = randint(0, 12)
    num_2 = randint(0, 12)
    real_answer = num_1 * num_2
    question_attempts = 0

    while True:
        try:
            question_attempts += 1
            print('\nWhat is {} * {}?'.format(num_1, num_2))
            player_answer = int(input("Answer: "))
        except ValueError:
            print("\nPlease enter a number.")
            continue
        else:
            if player_answer > real_answer:
                print("Your answer is too high!")
                continue
            elif player_answer < real_answer:
                print("Your answer is too low!")
                continue
            elif player_answer == real_answer:
                print("--CORRECT--")
                return question_attempts


def main():
    print('--------------------------------------------------------')

    number_of_problems = num_problems()
    total_attempts = 0

    start_time = time.clock()

    for x in range(number_of_problems):
        total_attempts += generate_problem()

    end_time = time.clock() - start_time

    average_tries = total_attempts / number_of_problems

    print('\nCongratulations, you completed {} problems in {:.1f} seconds!\n'
          'It took you an average of {:.0f} attempt(s) per problem.'
          .format(number_of_problems, end_time, average_tries))

    print('--------------------------------------------------------')


main()  # execute

#  _____________________
# |  _________________  |
# | |        5318008. | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | x | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|
