def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            return False
    return True


try:
    n = int(input())
    if (n > 2):
        flag = True
        div = 2
        while(flag):
            if(isPrime(div) and n % div != 0):
                print(div)
                flag = False
            div += 1
    else:
        print('Error')
except ValueError:
    print('Error')
except TypeError:
    print('Error')
