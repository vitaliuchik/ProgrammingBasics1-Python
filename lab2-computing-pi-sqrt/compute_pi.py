import math


def leibniz():
    n = int(input('Input leibniz pow: '))
    pi = 0
    plus = True
    count = 0
    for i in range(1, 2*10**n + 1, 2):
        count += 1
        if plus:
            pi += 1/i
            plus = False
        else:
            pi -= 1/i
            plus = True
    pi *= 4
    print(count)
    print(pi - math.pi)


def archimed():
    a = 2**0.5
    k = 0
    count = 4
    n = int(input('Input archimed iteration (The best result - 13): '))
    while k < n:
        a = (2 - 2 * (1 - a**2 / 4)**0.5)**0.5
        count *= 2
        k += 1
    pi = count * a / 2
    print(count)
    print(pi - math.pi)


def chudn():
    n = int(input('Input chudn iteration : '))
    pi = 13591409
    a = 1
    k = 1
    while k < n:
        a *= -((6*k-5)*(2*k-1)*(6*k-1))/(k**3*26680*640320**2)
        nex = a*(13591409 + 545140134*k)
        pi += nex
        k += 1
    pi = pi * 10005**0.5 / 4270934400
    pi = 1 / pi
    count = k - 1
    print(count)
    print(pi - math.pi)


leibniz()
archimed()
chudn()
