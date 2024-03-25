a = float(input('Enter voltage (V): '))
b = float(input('Enter current (A): '))
c = float(input('Enter operating time (h): '))
print(f'The cost is {(((a*b)*c)/1000)*4}')
