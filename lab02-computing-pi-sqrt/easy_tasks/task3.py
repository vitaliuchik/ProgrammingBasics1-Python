import math

r = float(eval(input()))
V = round(4/3 * math.pi * r**3, 3)
A = round(4 * math.pi * r**2, 3)

if ((V - int(V)) == 0):
    V = int(V)
if ((A - int(A)) == 0):
    A = int(A)

print('V = ', V)
print('A = ', A)
