def factorial_recursion(n, verbose, depth=0):
    # returns n!
    if verbose:
        print("   "*depth, "factorial_recursion(", n, ")")
    if n < 1:
        return 1
    else:
        result = n * factorial_recursion(n - 1, verbose, depth+1)
    if verbose:
        print("   "*depth, "-->", result)
    return result 


def factorial_loop(n, verbose):
    # returns n!
    result = 1
    for i in range(1, n + 2):
        if verbose:
            print(str(i-1)+'! =', result)
        result *= i
    return result


def fibonacci_recursion(n, verbose, depth=0):
    # returns n fibonacci number
    if verbose:
        print("   "*depth, "fibonacci_recursion(", n, ")")
    if (n < 2):
        result = 1
    else:
        result = fibonacci_recursion(n-1, verbose, depth+1) + \
        fibonacci_recursion(n-2, verbose, depth+1)
    if verbose:
        print("   "*depth, "-->", result)
    return result


def fibonacci_loop(n, verbose):
    # returns n fibonacci number
    fib = [0, 1]
    if n == 1:
        return 1
    for i in range(1, n + 1):
        fib.append(fib[i] + fib[i - 1])
    if verbose:
        for i in range(1, n + 1):
            print(str(i)+':', fib[i])
    return fib[n]


def numbers(number, func='factorial', option='loop', verbose=False):
    """
    (int, str, str, bool) -> float
    Returns duration of working one from four functions
    """
    import timeit
    code = func + '_' + option + '(' + str(number) + ',' + verbose + ')'
    return timeit.Timer(lambda: eval(code)).timeit(number=1)


func = input('Input type of function (factorial or fibonacci): ')
option = input('Input option of function (loop or recursion): ')
number = int(input('Input number for function: '))
verbose = bool(input('Input verbose argument (True or False): '))

print(numbers(number, func=func, option=option, verbose=verbose))