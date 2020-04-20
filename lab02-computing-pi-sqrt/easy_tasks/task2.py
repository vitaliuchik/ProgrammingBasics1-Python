a = int(input())
b = int(input())
for i in range(a):
    if(i > 0 and i < a-1 and b > 2):
        print('*'+' '*(b-2)+'*')
    else:
        print(b*'*')
