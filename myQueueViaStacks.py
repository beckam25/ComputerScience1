"""
file: myQueueViaStacks.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This file will simulate a queue using two stacks.
"""

from myStack import *


class QueueViaStacks(struct):
    """defines class QueueViaStacks with three slots"""
    _slots = ((Stack, 'stack1'), (Stack, 'stack2'), (int, 'size'))


def createQVS():
    """create a QueueViaStacks class with two stacks and a size"""
    return QueueViaStacks(Stack(None, 0), Stack(None, 0), 0)


def enqueue(queue, element):
    """Insert an element into the back of the queue (Returns None)"""
    while queue.stack1.size > 0:
        x = top(queue.stack1)
        pop(queue.stack1)
        push(queue.stack2, x)
    push(queue.stack1, element)
    queue.size += 1
    while queue.stack2.size > 0:
        x = top(queue.stack2)
        pop(queue.stack2)
        push(queue.stack1, x)


def dequeue(queue):
    """Remove the front element from the queue (Returns None)"""
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    else:
        pop(queue.stack1)
        queue.size -= 1


def front(queue):
    """Access and return the first element in the queue without removing it"""
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    else:
        return top(queue.stack1)


def back(queue):
    """Access and return the last element in the queue without removing it"""
    if emptyQueue(queue):
        raise IndexError("queue is empty")
    else:
        while queue.stack1.size > 1:
            x = top(queue.stack1)
            pop(queue.stack1)
            push(queue.stack2, x)
        y = top(queue.stack1)
        while queue.stack2.size > 0:
            x = top(queue.stack2)
            pop(queue.stack2)
            push(queue.stack1, x)
        return y


def emptyQueue(queue):
    """Is the queue empty?"""

    return queue.size == 0
