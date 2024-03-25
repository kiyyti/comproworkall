a = float(input('Base number:'))
c = float(input('Ceiling:'))
i = 0#
while a>=c:
    a/=2
    print(f'b = {a}')
    i+=1
print(f'Final b = {a} after {i} iteration(s).')