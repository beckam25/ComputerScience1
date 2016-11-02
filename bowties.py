"""
file: bowties.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description:
This file draws a series of bow ties starting with
one in the center followed by bow ties 1/3 the size at
each corner of the first bow tie in "rings" around it.
The placement and scaling continues for each consecutive ring.
The functions are dependant on:
        Length: How long the sides of the triangles will be
        Depth: How many consecutive "rings" there will be
"""
import turtle


def init_turtle():
    """
    Initialize the turtle. Center facing the
    right side of the bow tie. Pen up
    """
    turtle.home()
    turtle.setup()
    turtle.up()
    turtle.speed(0)
    turtle.fillcolor("red")
    turtle.pencolor("blue")


def draw_triangle(length):
    """
    Pre: Turtle up facing right
    Post: Triangle Drawn. Turtle up facing
    towards the start of the triangle. Pen up
    """
    turtle.down()
    turtle.left(30)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.left(30)
    turtle.up()


def draw_circle(length):
    """
    Pre: Turtle up in the center of the bow tie
    facing right of the bow tie
    Post: Red circle is drawn 1/4 the size of length.
    The turtle facing right in the center of the bow tie. Pen up
    """
    turtle.forward(length / 4)
    turtle.left(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(length / 4)
    turtle.end_fill()
    turtle.up()
    turtle.right(90)
    turtle.backward(length / 4)


def draw_bowtie(length):
    """
    Pre: Nothing is drawn
    Post: A bow tie is drawn. Two triangles touching at the points with a red circle
     in the middle with a blue ring. Pen Up
    """
    draw_triangle(length)
    draw_triangle(length)
    draw_circle(length)

#def test_bowtie(length):
    """
    Function to test that a bowtie is drawn with a red circle
    """
    #draw_bowtie(5)

def bowties(length, depth):
    """
    Pre: No bow ties are drawn. Turtle East
    Post: The series of bow ties are drawn with the desired
    depth prompted by the user. Turtle facing east in the middle
    of original bow tie. Pen up.
    """
    if depth <= 0:
        pass
    else:
        draw_bowtie(length)
        turtle.left(30)
        turtle.forward(length * 2)
        bowties(length / 3, depth - 1)
        turtle.back(length * 2)
        turtle.left(120)
        turtle.forward(length * 2)
        bowties(length / 3, depth - 1)
        turtle.back(length * 2)
        turtle.right(150)
        turtle.right(30)
        turtle.forward(length * 2)
        bowties(length / 3, depth - 1)
        turtle.back(length * 2)
        turtle.left(30)
        turtle.right(150)
        turtle.forward(length * 2)
        bowties(length / 3, depth - 1)
        turtle.back(length * 2)
        turtle.left(150)


def main():
    """
    The main function will:
    1: Ask the user for depth
    2: Draw the bow ties dependent on the depth input
    """
    init_turtle()
    bowties(100, int(input("what depth?: ")))
    turtle.done()


main()  # runs the main function
