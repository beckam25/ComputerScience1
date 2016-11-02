""" 
file: fourway_button.py
language: python3
author: bre5933@rit.edu Brian R Eckam 
description: drawing a picture using turtles
"""
import turtle
'''
init_turtle() initializes the turtle
to the middle of the screen facing north
'''
def init_turtle():
  turtle.up()
  turtle.home()
  turtle.setheading(90)
#end of the function
'''
draw_triangle() will draw an equilateral
triangle with the point facing the corner
'''
def draw_triangle():
  turtle.down()
  turtle.right(90)
  turtle.forward(50)
  turtle.left(120)
  turtle.forward(100)
  turtle.left(120)
  turtle.forward(100)
  turtle.left(120)
  turtle.forward(50)
#end of the function
'''
program begins here
'''
init_turtle()#calls init_turtle
turtle.forward(200)
turtle.left(90)
turtle.down()
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
#the square outline is drawn
init_turtle()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.down()
turtle.circle(50)
#the circle in the middle is drawn
init_turtle()
turtle.left(45)#upper left triangle location
turtle.forward(150)
draw_triangle()#calls draw_triangle
init_turtle()
turtle.right(45)#upper right triangle location
turtle.forward(150)
draw_triangle()#calls draw_triangle
init_turtle()
turtle.left(135)#lower left triangle location
turtle.forward(150)
draw_triangle()#calls draw_triangle
init_turtle()
turtle.right(135)#lower right triangle location
turtle.forward(150)
draw_triangle()#calls draw_triangle

turtle.done()
