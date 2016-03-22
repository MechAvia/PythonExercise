"""
Created on Mon Mar 21 22:03:37 2016
This program draws a Koch snowflake using recursion function
@author: DJ
"""

import turtle

def draw_koch(size, order, t):
    if order == 0:              #Most basic koch element, which is line
        t.forward(size/3)

    else:
        for angle in [60, -120, 60, 0]:      #Draw a _/\_ shape
            draw_koch(size/3, order-1, t)
            t.right(angle)

        
a = turtle.Screen()

myturtle = turtle.Turtle()
myturtle.speed(0)

for turn_angle in [120, 120, 0]:            #Loop the _/\_ shape 3 times to form a triangle
    draw_koch(1500, 4, myturtle)
    myturtle.left(turn_angle)


a.exitonclick()
        