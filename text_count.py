"""
file: text_count.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description: The program takes a user input word
and counts how many times it appears in a text file.
The program then tells the user how many times a word
was in the text file and prints the lines which the word
was in.
"""


def count_text_string(search_for, search_in):
    """
    a function that takes a text to be searched for and a text to be searched in.
    It must use recursion to return the number of times that the searched-for
    string appears in the searched-in string

    counter
    """
    if length(search_in) == 0:
        return 0
    elif length(search_for) == 0:
        return 0
    elif helper(search_for,search_in)==1:
        return 1 + count_text_string(search_for, get_tail(search_in))
    else:
        return count_text_string(search_for,get_tail(search_in))

def helper(search_for, search_in):
    """the helper() function will determine if the the words match"""

    if length(search_for) == 0:
        return True  # continue looking through the text
    elif length(search_for) == 0:
        return False  # done looking through the text file
    elif get_head(search_for) == get_head(search_in):
        return helper(get_tail(search_for), get_tail(search_in))
        # checking to see if the words are the same
    else:
        return False


def count_text_file(search_for, text_file_name):
    """
    a function that takes in the text to be searched for and the name of the
    ﬁle to search for the text in. It will use a for loop to print the lines
    containing the searched for text and the count of the given letter in the ﬁle.

    Text line and # of searched term in text
    """
    number=0
    count=0
    for line in open(text_file_name, "r"):
        line = line.strip()
        count = count_text_string(search_for, line)+count
        number = count + number
        if count >= 1:
            print(line)
            count=0
        else:
            None

    print("Total number of times your string is in the file: ",number)


def length(string):
    """computes the length of the string"""
    if string == '':
        return 0
    else:
        return 1 + length(get_tail(string))


def get_head(string):
    if string == "":
        return None
        """get the head of a string"""
    else:
        return string[0]


def get_tail(string):
    """get the tail of a string"""
    return string[1:]


def main():
    """
    This is the main function where the user will
    input the file and the word to search for within the file.
    Then those parameters are passed into the count_text_file
    function.
    """
    search_for = input("What word are you searching for: ")
    text_file_name = input("Enter Filename: ")
    count_text_file(search_for, text_file_name)

main()