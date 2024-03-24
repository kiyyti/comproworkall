import math as m
n, k = map(int,input('Enter n and k: ').split())

def fact():
    c  = int(m.factorial(n)/(m.factorial(k)*m.factorial(n-k)))
    return c
print(f"C({n},{k}) =", fact())