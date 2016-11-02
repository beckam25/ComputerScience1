"""
file: dictionary_impossible.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
The functions in this file will be used to encode and decode
data using word replacement.
"""
def encode_function(dictionary, word):
    """
    this function finds the word paired with the input word
    and returns it
    if the word has no pair then the original word is returned
    """
    if word in dictionary.keys():
        return dictionary.get(word)
    else:
        return word

def decode_function(dictionary,word):
    """
    this function finds the word paired with the input word
    and returns it
    if the word has no pair then the original word is returned
    """
    if word in dictionary.keys():
        return dictionary.get(word)
    else:
        return word

def main():
    """
    the main function will ask the user for the files it needs
    to run the encode and decode programs.
    then it will print all relative information
    """
    print("Welcome to the Encode Master 2001!")
    secret_key = input("input the name of the secret key secret_key: ")
    dictionary_encode = {}
    dictionary_decode = {}
    for line in open(secret_key):
        line = line.split()
        dictionary_encode[line[0]] = line[1]
        dictionary_decode[line[1]] = line[0]
    plain_text = input("input the name of the plain text file: ")
    print("Preparing to encode",plain_text,"using",secret_key)
    print("the <word,encode word> pairs are: ")
    print(dictionary_encode)
    encoded_words = ''
    for lines in open(plain_text):
        lines = lines.split()
        for word in lines:
            encoded_words = encoded_words + " " + encode_function(dictionary_encode,word)
    print("Sending the encoded lines to the agent")
    print("The encoded lines are:")
    print(encoded_words)
    print("The agent is decoding the lines.")
    print("The <encode word,word> pairs are: ")
    print(dictionary_decode)
    decoded_words = ''
    for decode in encoded_words.split():
        decoded_words = decoded_words + " " + decode_function(dictionary_decode,decode)
    print(decoded_words)
    print("Exiting the Encode Master 2001")
main()

