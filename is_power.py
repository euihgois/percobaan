def is_power(a,b):
    if a%b==0:
        return is_power(a/b,b)
    elif a%b==1 and a//b==0:
        return True
    elif a%b!=0:
        return False


print(is_power(729,3))