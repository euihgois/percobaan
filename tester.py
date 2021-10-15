import math

def mysqrt(a):
    epsilon = 1 / 100000000000000000000000
    x = a+2
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y

def test_square_root(x,y):
    while y>=x:
        j=mysqrt(x)
        k=math.sqrt(x)
        l=abs(k-j)
        print(float(x),j-(j%0.0001),k-(k%0.0001),l)
        x=x+1

test_square_root(1,9)
