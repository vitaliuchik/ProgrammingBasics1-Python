n = int(input())
mult = 1
for i in range(1, n+1):
    if i % 7 != 0:
        mult *= i

print(mult)
