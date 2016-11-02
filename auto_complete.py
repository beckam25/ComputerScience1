"""
file: auto_complete.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This program takes a user input prefix and finds the closest match
to a word. The program uses binary search on a sorted list, and
a linear search on unsorted and sorted lists. The program prints the
three results from the searches.

"""


def swap(lst, x, y):
    """
    Swap two indexes in a list
    :param lst: The list to be swapped in
    :param x: first index to swap
    :param y: second index to swap
    :return: list with x and y swapped
    """
    temporary = lst[x]
    lst[x] = lst[y]
    lst[y] = temporary


def find_min(lst):
    """
    Find the minimum index in a list
    :param lst: The list to look in
    :return: the minimum in the list
    """
    if len(lst) > 0:
        minimum = lst[0]
        for index in range(1, len(lst)):
            if lst[index] < minimum:
                minimum = lst[index]
        return minimum


def search_in_list(lst, number):
    """
    Finding the index of a number. In this case the minimum.
    :param lst: The list to look in.
    :param number: The number to look for.
    :return: The index where the number is located in the list
    """
    for index in range(len(lst)):
        if number == lst[index]:
            return index
    return None


def selection_sort(lst):
    """
    Sorting function that will sort integers in a list
    from lowest to highest
    :param lst: The list to be sorted
    :return: A sorted version of the list from low to high
    """
    x = 0
    while x < len(lst):
        minimum = find_min(lst[x:])
        found = search_in_list(lst[x:], minimum) + x  # add x to account for all indexes before the slice
        swap(lst, found, x)
        x = x + 1
    return lst


def main():
    """
    The main function which imports a user input list
    and sends that list to the sorting function.
    :return: The sorted list
    """
    filename = input("filename: ")
    text = open(filename)
    lst = []
    count = 0
    for line in text:
        lst = lst + line.split()
        new_lst = []
        for char in lst:
            new_lst.append(char)
    print("The Unsorted List:")
    print(new_lst)
    sorted_list = selection_sort(new_lst)
    print("The Sorted List")
    print(sorted_list)
    print("Welcome to Auto-Complete.")
    print("Entering nothing will search for the next word with that prefix.")
    print("Enter <QUIT> when asked for a prefix to exit.")
    copy_unsorted = new_lst
    copy_sorted = sorted_list
    auto_complete(new_lst,sorted_list,copy_sorted,copy_unsorted)

def auto_complete(new_lst,sorted_list,copy_sorted,copy_unsorted):
    searched_words =[]
    word = input("Type a word or prefix to search for: ")
    searched_words.append(word)

    if word == "<QUIT>":
        exit()
    elif word != "<QUIT>" or "":
        if len(new_lst) == 0 or len(sorted_list) ==0:
            new_lst = copy_unsorted
            sorted_list = copy_sorted
            auto_complete((new_lst,sorted_list,copy_sorted,copy_unsorted))
        while len(new_lst) > 0 and len(sorted_list) > 0:
            print("Match for Linear Unsorted is:",search_for(word,new_lst))
            print()
            print("Match for Linear Sorted is:",search_for(word,sorted_list))
            print()
            #print("Match for Binary Sorted is:", binary_search(sorted_list,word,sorted_list[0],sorted_list[-1]))
            auto_complete(new_lst[1:],sorted_list[1:],copy_sorted,copy_unsorted)

def search_for(word,lst):
    """
    Searches for a word or prefix in a list
    :param word: The word to look for
    :param lst: The list to look in
    :return: word in list if they match
    """
    for char in lst:
        if starts_with(word,char) == True:
            return char

def starts_with(word,char):
    """
    checks to see if a word starts with a prefix.
    returns the word if it does
    :param word: the word to check
    :param char: word from the list to compare to word
    :return:
    """
    for letter in char:
        if word[0] == letter:
            return True
        else:
            return False
        word = word[1:]


def binary_search(data, target, start, end):
    """
    binary_search : List(Orderable) Orderable NatNum NatNum -> NatNum or NoneType
    Perform a binary search for a target value between start and end indices.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
        start - the starting index in data that is part of this search
        end - the ending index in data that is part of this search
    Returns:
        index of target in data, if present; otherwise None.
    """

    # base condition - terminate when start passes end index
    if start > end:
        return None

    # find the middle value between start and end indices
    mid_index = len(data) // 2
    mid_value = data[mid_index]
    print(mid_value)

    if target == mid_value:
        return mid_value
    elif target < mid_value:
        return binary_search(data, target, start, mid_index - 1)
    else:
        return binary_search(data, target, mid_index + 1, end)



main()