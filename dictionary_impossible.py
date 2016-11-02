"""
file: dictionary_impossible.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
The functions in this file will be used to encode and decode
data from a text file using word replacement.
"""

def encode_function(plain_text, secret_key):
    """
    takes in a plain text file and a secret key file.
    encodes the plain text file and returns them in
    a list
    :param plain_text: file to be encoded
    :param secret_key: file of (key, value) pairs
    :return: list of encoded strings
    """
    dictionary_encode = {}
    for pairs in open(secret_key):
        pairs = pairs.split()
        dictionary_encode[pairs[0]] = pairs[1]
    lines = []
    words = ''
    for line in open(plain_text):
        for word in line.split():
            if word in dictionary_encode.keys():
                word = dictionary_encode.get(word)
            words += word + ' '
        lines += [words]
        words =''
    return lines



def decode_function(lst, secret_key):
    """
    takes a list of encoded strings and a secret (key,value) pair
    and decodes the string. it prints one decoded line at a time
    :param lst: the list of encoded strings
    :param secret_key: file of (key, value) pairs
    :return: None
    """
    dictionary_decode = {}
    for pairs in open(secret_key):
        pairs = pairs.split()
        dictionary_decode[pairs[1]] = pairs[0]
    words =''
    for line in lst:
        for each in line.split():
            if each in dictionary_decode.keys():
                each = dictionary_decode.get(each)
                words += each + ' '
        print(words)
        words = ''

def word_pairs_encode(secret_key):
    """
    takes a secret key file and returns the
    (key, value) pairs to encode
    """
    dictionary_encode = {}
    for line in open(secret_key):
        line = line.split()
        dictionary_encode[line[0]] = line[1]
    return dictionary_encode

def word_pairs_decode(secret_key):
    """
    takes a secret key file and returns the
    (key, value) pairs to decode
    """
    dictionary_decode = {}
    for line in open(secret_key):
        line = line.split()
        dictionary_decode[line[1]] = line[0]
    return dictionary_decode


def main():
    """
    the main function will ask the user for the files it needs
    to run the encode and decode programs.
    then it will send the information to the programs
    and print any relative information
    """
    print("Welcome to the Encode Master 2001!")
    secret_key = input("Input the name of the secret key secret_key: ")
    plain_text = input("Input the name of the plain text file: ")
    print("Preparing to encode",plain_text,"using",secret_key)
    x = encode_function(plain_text, secret_key) # list of encoded lines
    print("the <word, encode_word> pairs are: ")
    print(word_pairs_encode(secret_key)) # (key, value) encode pairs
    print("Sending the encoded lines to the agent")
    print("The encoded lines are:")
    print(x) # print the encoded list
    print("The agent is decoding the lines.")
    print("The <encode_word, word> pairs are: ")
    print(word_pairs_decode(secret_key)) # (key, value) decode pairs
    decode_function(x,secret_key) # decode function that prints line by line
    print("Exiting the Encode Master 2001")

main()