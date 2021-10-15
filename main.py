import math
import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
      for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
        angle = 360.0/n
        polyline(t, n, length, angle)

def arc(t, r, angle):
        arc_length = 2 * math.pi * r * abs(angle) / 360
        n = int(arc_length / 3) + 3
        step_length = arc_length / n
        step_angle = float(angle) / n
        t.lt(step_angle/2)
        polyline(t, n, step_length, step_angle)
        t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)


def flower (t,k,a,n):
    for i in range(n):
        angle = 360/n
        petal(t,k,a)
        t.lt(angle

def petal(t, k, a):
    for i in range(2):
         h = k / 2
         R = (h + math.pow(a, 2) / (4 * h)) / 2
         j = 2 * math.asin(a / (2 * R))
         angle = math.degrees(j)
         arc(t, R, angle)
         t.lt(180 - angle)

def line (t,length):
    for i in range(2):
        t.fd(length)
        t.lt(180)

def pie (t,n,radius):
    length=radius*(2*math.sin(math.radians(180/n)))
    step=360/n
    for i in range(n):
        line (t,radius)
        t.lt(step)
    t.pu()
    t.fd(radius)
    t.pd()
    t.lt(180-(180-step)/2)
    polygon(t,n,length)


bob = turtle.Turtle()

def poly_arc(t,n,a_step):
    a_0=0
    r_0=0
    for i in range(n):
        arc(t,r_0,a_0)
        a_0=a_0+a_step
        r_0=a_0

def arch(t,laps):
    a_step=2
    n=int(laps/a_step)
    poly_arc(t,n,a_step)

def asoy():
    pass


arch(bob,360)
bob.hideturtle()
turtle.mainloop()


