""" 
file: turtle_name.py
language: python3
author: bre5933@rit.edu Brian R Eckam 
description: Using turtles, I will draw the words TURTLE BRE5933@RIT.EDU
"""
import turtle
import math


def init_banner_canvas():
    """
    init_banner_canvas creates the world for the turtle to draw as well as
    positions the turtle in the lower left hand corner of the world
    """
    turtle.setup(1200, 80)
    turtle.setworldcoordinates(-5, 5, 455, 35)
    turtle.reset()
    turtle.up()
    turtle.pensize(2)
    turtle.speed(5)


# end of function

def letter_r():
    """
    letter_r() draws the letter R in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(145)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(125)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.up()
    turtle.forward(17.5)


# end of function

def test_letter_r():
    """
    this function will test to make sure letter r lines up correctly once it is drawn
    """
    letter_r()
    letter_r()  # call it twice
    turtle.done()


# end of cuntion

def letter_i():
    """
    letter_i() draws the letter I in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.up()
    turtle.forward(10)


# end of function

def letter_t():
    """
    letter_t() draws the letter T in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.forward(7.5)
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.up()
    turtle.forward(10)


# end of function

def letter_b():
    """
    letter_b() draws the letter B in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.up()
    turtle.forward(17.5)


# end of function

def letter_e():
    """
    letter_e() draws the letter E in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.right(180)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.forward(2.5)


# end of function

def number_5():
    """
    number_5() draws the number 5 and leaves a 5 point space at the
    end of the number
    """
    turtle.down()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(2.5)


# end of function

def number_9():
    """
    number_9() draws the number 9 and leaves a 5 point space at the
    end of the number
    """
    turtle.left(90)
    turtle.forward(7.5)
    turtle.down()
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.left(90)
    turtle.up()
    turtle.forward(2.5)


# end of function

def number_3():
    """
    number_3() draws the number 3 and leaves a 5 point space at the
    end of the number
    """
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(180)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(7.5)
    turtle.right(90)
    turtle.forward(15)
    turtle.up()
    turtle.right(180)
    turtle.forward(17.5)


# end of function

def letter_u():
    """
    letter_u() draws the letter U in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.up()
    turtle.forward(2.5)


# end of function

def letter_l():
    """
    letter_l() draws the letter L in caps and leaves a 5 point space at
    the end of the letter
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.up()
    turtle.forward(2.5)


# end of function

def letter_d():
    """
    letter_d() draws the letter D in caps and leaves a 5 point space at
    the end of the letter
    """
    a = math.sqrt(50)  # this math is needed to draw the angles for D
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(5)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(10)
    turtle.right(180)
    turtle.up()
    turtle.forward(17.5)


# end of function

def at_symbol():
    """
    at_symbol() will create the @ symbol
    """
    turtle.forward(7.5)
    turtle.down()
    turtle.circle(7.5)
    turtle.up()
    turtle.left(90)
    turtle.forward(3.75)
    turtle.down()
    turtle.right(90)
    turtle.circle(3.75)
    turtle.up()
    turtle.left(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(2.5)
    turtle.right(45)
    turtle.down()
    turtle.forward(3.75)
    turtle.up()
    turtle.right(180)
    turtle.forward(3.75)
    turtle.left(45)
    turtle.forward(2.5)
    turtle.left(90)
    turtle.forward(4.75)
    turtle.left(90)
    turtle.forward(10)


# end of function

def dot_symbol():
    """
    dot_symbol() will creat a period punctuation mark
    """
    turtle.down()
    turtle.circle(1)
    turtle.up()
    turtle.forward(5)


# end of function

def turtle_name():
    """
    turtle_name will draw the characters in the order that is displayed below
    """
    letter_t()
    letter_u()
    letter_r()
    letter_t()
    letter_l()
    letter_e()
    turtle.forward(7.5)  # puts a space between E and B
    letter_b()
    letter_r()
    letter_e()
    number_5()
    number_9()
    number_3()
    number_3()
    at_symbol()
    letter_r()
    letter_i()
    letter_t()
    dot_symbol()
    letter_e()
    letter_d()
    letter_u()


# end of function

def move_turtle():
    """
    the next three lines of code move the turtle
    to the middle of the canvas and face east
    """
    turtle.left(90)
    turtle.forward(7.5)
    turtle.right(90)


# end of function

def main():
    init_banner_canvas()  # calls init_banner_canvas() - creates canvas
    move_turtle()  # moves the turtle to desired location
    # test_letter_r()
    # function was used to test letters
    turtle_name()  # calls turtle_name() function
    turtle.done()  # keeps the turtle window open until the user closes it


main()  # calls the main function
