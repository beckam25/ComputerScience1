"""
file: shapy_turtle.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This program will take an input string of characters from the user.
The program will then execute shapy turtle commands based on the user
input.
"""
import turtle


def left(st):
    """
    turns the turtle left
    """
    if not st[0].isdigit():
        print(st[0], "is not valid after <")
        return None
    else:
        number = get_digit(st)
        st = st[len(number):]
        turtle.left(int(number))
        shapy_turtle(st)


def right(st):
    """
    turns the turtle right
    """
    if not st[0].isdigit():
        print(st[0], "is not valid after >")
        return None
    else:
        number = get_digit(st)
        turtle.right(int(number))
        st = st[len(number):]
        shapy_turtle(st)


def square(st):
    """
    draws a square ending at the bottom left
    corner facing east with lengths of x
    """
    if not st[0].isdigit():
        print(st[0], "is not valid after S")
        return None
    else:
        number = get_digit(st)
        x = int(number)
        st = st[len(number):]
        turtle.fd(x)
        turtle.left(90)
        turtle.fd(x)
        turtle.left(90)
        turtle.fd(x)
        turtle.left(90)
        turtle.fd(x)
        turtle.left(90)
        shapy_turtle(st)


def triangle(st):
    """
    draws an equilateral triangle with lengths of x
    turtle ends facing east at the bottom left
    """
    if not st[0].isdigit():
        print(st[0], "is not valid after T")
        return None
    else:
        number = get_digit(st)
        x = int(number)
        st = st[len(number):]
        turtle.fd(x)
        turtle.left(120)
        turtle.fd(x)
        turtle.left(120)
        turtle.fd(x)
        turtle.left(120)
        shapy_turtle(st)


def circle(st):
    """
    draws a circle with raidus x
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after C")
        return None
    else:
        number = get_digit(st)
        st = st[len(number):]
        turtle.circle(int(number))
        shapy_turtle(st)


def forward(st):
    """
    moves turtle forward x units
    """
    if not st[0].isdigit():
        print(st[0], "is not valid after F")
        return None
    else:
        number = get_digit(st)
        st = st[len(number):]
        turtle.forward(int(number))
        shapy_turtle(st)


def backwards(st):
    """
    moves turtle back x units
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after B")
        return None
    else:
        number = get_digit(st)
        st = st[len(number):]
        turtle.back(int(number))
        shapy_turtle(st)


def rectangle(st):
    """
    draw a rectangle with length l and width w
    ending bottom left facing east
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after R")
        return None
    else:
        number = get_digit(st)
        l = int(number)
        st = st[len(number) + 1:]
        number = get_digit(st)
        w = int(number)
        st = st[len(number):]
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(w)
        turtle.left(90)
        shapy_turtle(st)


def polygon(st):
    """
    draw a polygon with s equal to the number of sides
    and l equal to the length of each side
    turtle ends at the bottom right of the polygon facing east
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after P")
        return None
    else:
        number = get_digit(st)
        number_of_sides = int(number)
        st = st[len(number) + 1:]
        number = get_digit(st)
        plength = int(number)
        st = st[len(number):]
        degree = 360 / number_of_sides  # determines the number of degrees between each side to create a polygon
        if number_of_sides < 3:
            pass
        else:
            while number_of_sides > 0:
                turtle.forward(plength)
                turtle.left(degree)
                number_of_sides = number_of_sides - 1
            turtle.forward(plength)
        shapy_turtle(st)


def move(st):
    """
    moves the turtle to a specific location
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after G")
        return None
    else:
        number = get_digit(st)
        x = int(number)
        st = st[len(number) + 1:]
        number = get_digit(st)
        y = int(number)
        st = st[len(number):]
        turtle.goto(x, y)
        shapy_turtle(st)


def color(st):
    """
    changes the color of the pen based on the input x value
    """
    if not st[0].isdigit():
        print(st[0:], "is not valid after Z")
        return None
    else:
        number = get_digit(st)
        x = int(number)
        st = st[len(number):]
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
    shapy_turtle(st)


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
            left(t)
        elif h == ">":
            """calls the right command"""
            right(t)
        elif h == "S":
            """calls the square command"""
            square(t)
        elif h == "T":
            """calls the triangle command"""
            triangle(t)
        elif h == "C":
            """calls the circle command"""
            circle(t)
        elif h == "F":
            """calls the forward command"""
            forward(t)
        elif h == "B":
            """calls the backward command"""
            backwards(t)
        elif h == "U":
            turtle.up()
            st = st[1:]
            shapy_turtle(st)
        elif h == "D":
            turtle.down()
            st = st[1:]
            shapy_turtle(st)
        elif h == "R":
            """calls the rectangle function"""
            rectangle(t)
        elif h == "P":
            "calls the polygon function"
            polygon(t)
        elif h == "G":
            "calls the move funcion"
            move(t)
        elif h == "Z":
            """calls the color function"""
            color(t)
        else:
            print(st[0], "is not a valid command")
            return None
    else:
        print("There are no more commands")
        return None


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


def test():
    """testing my functions"""
    print(get_digit("123C123"))
    print(get_digit("C123C123"))
    shapy_turtle("C100")
    left("90")
    right("90")
    square("10")
    triangle("10")
    circle("10")
    forward("10")
    backwards("10")
    rectangle("5,10")
    polygon("5,10")
    move("5,10")
    color("1")


def main():
    """
    main asks for a user input of shapy turtle commands
    then gives that value to shapy_turtle
    """
    shapy_turtle(input("Enter a string of shapy turtle commands: "))
    turtle.speed(2)
    turtle.done()


main()
