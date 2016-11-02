import turtle
'''
draw_triangle() will draw a triangle
'''
def draw_triangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(30)
#end of function
'''
turtle home brings the turtle to the middle facing east
'''
turtle.home()
'''
the next four lines will draw four triangles
30 degrees apart and touching at the center
'''
draw_triangle()
turtle.done()

