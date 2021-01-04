import turtle
import math

bob = turtle.Turtle()

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    frac = angle/360
    arc_length = circumference * frac
    n = 50
    len = arc_length/n
    turn_ang = angle/n
    for i in range(n):
        t.fd(len)
        t.lt(turn_ang)

arc(bob, 50, 180)
