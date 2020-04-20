import math


def newton(n):
    epsilon = 0.01
    guess = n / 2.0
    count = 0
    while abs(guess**2 - n) >= epsilon:
        guess -= (((guess**2) - n) / (2*guess))
        count += 1
    print('Newton-Raphson')
    print('Root: ', guess)
    print('Difference: ', abs(guess - math.sqrt(n)))
    print('Iterations: ', count)


def bisection(n):
    epsilon = 0.01
    count = 0
    low = 0.0
    high = max(1.0, n)
    ans = (high + low) / 2.0
    while abs(ans**2 - n) >= epsilon:
        count += 1
        if ans**2 < n:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print('Bisection search')
    print('Root: ', ans)
    print('Difference: ', abs(ans - math.sqrt(n)))
    print('Iterations: ', count)


def exhaustive(n):
    epsilon = 0.01
    step = epsilon**2
    count = 0
    ans = 0.0
    while abs(ans**2 - n) >= epsilon and ans <= n:
        ans += step
        count += 1
    if abs(ans**2 - n) >= epsilon:
        print('Failed')
    else:
        print('Exhaustive enumeration')
        print('Root: ', ans)
        print('Difference: ', abs(ans - math.sqrt(n)))
        print('Iterations: ', count)


x = float(input())

exhaustive(x)
bisection(x)
newton(x)


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
