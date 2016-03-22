"""
Created on Mon Mar 21 22:43:10 2016
This program draws the Sierpinski triangle using recursive functions.
@author: DJ
"""

# This program needs to draw borders after drawing the recursive parts

import turtle

def draw_tri(size, order, t):
    if order > 0:
        t.left(120)
        for angle in [120, 120, -120]:
            t.forward(size/2)
            draw_tri(size/2, order-1, t)
            t.forward(size/2)
            t.right(angle)
#    if order == 0:
#    for angle in [120, 120, 120]:
#        if order > 1:
#            draw_tri(size/2, order - 1, t)
#        t.forward(size)
#        t.left(angle)
#    else:
#        draw_tri(size/2, order-1, t)
#        t.forward(size/2)
#        draw_tri(size/2, order-1, t)
#        t.left(120)
#        t.forward(size/2)
#        t.right(120)
#        draw_tri(size/2, order-1, t)
#        t.right(120)
#        t.forward(size/2)
#        t.left(120)

a = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.speed(8)

draw_tri(100, 5, myturtle)

a.exitonclick()
