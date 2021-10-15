import turtle
import math
c=200
bob = turtle.Turtle()
alice = turtle.Turtle()
print(bob)
""""aaiiai
a"""
def polygon(t,length,n):
    #ddd
    for i in range(n):
        t.fd(length)
        t.lt(360/c)

def arc(t,r,angle):
    fcircle=angle/360
    circumference=2*math.pi*r
    length=circumference/c
    n=int(fcircle*c)
    polygon(t,length,n)

arc(bob,40,180)

turtle.mainloop()