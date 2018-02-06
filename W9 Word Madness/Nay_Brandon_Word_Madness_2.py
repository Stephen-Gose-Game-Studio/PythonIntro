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
    options = {'v', 'c', 'q'}
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
                if mode.lower() in options:
                    return mode.lower()
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


def sort_characters(input_word, mode):
    vowels = 0
    consonants = 0

    for x in input_word:
        if x in 'aeiouy':
            vowels += 1
        else:
            consonants += 1
    if mode == 'v':
        return vowels
    elif mode == 'c':
        return consonants
    else:
        pass


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
    mode = get_mode()  # initial prompt to start the party
    total_characters = 0
    total_words = 0
    average_characters = 0

    if mode == 'q':
        pass

    # Interactive loop
    elif mode == 'v' or mode == 'c':
        while True:
            # receive word
            input_word = get_word()

            # add count to total words
            total_words += 1

            # get vowels or consonants based on mode
            current_word_characters = sort_characters(input_word, mode)

            # add characters to total and report based on mode
            total_characters += current_word_characters
            if mode == 'v':
                print('\nThere are', current_word_characters, 'vowels in',
                      str(input_word) + '.')
            else:
                print('\nThere are', current_word_characters, 'consonants in',
                      str(input_word) + '.')

            # see if they wanna go again
            answer = ask_another_word()
            if answer == 'y':
                continue
            else:
                average_characters = total_characters / total_words
                break

    else:  # Something goofed even though it shouldn't be able to
        print('Something uhhhhh went wrong.')

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
