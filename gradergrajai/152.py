a = int(input('a: '))
b = int(input('b: '))

if a==0 and b==0:
    print(f'a/b = Not defined')
elif a<0 and b==0:
    print('a/b = Negative Infinity')
elif a>0 and b==0:
    print('a/b = Infinity')
else:
    print(f'a/b = {a/b}')