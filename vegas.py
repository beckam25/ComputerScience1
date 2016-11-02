from rit_lib import *
from myStack import *
from myQueue import *
from myNode import *
import random


class vegas(struct):
    """ the class vegas with slots for victory, 2 discard piles and a deck"""
    _slots = ((Stack, "victory"), (Stack, "discard1"), (Stack, "discard2"), (Queue, "deck"))


def create_game(game_queue):
    """ creates the vegas class with the game_queue from user input"""
    return vegas(Stack(None, 0), Stack(None, 0), Stack(None, 0), game_queue)


def shuffled(queue):
    """ 'shuffles' the deck a random number of times and returns the front card"""
    x = random.randint(0, queue.size)
    for i in range(x):
        enqueue(queue, front(queue))
        dequeue(queue)
    temp = front(queue)
    dequeue(queue)
    return temp


def game(vegas, x):
    """
    takes a card and compares it to the stacks. pushing it in order.
    """
    if emptyStack(vegas.victory) and x == 1:  # only push 1 to victory
        push(vegas.victory, x)
        discards(vegas)
    elif not emptyStack(vegas.victory) and x == (top(vegas.victory) + 1):  # only push top(victory) + 1
        push(vegas.victory, x)
        discards(vegas)
    elif not emptyStack(vegas.discard1) and x == top(vegas.discard1) - 1:  # if x = top of discard1 minus 1
        push(vegas.discard1, x)
    elif not emptyStack(vegas.discard2) and x == top(vegas.discard2) - 1:  # if x = top of discard2 minus 1
        push(vegas.discard2, x)
    elif emptyStack(vegas.discard1):  # if discard1 is empty
        push(vegas.discard1, x)
    elif emptyStack(vegas.discard2):  # if discard2 is empty
        push(vegas.discard2, x)
    elif x > top(vegas.discard1) and x > top(vegas.discard2):  # if x > both tops of discards
        if top(vegas.discard1) > top(vegas.discard2):  # if top discard1 > top discard2
            push(vegas.discard1, x)
        else:
            push(vegas.discard2, x)
    elif x < top(vegas.discard1) and x < top(vegas.discard2): # if x < both tops
        if top(vegas.discard1) > top(vegas.discard2):  # if top discard1 > top discard2
            push(vegas.discard1, x)
        else:
            push(vegas.discard2, x)
    elif x < top(vegas.discard1) and x > top(vegas.discard2): # if x < both tops
            push(vegas.discard1, x)
    elif x > top(vegas.discard1) and x < top(vegas.discard2): # if x < both tops
            push(vegas.discard2, x)

def discards(vegas):
    """
    checks the discard piles to see if they can put their top on the victory pile
    """
    while True:
        if not emptyStack(vegas.discard1) and top(vegas.discard1) == (top(vegas.victory) + 1):
            push(vegas.victory, top(vegas.discard1))
            pop(vegas.discard1)

        elif not emptyStack(vegas.discard2) and top(vegas.discard2) == (top(vegas.victory) + 1):
            push(vegas.victory, top(vegas.discard2))
            pop(vegas.discard2)

        else:
            break


def main():
    """
    Prompts a user for deck size and number of plays
    Creates each game while keeping track of min, max and the sum
    of all the games
    Prints an average victory size, the min victory size and max victory size
    """
    size = int(input("what is the size of the deck? "))
    plays = int(input("how many plays? "))
    sum = 0
    minimum = size + 1
    maximum = 0
    for each in range(plays):
        game_queue = createQueue()
        for i in range(size):
            enqueue(game_queue, i + 1)
        x = create_game(game_queue)
        while game_queue.size > 0:
            game(x, shuffled(x.deck))
        victory_size = x.victory.size
        if victory_size > maximum:
            maximum = victory_size
        if victory_size < minimum:
            minimum = victory_size
        sum = sum + victory_size
    average = sum/plays
    print("The Average Size of Victory: ", average)
    print("The maximum victory size: ", maximum)
    print("The minimum victory size: ", minimum)


main()