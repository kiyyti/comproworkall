x = int(input('Number of values:'))
i = 0
z = 0
while x > i:
    y = float(input('value:'))
    z += y 
    i += 1
if x != 0:
    print(f'Average = {z/x}')
else:
    print(f'Average = {x}')