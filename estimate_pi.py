import math


def mysqrt(a):
    epsilon = 1 / 1000000000000000000
    x = a + 2
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def formula(k):
    return factorial(4 * k) * (1103 + 26390 * k) / (factorial(k) ** 4 * (396 ** (4 * k)))


def estimate_pi():
    k = 0
    sigma = formula(k)
    while formula(k) > 1e-15:
        k = k + 1
        sigma = sigma + formula(k)
    return 1 / ((2 * mysqrt(2) / 9801) * sigma)


def diff():
    return abs(estimate_pi() - math.pi)


print(mysqrt(2))
print(factorial(3))
print(estimate_pi())
print(diff())
