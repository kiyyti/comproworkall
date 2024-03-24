import math as m
def eu(x1, y1, x2, y2):
    a = m.sqrt((x1-x2)**2 + (y1-y2)**2)
    return a

def man(x1, y1, x2, y2):
    b = abs(x1-x2) + abs(y1-y2)
    return b

x1, y1, x2, y2 = map(int,input('Enter x1, y1, x2, y2: ').split())

Eu = eu(x1, y1, x2, y2)
Ma = man(x1, y1, x2, y2)

print('Please choose your distance:')
print('\t1 Euclidean distance')
print('\t2 Manhattan distance')

n = int(input('Your choice: '))
if n == 1:
    print(f'Euclidean distance = {Eu:.5f}')
elif n == 2:
    print(f'Manhattan distance = {Ma:.5f}')