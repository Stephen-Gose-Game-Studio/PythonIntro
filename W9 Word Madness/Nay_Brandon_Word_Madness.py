###############################################################################
# Brandon Nay
# Word Madness
###############################################################################
# In this assignment you will write a Python program that counts vowels or
# consonants for a set of words, and calculates the average number of vowels or
# consonants across the set of words.
#
# User interaction with the program should look like this:
#
# 1. Program Starts and asks the user whether they want to count vowels or
#    consonants or quit. The input value is stored as a "mode". If user
#    provides input other than "consonant" or "vowel" or "quit", program
#    interprets this as an error and re-asks for input.
# 2. Program asks for a word.
# 3. Depending on mode, the number of consonants or vowels are calculated and
#    reported to the user.
# 4. Program asks if another word is available. If so, steps 2 through 4 are
#    repeated, otherwise continue to step 5.
# 5. Average vowels per word or average consonants per word are reported to
#    the user.
###############################################################################


def get_mode():
    retry = '\nPlease enter "v", "c" or "q".'
    while True:
        try:
            mode = str(input('Would you like to count '
                             '(v)owels, (c)onsonants or (q)uit? '))
        except ValueError:
            print(retry)
            continue
        else:
            if mode == "":
                print(retry)
                continue
            else:
                if mode.lower() in "vcq":
                    return mode
                else:
                    print(retry)
                    continue


def get_word():
    retry = '\nSpaces, numbers and special characters not allowed.'
    while True:
        try:
            input_word = str(input('Enter a word: '))
        except ValueError:
            print(retry)
            continue
        else:
            if input_word == "":
                print(retry)
                continue
            else:
                if input_word.isalpha():  # check for numbers and spaces
                    return input_word.lower()
                else:
                    print(retry)
                    continue


def count_vowels(input_word):
    vowels = 0

    for x in input_word:
        if x in 'aeiouy':
            vowels += 1
        else:
            continue
    return vowels


def count_consonants(input_word):
    consonants = 0

    for x in input_word:
        if x in 'bcdfghjklmnpqrstvwxz':  # say that 10 times fast
            consonants += 1
        else:
            continue
    return consonants


def ask_another_word():
    retry = '\nPlease choose "y" or "n".'
    while True:
        try:
            answer = str(input('Would you like to check another word? [y/n] '))
        except ValueError:
            print(retry)
            continue
        else:
            if answer == "":
                print(retry)
                continue
            else:
                if answer.lower() in 'yn':
                    return answer.lower()
                else:
                    print(retry)
                    continue


def main():
    mode = get_mode().lower()  # initial prompt to start the party
    total_vowels = 0
    total_consonants = 0
    total_words = 0
    average_characters = 0

    #################################
    # BEGINNING OF INTERACTIVE LOOP #
    #################################

    # QUITTER-TALK MODE
    if mode == 'q':
        pass

    # VOWEL MODE
    elif mode == 'v':
        while True:
            # receive word
            input_word = get_word()

            # add count to total words
            total_words += 1

            # count vowels in current word
            current_word_vowels = count_vowels(input_word)

            # add vowels to total and report
            total_vowels += current_word_vowels
            print('\nThere are', current_word_vowels, 'vowels in',
                  str(input_word) + '.')

            # see if they wanna go again
            answer = ask_another_word()
            if answer == 'y':
                continue
            else:
                average_characters = total_vowels / total_words
                break

    # CONSONANT MODE
    elif mode == 'c':
        while True:  # mirror of vowel mode for consonants
            input_word = get_word()
            total_words += 1
            current_word_consonants = count_consonants(input_word)
            total_consonants += current_word_consonants
            print('\nThere are', current_word_consonants, 'consonants in',
                  str(input_word) + '.')
            answer = ask_another_word()
            if answer == 'y':
                continue
            else:
                average_characters = total_consonants / total_words
                break

    # Something goofed even though it shouldn't be able to
    else:
        print('Something uhhhhh went wrong.')

    ###########################
    # END OF INTERACTIVE LOOP #
    ###########################

    # Exit message based on mode
    if mode == 'q':
        print('\n\nGoodbye!')
    elif mode == 'v':
        print('\n\nCool! You tested', total_words,
              'words for vowels.\nOn average, there were',
              format(average_characters, '.1f'),
              'vowels per word!\nSee you next time!')
    elif mode == 'c':
        print('\n\nCool! You tested', total_words,
              'words for consonants.\nOn average, there were',
              format(average_characters, '.1f'),
              'consonants per word!\nSee you next time!')
    else:
        print('Something went wrong but really im just trying not to get '
              'caught with hanging if statements even if everything above is '
              'indestructible.')


main()  # execute
