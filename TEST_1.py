import random
import turtle
turtle.speed(0)
def random_position():
    turtle.up()
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    a=random.randint(0,360)
    turtle.goto(x,y)
    turtle.setheading(a)


def draw_stairs(length,number,count):
    if number <=0:
        return count
    else:
        turtle.down()
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        count = count + length + length
        return draw_stairs(length,number - 1,count)

def escher(length,number,flights):
    random_position()
    count=0
    while flights > 0:
        count+=draw_stairs(length ,number,0)
        turtle.forward(length)
        turtle.left(90)
        flights= flights - 1
        length = length - 1
    print(count)

escher(25,10,25)
turtle.done()