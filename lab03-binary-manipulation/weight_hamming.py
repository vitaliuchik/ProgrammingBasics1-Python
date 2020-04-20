for j in range(21):
    power = 5**j
    sum = bin(power).count('1')
    print('5 **', j, ' = ', power, '  hamming weight is ', sum, end='')
    if sum % 2 == 0:
        print(' - Evil number')
    else:
        print(' - Odious number')
