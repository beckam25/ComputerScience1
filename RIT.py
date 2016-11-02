""" 
file: RIT.py
language: python3
author: bre5933@rit.edu Brian R Eckam 
description: drawing a picture using turtles
"""
import turtle

"""
init_banner_canvas creates the world for the turtle to draw
"""
def init_banner_canvas():
  turtle.setup(1200,80)
  turtle.setworldcoordinates(-5,5,455,35)
  turtle.reset()
  turtle.up()
  turtle.pensize(2)
  turtle.speed(5)
  #end function
"""
letter_r draws the letter R in caps
"""
def letter_r():
  turtle.down()
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(30)
  turtle.left(135)
  turtle.forward(34)
  turtle.up()
  turtle.left(180)
  turtle.forward(34)
  turtle.left(135)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(60)
#end function
def letter_i():
  turtle.down()
  turtle.left(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(15)
  turtle.left(180)
  turtle.forward(30)
  turtle.left(180)
  turtle.forward(15)
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(15)
  turtle.right(180)
  turtle.forward(30)
  turtle.up()
  turtle.forward(30)
def letter_t():
  turtle.down()
  turtle.left(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(15)
  turtle.left(180)
  turtle.forward(30)
  turtle.left(180)
  turtle.forward(15)
  turtle.left(90)
  turtle.forward(30)
def rit_word():
  init_banner_canvas()
  letter_r()
  letter_i()
  letter_t()
#end of function
rit_word()
turtle.done()
