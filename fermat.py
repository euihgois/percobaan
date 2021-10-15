import math
def check_fermat(a,b,c,n):
    val=math.pow(a,n)+math.pow(b,n)==math.pow(c,n)
    if (n<=2)==True:
        print('holyshit, input correctly')
    elif val==True:
        print('sugoiii')
    else:
        print("of course, it can't")

p='please input postive integers a,b,c,d for fermat last theorem'
a=input('a = ')
b=input('b = ')
c=input('c = ')
n=input('n = ')
a=int(a)
b=int(b)
c=int(c)
n=int(n)
check_fermat(a,b,c,n


def is_triangle(a,b,c):
    if (math.pow(a,n)+math.pow(b,n)==math.pow(c,n))==True:
        print('Y')
    elif (math.pow(b,n)+math.pow(a,n)==math.pow(c,n))==True:
        print('Y')
    elif (math.pow(c,n)+math.pow(a,n)==math.pow(b,n))==True:
        print('Y')
    elif (math.pow(c,n)+math.pow(b,n)==math.pow(a,n))==True:
        print('Y')
    elif (math.pow(b,n)+math.pow(c,n)==math.pow(a,n))==True:
        print('Y')
    elif (math.pow(a,n)+math.pow(c,n)==math.pow(b,n))==True:
        print('Y')
    else:
        print('N')

pr='please input'
a=input(pr,'a = ')
b=input('b= ')
c=input('c = ')
is_triangle(a,b,c)