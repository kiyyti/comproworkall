import math as m
a, b, c = map(int,input('Enter coefficients a, b, c: ').split())

if a == 0:
    print('This equation is not quadratic.')
elif b**2 - 4*a*c < 0:
    print('This equation has complex roots.')
else:
    st1 = (-b + m.sqrt(b**2 - 4*a*c))/2*a
    st2 = (-b - m.sqrt(b**2 - 4*a*c))/2*a
    print(f'The 1st root = {st1:.2f}')
    print(f'The 2nd root = {st2:.2f}')