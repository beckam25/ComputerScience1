import turtle
import math
turtle.speed(0)
def square(x,y):
    if x<0 or y<0:
        pass
    else:
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(x/2)
        turtle.left(45)
        x=math.sqrt((x**2)+(x**2))
        square(x/2,y-1)
square(100,5)
turtle.done()