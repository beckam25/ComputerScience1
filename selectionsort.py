"""
file: selectionsort.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This program takes a list of numbers from a file and
sorts the list without creating a new list.

Answers to questions:
1) Insertion sort works better than selection sort in a case where you have
a very long list that you wish to be sorted.

2)Selection sort is worse in this case because it would search the list for
the lowest(or highest) index remaining in the list THEN put it at the end of
the sorted list.
Insertion sort would take the next unsorted index and insert it where it belonged in
the sorted part of the list.
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
    :param lst: THe list to look in
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
    print("The sorted list:")
    print(lst)


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
    print("The original list:")
    print(new_lst)
    selection_sort(new_lst)



main()
