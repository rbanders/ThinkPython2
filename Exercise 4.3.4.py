import turtle
import math

bob = turtle.Turtle()

def circle(t,r, n):
    circumference = 2 * math.pi * r
    length = circumference/n
    polygon(t, 360, 1)

def polygon(t,n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

circle(bob, 5, 360)