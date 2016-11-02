"""
file: raindrops.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This Program draws a a series of raindrops with ripples.
The # of raindrop and # of ripples are randomly generated within a
given range. The raindrops must fit within the default turtle window.
"""

import turtle
import random
import math


def box():
    """
    DRAWS THE BOUNDING BOX
    """
    turtle.speed(0)
    turtle.hideturtle()
    turtle.up()
    turtle.forward(300)
    turtle.down()
    turtle.pencolor("blue")
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(250)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.pencolor("black")


def MAX_RAINDROPS():
    """Maximum number of raindrops"""
    return 100


def MIN_RAINDROPS():
    """Minimum number of raindrops"""
    return 1


def MAX_RADIUS():
    """Maximum radius of a raindrop"""
    return 20


def MIN_RADIUS():
    """Minimum radius of a raindrop"""
    return 1


def MAXIMUM_X_VALUE():
    """Max value of x coordinate of the box"""
    return 250


def MINIMUM_X_VALUE():
    """Min value of x coordinate of the box"""
    return -250


def MAXIMUM_Y_VALUE():
    """Max value of y coordinate of the box"""
    return 250


def MINIMUM_Y_VALUE():
    """Min value of y coordinate of the box"""
    return -250


def MINIMUM_RIPPLE():
    """Minumum number of ripples"""
    return 3


def MAXIMUM_RIPPLE():
    """Maximum number of ripples"""
    return 8

def draw_rec(n):
    """
    Pre: No drops drawn
    Post: The user input number of drops is drawn with the randomly
    generated ripples

    draw_rec is the function that draws each individual raindrop.
    It takes a random number r, radius, and creates a circle with
    that radius at a random (x,y) location. It then fills in the circle
    with a randomly generated color.

    r = radius
    x = x value of (x,y) coordinate
    y = y value of (x,y) coordinate
    ripple = number of ripples
    xvalue = absolute value of the difference between the max value
    of x and the absolute value of the x coordinate
    yvalue = absolute value of the difference between the max value
    of y and the absolute value of the y coordinate
    """
    total_area = 0
    if n <= 0:
        return total_area
    else:
        r = random.randint(MIN_RADIUS(), MAX_RADIUS())
        x = random.randint(MINIMUM_X_VALUE(), MAXIMUM_X_VALUE())
        y = random.randint(MINIMUM_Y_VALUE(), MAXIMUM_Y_VALUE())
        ripple = random.randint(MINIMUM_RIPPLE(), MAXIMUM_RIPPLE())
        xvalue = abs(MAXIMUM_X_VALUE() - abs(x))
        yvalue = abs(MAXIMUM_Y_VALUE() - abs(y))
        if r > xvalue or r > yvalue:
            total_area += draw_rec(n)
            return total_area
        else:
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            red = random.random()
            green = random.random()
            blue = random.random()
            turtle.fillcolor(red, green, blue)
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
            total_area += math.pi * r ** 2  # this equals pi*r^2 + area
            draw_iter(r, ripple, x, y)
            total_area = draw_rec(n-1) + total_area
        return total_area

def draw_iter(r, ripple,x,y):
    """
    Pre: No ripples drawn
    Post: The randomly generated number of ripples is drawn

    draw_iter is used to draw the ripples around the original raindrop.
    The function will check to see if the ripple stays within the drawn
    boundary. If the ripple can be drawn without going outside the boundary
    then it will be drawn.
    """
    n = r
    while ripple > 0:
        if x + n < MAXIMUM_X_VALUE()- r and y + n < MAXIMUM_Y_VALUE() - r \
                and x - n > MINIMUM_X_VALUE() + r and y - n > MINIMUM_Y_VALUE() + r:
            turtle.up()
            turtle.setheading(0)
            turtle.forward(r)
            turtle.setheading(90)
            turtle.down()
            n = n + r
            turtle.circle(n)
            ripple = ripple - 1
        else:
            ripple = 0


#def test_ripple():
#   draw_iter(20, 8)


def main():
    """
    Pre: No turtle window open. Nothing drawn.
    Post: The user input raindrops are drawn with the correct number
    of randomly generated ripples.

    main() asks for the user to enter a number for the amount of
    raindrops to be drawn. If the number is within the boundaries then
    the raindrops will be drawn.
    """
    n = int(input("Enter the number of raindrops: "))
    if n > MAX_RAINDROPS() or n < MIN_RAINDROPS():
        print("Raindrops must be between 1 and 100 inclusive")
        exit()
    else:
        turtle.fillcolor("blue")
        turtle.begin_fill()
        box()
        turtle.end_fill()
        print("Raindrops (1-100): ", n)
        print ("The total area of the raindrops is",draw_rec(n), "square units")
    turtle.done()

main()