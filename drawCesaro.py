"""
Created on Tue Mar 22 14:07:04 2016
This program draws the Cesaro torn using recursive programming
@author: DJ
"""

import turtle

def draw_ces(size, order, angle, t):
    if order == 0:
        t.forward(size)
    else:
        draw_ces(size/2.0, order-1, angle, t)
        t.right(90-angle/2.0)
        draw_ces(size/2.0, order-1, angle, t)
        t.left(180-angle)
        draw_ces(size/2.0, order-1, angle, t)
        t.right(90-angle/2.0)
        draw_ces(size/2.0, order-1, angle, t)

a = turtle.Screen()

dragon = turtle.Turtle()
dragon.speed(0)
draw_ces(200, 3, 13, dragon)

a.exitonclick()          