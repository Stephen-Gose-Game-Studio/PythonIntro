###############################################################################
# Brandon Nay
# Listomania
###############################################################################
# the difficulty of question 1 != questions 2-6


###############################################################################
# 1. Write a function that takes a list of any size as an argument, and returns
#    a list where all adjacent, equal elements have been reduced to a single
#    element. For example [1, 2, 2, 3] would return as [1, 2, 3].
###############################################################################
def remove_doubles(input_list):
    index = 0

    # len(input_list)-1 allows the loop to compare the current and next index
    #   (index+1) without causing an index error when it gets to the last
    #   element; break from loop once the last element has been compared.
    while index < len(input_list) - 1:
        if input_list[index] == input_list[index + 1]:
            del input_list[index]
        else:
            index += 1
    return input_list

    # We can't simply use set() because it removes ALL
    # duplicates, not just ADJACENT repeating numbers.
    #   Example: set([2, 2, 4, 2, 2])
    #   would return {2, 4} when based on the problem,
    #   we want:     [2, 4, 2]


###############################################################################
# 2. Write a function that takes a list of numbers of any size as an argument
#    and returns true if the list is sorted, and false otherwise. For example,
#    [1, 2, 3] would return True, and [2,1,3] would return false.
###############################################################################
def check_sorting(input_list):
    if input_list == sorted(input_list):
        return True
    else:
        return False


###############################################################################
# 3. Write a function that takes a list of numbers of any size as an argument,
#    and returns the sum of the numbers. For example, [1,2,2,3] returns 8.
###############################################################################
def add_list_elements(input_list):
    return sum(input_list)


###############################################################################
# 4. Write a function that takes a list of any type and size as an argument,
#    and returns a list where the elements are in reverse list order. For
#    example ['rubber', 'baby', 'bellybutton']
#    returns ['bellybutton', 'baby', 'rubber']
###############################################################################
def reverse_list(input_list):
    return input_list[::-1]
# attempting to return reversed(input_list) runs, but prints a memory error.


###############################################################################
# 5. Write a function that takes two sorted lists as arguments, and returns a
#    single sorted list. For example, providing lists [1, 5, 7] and [1, 2, 4]
#    results in [1,1,2,4,5,7].
###############################################################################
def add_sorted_lists(sorted_list_1, sorted_list_2):
    return sorted(sorted_list_1 + sorted_list_2)


###############################################################################
# 6. Write a function that demonstrates and tests each of the above functions.
###############################################################################
def main():
    print('----------------------------------------------------')

    print('\nOriginal list:\n',
          test)

    print('\nList with adjacent doubles removed:\n -',
          remove_doubles(test))  # 1

    print('Is the original list sorted?:\n -',
          check_sorting(test))  # 2 False
    print('Sort the list. Now is it sorted?:\n -',
          check_sorting(sorted_test))  # 2 True

    print('Sum of', str(test) + ':\n -',
          add_list_elements(test))  # 3

    print('\nAscending list:\n -',
          ascending_list)
    print('Ascending list in reversed order:\n -',
          reverse_list(ascending_list))  # 4

    print(' \nSorted list 1:', s_list_1,
          '\nSorted list 2:', s_list_2)
    print('New list after adding and sorting the above two:\n -',
          add_sorted_lists(s_list_1, s_list_2))  # 5

    print('\n----------------------------------------------------')


test = [1, 1, 1, 4, 4, 2, 2, 2, 5, 2, 6, 5, 5, 1, 1]
sorted_test = sorted(test)
ascending_list = [0, 1, 2, 3, 4, 5]
s_list_1 = [1, 5, 7]
s_list_2 = [1, 2, 4]

main()  # execute
