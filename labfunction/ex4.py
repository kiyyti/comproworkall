import math as m
def fact(n):
    if n == 0:
        return 1
    else:
        return m.factorial(n)

n = int(input("Enter n: "))

for i in range(1, n+1):
    print(f'{i}! = {m.factorial(i)}')

print('Result = ',fact(n))