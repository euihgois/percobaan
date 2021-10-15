def gcd(a,b):
    if a==0 and b==0:
        return print('type correctly')
    elif a==0:
        return b
    elif b==0:
        return a
    elif abs(a)>=abs(b):
        return gcd(a%b,b)
    elif abs(a)<abs(b):
        return gcd(b%a,a)

print(gcd(1052,20102))