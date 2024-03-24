totle = 0
for i in range(1,4):
    print(f'Student {i}')
    for j in range(1,6):
        sum = int(input(f'\tSubject {j}: '))
        totle += sum
    print(f'Totle score of student {i} is {totle}.')