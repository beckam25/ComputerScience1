"""
file: .py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This Program draws a a series of raindrops with ripples.
The # of raindrop and # of ripples are randomly generated within a
given range. The raindrops must fit within the default turtle window.
"""

def left(x):
    """
    turns the turtle left
    """
    turtle.left(x)


def right(x):
    """
    turns the turtle right
    """
    turtle.right(x)


def square(x):
    """
    draws a square ending at the bottom right
    corner facing east with lengths of x
    """
    turtle.fd(x)
    left(90)
    turtle.fd(x)
    left(90)
    turtle.fd(x)
    left(90)
    turtle.fd(x)
    left(90)
    turtle.fd(x)


def triangle(x):
    """
    draws an equilateral triangle with lengths of x
    turtle ends facing east at the bottom right
    """
    turtle.fd(x)
    left(120)
    turtle.fd(x)
    left(120)
    turtle.fd(x)
    left(120)
    turtle.fd(x)


def circle(x):
    """
    draws a circle with raidus x
    """
    turtle.circle(x)


def forward(x):
    """
    moves turtle forward x units
    """
    turtle.forward(x)


def backwards(x):
    """
    moves turtle back x units
    """
    turtle.backward(x)


def up():
    """
    turtle pen up
    """
    turtle.up()


def down():
    """
    turtle pen down
    """
    turtle.down()


def rectangle(l, w):
    """
    draw a rectangle with length l and width w
    ending bottom right facing east
    """
    turtle.forward(l)
    left(90)
    turtle.forward(w)
    left(90)
    turtle.forward(l)
    left(90)
    turtle.forward(w)
    left(90)
    turtle.forward(l)


def polygon(s, l):
    """
    draw a polygon with s equal to the number of sides
    and l equal to the length of each side
    turtle ends at the bottom right of the polygon facing east
    """
    degree = 360 / s  # determines the number of degrees between each side to create a polygon
    if s < 3:
        pass
    else:
        while s > 0:
            turtle.forward(l)
            turtle.left(degree)
            s = s - 1
    turtle.forward(l)


def move(x, y):
    """
    moves the turtle to a specific location
    """
    turtle.goto(x, y)


def color(x):
    """
    changes the color of the pen based on the input x value
    """
    if x == 0:
        turtle.pencolor("red")
    elif x == 1:
        turtle.pencolor("blue")
    elif x == 2:
        turtle.pencolor("green")
    elif x == 3:
        turtle.pencolor("yellow")
    elif x == 4:
        turtle.pencolor("brown")
    else:
        turtle.pencolor("black")


def length(string):
    """computes the length of the string"""
    if string == "":
        return 0
    else:
        return 1 + length(get_tail(string))


def get_head(string):
    """get the head of a string"""
    if string == "":
        return None
    else:
        return string[0]


def get_tail(string):
    """get the tail of a string"""
    return string[1:]


def shapy_turtle(st):
    """
    shapy_turtle will:
    1)read the first character in the string
    2)a.if the character is a command, the function will execute that command
      b.if the character is not a command the function will exit and print
        the attempted input.
    3)each command will check for the digits following the command and execute
      the command based on the given input
    """
    number = ""
    if len(st) > 0:
        h = st[0]
        t = st[1:]
        if h == "<":
            """calls the left command"""
            if not t[0].isdigit():
                print(t[0:], "is not valid after <")
                return None
            else:
                number = get_digit(t)
                left(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == ">":
            """calls the right command"""
            if not t[0].isdigit():
                print(t[:], "is not valid after >")
                return None
            else:
                number = get_digit(t)
                right(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "S":
            """calll the square command"""
            if not t[0].isdigit():
                print(t[0:], "is not valid after S")
                return None
            else:
                number = get_digit(t)
                square((int(number)))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "T":
            """calls the triangle command"""
            if not t[0].isdigit():
                print(t[0:], "is not valid after T")
                return None
            else:
                number = get_digit(t)
                triangle(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "C":
            """calls the circle command"""
            if not t[0].isdigit():
                print(t[0:], "is not valid after C")
                return None
            else:
                number = get_digit(t)
                circle(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "F":
            """calls the forward command"""
            if not t[0].isdigit():
                print(t[0:], "is not valid after F")
                return None
            else:
                number = get_digit(t)
                forward(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "B":
            if not t[0].isdigit():
                print(t[0:], "is not valid after B")
                return None
            else:
                number = get_digit(t)
                backwards(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        elif h == "U":
            up()
            st = st[len(number) + 1:]
            shapy_turtle(st)
        elif h == "D":
            down()
            st = st[len(number) + 1:]
            shapy_turtle(st)
        elif h == "R":
            if not t[0].isdigit():
                print(t[0:], "is not valid after R")
                return None
            else:
                number = get_digit(t)
                rlength = int(number)
                st = st[len(number) + 2:]
                number = get_digit(st)
                rwidth = int(number)
                rectangle(rlength, rwidth)
                st = st[len(number):]
                shapy_turtle(st)
        elif h == "P":
            if not t[0].isdigit():
                print(t[0:], "is not valid after P")
                return None
            else:
                number = get_digit(t)
                number_of_sides = int(number)
                st = st[len(number) + 2:]
                number = get_digit(st)
                plength = int(number)
                polygon(number_of_sides, plength)
                st = st[len(number):]
                shapy_turtle(st)
        elif h == "G":
            if not t[0].isdigit():
                print(t[0:], "is not valid after G")
                return None
            else:
                number = get_digit(t)
                xcoordinate = int(number)
                st = st[len(number) + 2:]
                number = get_digit(st)
                ycoordinate = int(number)
                turtle.goto(xcoordinate, ycoordinate)
                st = st[len(number):]
                shapy_turtle(st)
        elif h == "Z":
            if not t[0].isdigit():
                print(t[0:], "is not valid after Z")
                return None
            else:
                number = get_digit(t)
                color(int(number))
                st = st[len(number) + 1:]
                shapy_turtle(st)
        else:
            print(st[0], "is not a valid command")
    else:
        print("There are no more commands")


def get_digit(string):
    """
    get_digits will get the string of digits after
    a command and return that string of digits
    """
    number = ""
    for h in string:
        if h.isdigit():
            number = number + h
        else:
            return number
    return number


def main():
    """
    main asks for a user input of shapy turtle commands
    then gives that value to shapy_turtle
    """
    shapy_turtle(input("Enter a string of shapy turtle commands: "))
    turtle.done()


main()
