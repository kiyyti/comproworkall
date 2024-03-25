a = float(input('Base number:'))
b = int(input('# iterations:'))
for i in range(b):  
    a *= 2
    print(f"i: {i} , b= {a}")
print(f'Final b = {a}')