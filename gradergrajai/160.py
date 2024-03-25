x = int(input('Number of values:'))
i = 0
z = 1
while i < x:
    y = float(input('value:'))
    z = z*y 
    i += 1
print('Product = {:,.2f}'.format(z))