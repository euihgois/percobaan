import math

def is_triangle(a,b,c):
    n=2
    if (math.pow(a,n)+math.pow(b,n)==math.pow(c,2))==True:
        print('Y')
    elif (math.pow(b,n)+math.pow(a,n)==math.pow(c,2))==True:
        print('Y')
    elif (math.pow(c,n)+math.pow(a,n)==math.pow(b,2))==True:
        print('Y')
    elif (math.pow(c,n)+math.pow(b,n)==math.pow(a,2))==True:
        print('Y')
    elif (math.pow(b,n)+math.pow(c,n)==math.pow(a,2))==True:
        print('Y')
    elif (math.pow(a,n)+math.pow(c,n)==math.pow(b,2))==True:
        print('Y')
    else:
        print('N')

pr='please input'
print(pr)
s=input('a = ')
d=input('b= ')
f=input('c = ')
a=int(s)
b=int(d)
c=int(f)
is_triangle(a,b,c)