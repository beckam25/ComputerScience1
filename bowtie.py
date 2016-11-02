import turtle

def recursion(x):
    if x>0:
        turtle.forward(x)
        turtle.right(90)
        recursion(x-5)
    else:
        pass

def iteration(x):
    while x > 0:
        turtle.forward(x)
        turtle.right(90)
        x = x - 5
turtle.left(90)
recursion(100)
turtle.home()
iteration(100)
turtle.done()