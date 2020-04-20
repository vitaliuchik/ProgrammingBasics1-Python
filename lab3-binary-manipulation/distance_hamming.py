num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result_num = bin(num1 ^ num2).count('1')
print('Hamming distance = ', result_num)
