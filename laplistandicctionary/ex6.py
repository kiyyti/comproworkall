td = {}

while 1:
    tds = input('To do: ')
    if tds == '':
        break

    td[tds] = input('* details: ')

tdss = sorted(td.items())    

print(f'You have  {len(tdss)} thing(s) to do: ')
print('Work out loss function')

for i in tdss:
    print("*",i[1])
    print(f"{i[0]}")
