day = int(input('How many day? '))
x,y = 0,1
for i in range(day):
    x,y = y,x+y
print(f'{day}-day height is {x} cm.')