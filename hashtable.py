from rit_lib import *

class HashTable(struct):
    _slots = ((list, 'table'),
              (int, 'size'),
              (int, 'capacity'),
              (object, 'hash_function'))

class Entry(struct):
    _slots = ((object, 'key'),
              (object, 'value'))

def hash_function(string):
    """
    sums the ASCII values of characters in string
    scaled by 31 to the power of the index in the string
    :returns: sum of those values
    """
    sum = 0
    for i in range(len(string)):
        sum += ord(string[i])*(31**i)
    return sum

def createHashTable(hash_func, capacity):
    empty_list = [None for _ in range(capacity)]
    return HashTable(empty_list, 0, capacity,  hash_func)

def imbalance():
    pass
