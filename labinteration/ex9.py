x = int(input('Enter n: '))
for i in range(x):
    for j in range(x):
        if i == j or i+j == x-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()